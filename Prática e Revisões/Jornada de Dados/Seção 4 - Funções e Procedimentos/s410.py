"""
SECAO: 4 - FUNÇÕES E PROCEDIMENTOS
EXERCICIO: 10
TEMA: SISTEMA DE APROVAÇÃO DE EMPRÉSTIMO
AUTOR: WELLINGTON M. SANTOS
DATA: 2026-10-09
"""

# 1. Comprometimento da renda
def calcular_comprometimento_renda(renda_mensal: float, valor_parcela: float) -> float:
    """
    Calcula o percentual da renda mensal comprometido pela parcela.

    Args:
        renda_mensal (float): valor da renda mensal.
        valor_parcela (float): valor da parcela do empréstimo.

    Returns:
        float: percentual da renda comprometida com o empréstimo.
    """
    return (valor_parcela / renda_mensal) * 100


# 2. Analisar empréstimo
def analisar_emprestimo(renda_mensal: float, valor_emprestimo: float, renda_comprometida: float) -> str:
    """
    Classifica a solicitação de empréstimo com base na renda e comprometimento.

    Args:
        renda_mensal (float): renda mensal do cliente.
        valor_emprestimo (float): valor total solicitado.
        renda_comprometida (float): percentual de comprometimento da renda.

    Returns:
        str: classificação ("Recusado", "Análise manual" ou "Aprovado").
    """
    if renda_comprometida > 40:
        return 'Recusado'
    elif valor_emprestimo > (renda_mensal * 5):
        return 'Análise manual'
    else:
        return 'Aprovado'


# 3. Total pagamento
def calcular_total_pagamento(valor_parcela: float, qtd_parcelas: int) -> float:
    """
    Calcula o valor total que será pago ao final do empréstimo.

    Args:
        valor_parcela (float): valor de cada parcela.
        qtd_parcelas (int): quantidade total de parcelas.

    Returns:
        float: valor total final a ser pago.
    """
    return valor_parcela * qtd_parcelas


# 4. Resultado
def exibir_resultado(
    valor_solicitado: float,
    percentual_comprometido: float,
    total_a_pagar: float,
    classificacao: str
) -> None:
    """
    Exibe o resumo da análise de empréstimo.

    Args:
        valor_solicitado (float): valor do empréstimo solicitado.
        percentual_comprometido (float): percentual comprometido da renda.
        total_a_pagar (float): valor total final a pagar.
        classificacao (str): resultado da análise.

    Returns:
        None
    """
    print("--- Análise do empréstimo ---")
    print(f"Valor solicitado: R$ {valor_solicitado:.2f}")
    print(f"Comprometimento da renda: {percentual_comprometido:.1f}%")
    print(f"Total a pagar: R$ {total_a_pagar:.2f}\n")
    print(f"Resultado: {classificacao}")


if __name__ == '__main__':
    renda_mensal = 1000.00
    valor_parcela = 100.00
    emprestimo_solicitado = 2000.00
    quantidade_parcelas = 24

    percentual_renda_comprometida = calcular_comprometimento_renda(
        renda_mensal=renda_mensal,
        valor_parcela=valor_parcela
    )
    
    classificacao = analisar_emprestimo(
        renda_mensal=renda_mensal,
        valor_emprestimo=emprestimo_solicitado,
        renda_comprometida=percentual_renda_comprometida
    )
    
    total_a_pagar = calcular_total_pagamento(
        valor_parcela=valor_parcela,
        qtd_parcelas=quantidade_parcelas
    )

    exibir_resultado(
        valor_solicitado=emprestimo_solicitado,
        percentual_comprometido=percentual_renda_comprometida,
        total_a_pagar=total_a_pagar,
        classificacao=classificacao
    )