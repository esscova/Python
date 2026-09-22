"""
    SECAO 2 - TIPOS E ERROS
    EXERCICIO 08
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-09-15
    OBJETIVO:
        - USO DE TRY/EXCEPT
"""


idade = input("Informe sua idade: ")

try:
    idade = int(idade)
    print("Idade registrada com sucesso.")
except ValueError:
    print("Digite a idade utilizando apenas números.")