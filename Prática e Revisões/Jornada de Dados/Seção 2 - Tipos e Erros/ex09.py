"""
    SECAO 2 - TIPOS E ERROS
    EXERCICIO 09
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-15
    OBJETIVO:
        - USO DE TRY/EXCEPT
"""

while True:
    entrada = input("Digite a nota: ")

    try:
        entrada = entrada.replace(",", ".")
        nota = float(entrada)

        if 0 <= nota <= 10:
            print(f"Nota registrada: {nota}")
            break
        else:
            print("A nota deve estar entre 0 e 10.")

    except ValueError:
        print("Valor inválido. Digite um número.")