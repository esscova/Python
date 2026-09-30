"""
    SECAO 3 - ESTRUTURAS DE DADOS
    EXERCICIO 05
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-25
    OBJETIVO:
        - PRATICAR ESTRUTURAS DE DADOS
        - OPERAÇÕES COM ESTRUTURAS DE DADOS
        - UNIR FLUXOS DE CONTROLE E REPETIÇÃO COM ESTRUTURAS DE DADOS
"""

jogadores = []

while True:
    try:
        quantidade = int(input('Informe a quantidade de jogadores: ').strip())
        if quantidade > 0:
            break
        print('Por favor, digite um número maior que zero.')
    except ValueError:
        print('Erro: o valor deve ser numérico inteiro.')

for i in range(quantidade):
    jogador = {}
    print(f'\n=== CADASTRO DO JOGADOR {i+1} ===')
    jogador['nome'] = input('Nome: ').strip().title()
    jogador['seleção'] = input('Seleção: ').strip().title()
    
    while True:
        try:
            jogador['gols'] = int(input('Quantidade de gols: ').strip())
            break
        except ValueError:
            print('Erro: O valor deve ser um número inteiro válido.')
            
    jogadores.append(jogador)

# report
artilheiro = max(jogadores, key=lambda j: j['gols'])
total_gols = sum(j['gols'] for j in jogadores)
media_gols = total_gols / len(jogadores)

print('\n' + '='*40)
print('          RELATÓRIO DA ARTILHARIA          ')
print('='*40)

print('\nJogadores Cadastrados:')
for j in jogadores:
    print(f"- {j['nome']} ({j['seleção']}): {j['gols']} gol(s)")

print(f"\nArtilheiro: {artilheiro['nome']} ({artilheiro['seleção']}) com {artilheiro['gols']} gol(s).")
print(f"Média de gols do torneio: {media_gols:.2f} gols por jogador.")