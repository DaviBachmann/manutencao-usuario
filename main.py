from core.utils import limpa_tela, carregar_arquivo_env
from features.input_handler import coleta_acao, coleta_query_params
from features.operations import executar

def main():
    limpa_tela()
    
    acao = coleta_acao()
        
    try:
        carregar_arquivo_env()
        
    except Exception as e:
        print(f"Erro ao carregar variáveis de ambiente: {e}")
        
    limpa_tela()
    print(f'Ação: {'Cadastro' if acao == 'cad' else 'Exclusão'}\n')
    
    params = coleta_query_params()

    limpa_tela()
    print(f'Ação: {'Cadastro' if acao == 'cad' else 'Exclusão'}')
    print(f"Nome: {params[0]}\nLogin: {params[1]}\n")
    
    executar(acao, params)
    
    print("Todas as execuções foram realizadas!")
    if acao == 'cad':
        print("A senha padrão é 'Suporte@123'. Por questões de segurança, altere no monitor assim que possível!\n")
    input('Pressione ENTER para sair')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print('\n\nPrograma encerrado pelo usuário')
        input('Pressione ENTER para sair')
    except Exception as e:
        input('[ERRO] Pressione ENTER para sair')