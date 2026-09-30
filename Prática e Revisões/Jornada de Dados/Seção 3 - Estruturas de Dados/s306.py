"""
    SECAO 3 - ESTRUTURAS DE DADOS
    EXERCICIO 06
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-28
    OBJETIVO:
        - PRATICAR ESTRUTURAS DE DADOS
        - OPERAÇÕES COM ESTRUTURAS DE DADOS
        - UNIR FLUXOS DE CONTROLE E REPETIÇÃO COM ESTRUTURAS DE DADOS
"""

partidas = []

print('\n=== SISTEMA DA COPA DO MUNDO ===')

# LOOP DE CADASTRO
while True:
    opcao = input('\nDeseja cadastrar uma partida? [S/N]: ').strip().lower()

    if opcao == 's': # cadastrar?
        partida = {}
        partida['mandante'] = input('Seleção mandante: ').strip().title()
        partida['visitante'] = input('Seleção visitante: ').strip().title()

        # loop de validação de gols com tratamento de erro
        while True:
            try:
                gols_m = int(input(f'Gols do {partida["mandante"]}: ').strip())
                gols_v = int(input(f'Gols do {partida["visitante"]}: ').strip())

                if gols_m >= 0 and gols_v >= 0:
                    partida['gols_mandante'] = gols_m
                    partida['gols_visitante'] = gols_v
                    break
                else:
                    print('Erro: A quantidade de gols não pode ser negativa.')
            except ValueError:
                print('Erro: Digite apenas números inteiros válidos.')

        # dict na lista
        partidas.append(partida)
        print('Partida cadastrada com sucesso!')

    elif opcao == 'n': #cadastrar?
        print('\nEncerrando cadastro de partidas...')
        break

    else: #cadastrar?
        print('Opção inválida! Digite apenas "S" para Sim ou "N" para Não.')


# PROCESSAMENTO DAS ESTATÍSTICAS E EXIBIÇÃO
if len(partidas) > 0: #partidas?
    empates = 0
    total_gols = 0
    partida_mais_gols = partidas[0]  # startar c/a primeira partida

    print('\n' + '='*50)
    print('             RELATÓRIO GERAL DO TORNEIO             ')
    print('='*50)

    print(f'\nTotal de partidas cadastradas: {len(partidas)}')
    print('\n--- TODAS AS PARTIDAS ---')

    for p in partidas:
        gols_m = p['gols_mandante']
        gols_v = p['gols_visitante']
        total_jogo = gols_m + gols_v

        # jogo
        print(f"{p['mandante']} [{gols_m}] x [{gols_v}] {p['visitante']}")
        
        if gols_m == gols_v: #empate?
            empates += 1

        # acumulador p/media
        total_gols += total_jogo

        # partida com mais gols
        if total_jogo > (partida_mais_gols['gols_mandante'] + partida_mais_gols['gols_visitante']):
            partida_mais_gols = p

    # metricas
    media_gols = total_gols / len(partidas)

    print('\n--- ESTATÍSTICAS ---')
    print(f'Partidas empatadas: {empates}')
    print(f'Média de gols por partida: {media_gols:.2f}')
    
    gols_max = partida_mais_gols['gols_mandante'] + partida_mais_gols['gols_visitante']
    print(f'Partida com mais gols ({gols_max} gol(s)): '
          f"{partida_mais_gols['mandante']} [{partida_mais_gols['gols_mandante']}] x "
          f"[{partida_mais_gols['gols_visitante']}] {partida_mais_gols['visitante']}")

else: #partidas?
    print('\nNenhuma partida foi cadastrada no sistema.')