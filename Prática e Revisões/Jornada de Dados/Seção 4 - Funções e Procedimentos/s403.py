"""
    SECAO 4 - FUNÇÕES E PROCEDIMENTOS
    EXERCICIO 03
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-10-01
"""

def calcular_total(preco:float, quantidade:int) -> float:
    """
    Função que calcula o valor total de uma compra.

    Args:
        - preco(float)     : valor de um produto
        - quantidade (int) : quantidade de itens
    
    Returns:
        - total (float): valor total da compra. (preço X quantidade)
    """
    total = preco * quantidade
    return total

if __name__ == '__main__':
    total = calcular_total(preco=50.
                           ,quantidade=3)
    print(total)