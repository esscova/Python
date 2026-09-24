"""
    SECAO 3 - ESTRUTURAS DE DADOS
    EXERCICIO 01
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-22
    OBJETIVO:
        - PRATICAR ESTRUTURAS DE DADOS
        - INTEGRAR FLUXO DE CONTROLE EM ESTRUTURAS
"""
data = []

while True:
    fig = input('Nome da figurinha (ou "fim" para encerrar): ').strip()
    
    if fig.lower() == 'fim':
        break
    
    if fig:
        data.append(fig)
        print('Figurinha cadastrada!')
    else:
        print('Digite um nome válido para a figurinha.')

print('\n--- RELATÓRIO FINAL ---')
if data:
    print(f'Figurinhas: {data}')
    print(f'Total: {len(data)}')
    print(f'Primeira: {data[0]}')
    print(f'Última: {data[-1]}')
else:
    print('Nenhuma figurinha cadastrada.')