"""
    SECAO 4 - FUNÇÕES E PROCEDIMENTOS
    EXERCICIO 02
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-10-01
"""

def exibir_produto(nome:str, preco:float) -> None:
    """
    Função para exibir nome e preço de um produto.

    Args: 
        - nome:str    - nome do produto
        - preco:float - valor do produto
    Returns:
        - None
    """
    print(f'Produto: {nome} | Preço: R${preco:.2f}')

if __name__ == '__main__':
    exibir_produto(nome='Teclado',
                   preco=150.)