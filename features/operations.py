import os

from core.db_utils import conectar_banco, executar_query, fechar_conexao

def executar(
    acao: str,
    params: tuple
) -> None:
    
    db_names = {
        'SaaS': {
            'NFe': 'saas_nfepack_prd',
            'NFe2': 'saas2_nfepack_prd',
            'CTe': 'saas_ctepack_prd',
            'CTe2': 'saas_ctepack2_prd',
            'NFCe': 'saas_nfcepack_prd',
            'MDFe': 'saas_mdfepack_prd',
            'NFSeOut': 'saas_nfse_soft_prd',
            'NFSeIn': 'saas_nfsre_prd'
        },
        'DHL': {
            'CTe2': 'dhl_cte_prd'
        },
        'Shein': {
            'CTe2': 'shein_cte_prd'
        },
        'Nissei': {
            'NFe': 'nissei_nfepack_prd',
            'CTe': 'nissei_ctepack_prd',
            'NFCe': 'nissei_nfcepack_prd',
            'MDFe': 'nissei_mdfepack_prd'
        },
        'Accor': {
            'NFSeOut': 'accor_nfsepack_prd'
        },
        'InfoGlobo': {
            'NFe': 'infoglobo_nfepack_prd'
        },
        'VIVO': {
            'NFCe': 'vivo_nfce_prd'
        }
    }
        
    for tennant in db_names:
        
        try:
            db_server = os.getenv(f"db_server_{tennant}")
            db_user = os.getenv(f"db_user_{tennant}")
            db_password = os.getenv(f"db_password_{tennant}")
        except Exception as e:
            print(f"Erro ao carregar variáveis de ambiente: {e}")
        
        print(tennant)
        
        for produto in db_names[tennant]:
            conn = None
            db_name = db_names[tennant][produto]
        
            try:
                conn = conectar_banco(db_server, db_name, db_user, db_password)
                if acao == 'cad':
                    if executar_cad(conn, produto, params) == False:
                        continue
                    print(f'  [{produto}] Cadastro realizado')
                else:
                    if executar_exc(conn, produto, params) == False:
                        continue
                    print(f"  [{produto}] Desativação realizada")
                    
            except Exception as e:
                print(f"  [{produto}] Falha na execução: {str(e)}")
            finally:
                if conn:
                    fechar_conexao(conn)
                    
        print('')
                
def executar_cad(conn, produto, params):
    queries = {
        'NFe': ["db_nfe_insert_emis1", "db_nfe_insert_emis2", "db_nfe_insert_dest1", "db_nfe_insert_dest2", "db_nfe_insert_trans1", "db_nfe_insert_trans2", "db_nfe_insert_oper"],
        'NFe2': ["db_nfe2_insert_emis1", "db_nfe2_insert_emis2", "db_nfe2_insert_dest1", "db_nfe2_insert_dest2", "db_nfe2_insert_trans1", "db_nfe2_insert_trans2", "db_nfe2_insert_oper"],
        'NFCe': ["db_nfce_insert_emis1", "db_nfce_insert_emis2", "db_nfce_insert_dest1", "db_nfce_insert_dest2", "db_nfce_insert_trans1", "db_nfce_insert_trans2", "db_nfce_insert_oper"],
        'CTe': ["db_cte_insert_permis"],
        'CTe2': ["db_cte2_insert_permis"],
        'MDFe': ["db_mdfe_insert_permis"],
        'NFSeOut': ["db_nfseout_insert_permis"]
    }
    
    login_key_env = f"db_{produto}_select_login"
    db_select_login = os.getenv(login_key_env)
    
    try:
        resultado = executar_query(conn, db_select_login, params=params[1], fetch=True)
        if resultado[0]:
            print(f'  [{produto}] Erro ao tentar cadastrar usuário duplicado')
            return False
        
    except Exception as e:
        print(f"  [{produto}] Falha no cadastro: {str(e)}")
        return False
    
    usuar_key_env = f"db_{produto}_insert_usuar"
    db_insert_usuar = os.getenv(usuar_key_env)
    
    id_key_env = f"db_{produto}_select_id"
    db_select_id = os.getenv(id_key_env)
    
    try:
        if not executar_query(conn, db_insert_usuar, params=params, commit=True):
            print(f"  [{produto}] Falha no cadastro: Não foi possível cadastrar o usuário")
            return False
        resultado = executar_query(conn, db_select_id, params=params, fetch=True)[0]
        if resultado:
            id = resultado[0][0]
        else:
            print(f"  [{produto}] Falha no cadastro: Não foi possível localizar o ID do usuário cadastrado")
            return False
        
    except Exception as e:
        print(f"  [{produto}] Falha no cadastro: {str(e)}")
        return False
    
    if produto in ('CTe', 'CTe2', 'MDFe', 'NFSeOut'):
        max_role_key_env = f"db_{produto}_select_max_role"
        db_select_max_role = os.getenv(max_role_key_env)
        
        try:
            resultado = executar_query(conn, db_select_max_role, fetch=True)[0]
            if resultado:
                max_role = resultado[0][0]
            else:
                print(f"  [{produto}] Falha no cadastro: Não foi possível coletar valores específicos do banco de dados")
                return False
            
        except Exception as e:
            print(f"  [{produto}] Falha no cadastro: {str(e)}")
            return False
    
    if produto in queries:
        for key in queries[produto]:
            query = os.getenv(key)
            
            if produto in ('NFe', 'NFe2', 'NFCe'):
                executar_query(conn, query, params=int(id), commit=True)
                
            elif produto in ('CTe', 'CTe2', 'NFSeOut'):
                for role in range(1, max_role+1):
                    executar_query(conn, query, params=(role, int(id)), commit=True)
                    
            elif produto == 'MDFe':
                for role in (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
                    executar_query(conn, query, params=(role, int(id)), commit=True)
        
def executar_exc(conn, produto, params):
    delete_key_env = f"db_{produto}_delete"
    db_delete = os.getenv(delete_key_env)
    
    id_key_env = f"db_{produto}_select_id"
    db_select_id = os.getenv(id_key_env)
    
    try:
        resultado = executar_query(conn, db_select_id, params=params, fetch=True)[0]
        if resultado:
            id = resultado[0][0]
        else:
            print(f"  [{produto}] Falha na desativação: Usuário não encontrado")
            return False
        executar_query(conn, db_delete, params=(id), commit=True)
    except Exception as e:
        print(f"  [{produto}] Falha na desativação: {str(e)}")
        return False