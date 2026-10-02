"""
    SECAO 4 - FUNÇÕES E PROCEDIMENTOS
    EXERCICIO 04
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-10-02
"""

def calcular_media_avaliacoes(n1:float, n2:float, n3:float) -> float:
    """
    Função para calcular a média aritmética de três avaliações de um produto.

    Args:
        - n1: float - primeira nota
        - n2: float - segunda nota
        - n3: float - terceira nota
    Returns:
        - float: media aritmética (n1 + n2 + n3)/3
    """
    total = n1 + n2 + n3
    media = total/3
    return media

if __name__ == '__main__':
    nota1 = 4
    nota2 = 4
    nota3 = 5

    nota_media = calcular_media_avaliacoes(n1=nota1,
                                           n2=nota2,
                                           n3=nota3)
    print(f'Nota média para o produto: {nota_media:.2f}')