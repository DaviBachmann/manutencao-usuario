from core.utils import menu

def coleta_acao():
    acao = menu(
    {
        '1': 'cad',
        '2': 'exc'
    },
    """
===========================================
                   Ação:                 
|1 - Cadastrar usuário
|2 - Excluir usuário
==========================================="""
    )
    
    return acao

def coleta_produtos():
    produtos = []
    
    print("""
Selecione um produto por vez:
===========================================
                Produtos:    
|0 - Parar de add     |4 - MDFe
|1 - NFe              |5 - NFSe Out
|2 - CTe              |6 - NFSe In
|3 - NFCe             |7 - Todos
===========================================""")
    
    while True:
        produto = menu(
            {
                '0': False,
                '1': 'NFe',
                '2': 'CTe',
                '3': 'NFCe',
                '4': 'MDFe',
                '5': 'NFSeOut',
                '6': 'NFSeIn',
                '7': True
            }
        )
        
        if produto == True:
            produtos = ['NFe', 'CTe', 'NFCe', 'MDFe', 'NFSeOut', 'NFSeIn']
            break
        
        if produto == False:
            break
        
        if produto not in produtos:
            produtos.append(produto)
            print(produtos, '\n')
        else:
            print('Este produto já foi escolhido.')
            print(produtos, '\n')
        
    print('\n')
        
    return produtos

def valida_entrada(
    param: str,
    nulo: bool = False,
    comprimento: int = None,
    especiais: bool = False
) -> str:
    
    def validar_caracteres(param):
        caracteres_invalidos = ('[', ']', '{', '}', '!', '#', '$', '%', '¨', '&', '*', '(', ')', '+', '=', '"', "'", '\\', '|', '?', '/', ':', ';', ',')
        for caracter in param:
            if caracter in caracteres_invalidos:
                return False
                    
        return True
    
    while True:
    
        if nulo:
            if param.upper() in ('', 'NULL'):
                param = input(f'Não é permitido um valor vazio ou nulo, favor inserir novamente: \n>> ')
                continue
        
        if comprimento:
            if len(param) > comprimento:
                param = input(f'Limite de caracteres excedido ({len(param)}) (limite = {comprimento})\nFavor inserir novamente: \n>> ')
                continue
                
        if especiais:
            if validar_caracteres(param) == False:
                param = input(f'Caracteres inválidos, favor inserir novamente: \n>> ')
                continue
            
        break
    return param

def coleta_query_params(nome=True, login=True, senha=True):
    
    saida = []
    
    if nome:
        nome = input('Insira o nome do usuário (Exemplo da Silva): \n>> ').strip()
        nome = valida_entrada(nome, nulo=True, comprimento=40, especiais=True)
        saida.append(nome)
                
    if login:
        login = input('\nInsira o login do usuáiro (exemplo.da.silva): \n>> ').strip()
        login = valida_entrada(login, nulo=True, comprimento=255, especiais=True)
        saida.append(login)
            
    return tuple(saida)