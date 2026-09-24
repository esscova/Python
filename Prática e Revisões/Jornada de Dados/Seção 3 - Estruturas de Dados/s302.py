"""
    SECAO 3 - ESTRUTURAS DE DADOS
    EXERCICIO 02
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-24
    OBJETIVO:
        - PRATICAR ESTRUTURAS DE DADOS
"""

estatisticas = {}

mandante = input('Seleção mandante: ').strip()
estatisticas['mandante'] = mandante

visitante = input('Seleção visitante: ').strip()
estatisticas['visitante'] = visitante

try:
    gols_mandante = int(input('Gols do mandante: ').strip())
    gols_visitante = int(input('Gols do visitante: ').strip())
except ValueError:
    print('Erro: A quantidade de gols deve ser um número inteiro válido.')
    exit()

estatisticas['gols_mandante'] = gols_mandante
estatisticas['gols_visitante'] = gols_visitante

print('\n== INFORMAÇÕES ARMAZENADAS ===')
for k,v in estatisticas.items():
    print(f'{k.replace('_', ' ').capitalize()}: {v}')

print('\n== RESULTADO ===')
if estatisticas['gols_mandante'] > estatisticas['gols_visitante']:
    print('A seleção mandante ganhou.')
elif estatisticas['gols_mandante'] < estatisticas['gols_visitante']:
    print('A seleção visitante ganhou.')
else:
    print('A partida terminou empatada.')