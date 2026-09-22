"""
    SECAO 2 - TIPOS E ERROS
    EXERCICIO 10
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-15
    OBJETIVO:
        - TRATAMENTO DE ERROS 
        - USO DE LOOPS E VALIDAÇÕES 
"""

while True:
    entrada = input("Quantos gols a seleção marcou? ")

    try:
        gols = int(entrada)

        if gols >= 0:
            print(f"Quantidade de gosl registrada: {gols}")
            break
        else:
            print("A quantidade de gols não pode ser negativa.")

    except ValueError:
        print("Entrada inválida")