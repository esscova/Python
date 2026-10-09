"""
    SECAO 4 - FUNÇÕES E PROCEDIMENTOS
    EXERCICIO 08
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-10-07
"""

def calcular_percentual_meta(meta: float, valor: float) -> float:
    """
    Função para calcular o valor percentual alcançado da meta.

    Exemplo: 
    
    ```python
    percentual = calcular_percentual_meta(10000.0, 7500.0)
    print(percentual)
    
    # Resultado: 75.0
    ```

    Args:
        - meta (float) : valor da meta
        - valor (float): valor vendido
    Returns:
        - float: valor percentual alcançado da meta.
    """
    try:
        meta_float = float(meta)
        valor_float = float(valor)

        if meta_float <= 0:
            raise ValueError("O valor da meta deve ser maior que zero.")

        return (valor_float / meta_float) * 100

    except (ValueError, TypeError) as e:
        raise ValueError(f"Erro nos parâmetros informados: {e}")


def exibir_status_meta(resultado: float) -> None:
    """
    Função para informar se a meta foi alcançada caso seja igual ou superior a 100%.

    Args:
        - resultado (float) : resultado da função `calcular_percentual_meta`.
    Returns:
        - None
    """
    if resultado >= 100: 
        print('Meta atingida!')
    else:
        print('Meta ainda não atingida.')


if __name__ == '__main__':
    percentual = calcular_percentual_meta(10000.0, 7500.0)
    print(f'Resultado: {percentual}')
    exibir_status_meta(percentual)