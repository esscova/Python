"""
    SECAO 3 - ESTRUTURAS DE DADOS
    EXERCICIO 04
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-24
    OBJETIVO:
        - PRATICAR ESTRUTURAS DE DADOS
        - OPERAÇÕES COM ESTRUTURAS DE DADOS
        - UNIR FLUXOS DE CONTROLE E REPETIÇÃO COM ESTRUTURAS DE DADOS
"""
figurinhas = []

while True:
    print("""
        =======   MENU   =======
        1 - Adicionar figurinha
        2 - Remover figurinha
        3 - Buscar figurinha
        4 - Mostrar álbum
        5 - Encerrar
    """)
    
    opcao = input('Escolha uma opção: ').strip()

    if opcao == '1':
        nova_fig = input('Nome da figurinha a adicionar: ').strip().title()
        figurinhas.append(nova_fig)  
        print(f'"{nova_fig}" foi adicionada com sucesso!')

    elif opcao == '2':
        fig_remover = input('Nome da figurinha a remover: ').strip().title()
        if fig_remover in figurinhas:
            figurinhas.remove(fig_remover)  
            print(f'"{fig_remover}" foi removida do álbum.')
        else:
            print('Figurinha não encontrada no álbum.')

    elif opcao == '3':
        fig_buscar = input('Nome da figurinha a buscar: ').strip().title()
        if fig_buscar in figurinhas:
            print(f'A figurinha "{fig_buscar}" ESTÁ no álbum!')
        else:
            print(f'A figurinha "{fig_buscar}" NÃO está no álbum.')

    elif opcao == '4':
        if not figurinhas:
            print('O álbum está vazio no momento.')
        else:
            print('\n--- FIGURINHAS NO ÁLBUM ---')
            for idx, fig in enumerate(figurinhas, start=1):
                print(f'{idx}. {fig}')

    elif opcao == '5':
        print('Encerrando o programa do álbum. Até mais!')
        break

    else:
        print('Opção inválida! Por favor, escolha um número de 1 a 5.')