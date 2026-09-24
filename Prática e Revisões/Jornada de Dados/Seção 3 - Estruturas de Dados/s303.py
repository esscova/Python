"""
    SECAO 3 - ESTRUTURAS DE DADOS
    EXERCICIO 03
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-24
    OBJETIVO:
        - PRATICAR ESTRUTURAS DE DADOS
"""

selecoes = set()

print("Digite o nome de 8 seleções:")
for i in range(8):
    time = input(f"Seleção {i+1}: ").strip().title()
    selecoes.add(time)

print('\n=== SELEÇÕES CLASSIFICADAS ===')
for time in selecoes:
    print(f"- {time}")

print(f'\nTotal de seleções diferentes cadastradas: {len(selecoes)}')

print('\n=== CONSULTAR SELEÇÃO ===')
busca = input('Consulte a seleção: ').strip().title()

if busca in selecoes:
    print(f'A seleção "{busca}" ESTÁ classificada!')
else:
    print(f'A seleção "{busca}" NÃO foi encontrada / não está classificada.')