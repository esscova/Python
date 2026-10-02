"""
    SECAO 4 - FUNÇÕES E PROCEDIMENTOS
    EXERCICIO 05
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-10-02
"""

# FUNÇÕES
def calcular_valor_final(preco:float, quantidade:int, desconto:float) -> float:
    """
    Função para calcular o valor final de um pedido após o desconto.

    Args:
        - preco(float)   : preço unitário
        - quantidade(int): quantidade
        - desconto(float): desconto à aplicar em formato decimal. Ex.: 0.10 representa 10% de desconto.
    
    Returns:
        - total(float): valor final do pedido após o desconto.
    """
    subtotal         = preco * quantidade
    total = (1 - desconto) * subtotal
    return total

def exibir_resumo_pedido(pedido:str, valor:float) -> None:
    """
    Exibe uma mensagem sobre um pedido.

    Args:
        - pedido(str) : o número do pedido
        - valor(float): valor final do pedido
    
    Returns:
        - None
    """
    if pedido:pedido = pedido.strip()
    print(f'Pedido #{pedido} finalizado. Total: R${valor:.2f}')

if __name__ == '__main__':
    exibir_resumo_pedido(pedido='1234',
                         valor=calcular_valor_final(
                             preco=100.,
                             quantidade=1,
                             desconto=.1
                         ))