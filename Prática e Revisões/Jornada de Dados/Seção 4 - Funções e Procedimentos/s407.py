"""
    SECAO 4 - FUNÇÕES E PROCEDIMENTOS
    EXERCICIO 07
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-10-05
"""

def calcular_consumo_medio(dist: float, litros: float) -> float:
    """
    Função para calcular quantos quilômetros o veículo percorreu por litro.

    Args:
        - dist (float): distância percorrida em quilômetros.
        - litros (float): quantidade de litros utilizados.

    Returns:
        - float: consumo médio em km/l.
    """
    try:
        if litros <= 0:
            raise ValueError("A quantidade de litros deve ser maior que zero.")
        if dist < 0:
            raise ValueError("A distância não pode ser negativa.")
            
        return dist / litros
    except TypeError:
        raise TypeError("Os valores de distância e litros devem ser numéricos.")

def exibir_consumo(consumo: float) -> None:
    """
    Função para exibir a mensagem formatada de consumo ao usuário.

    Args:
        - consumo (float): resultado obtido da função `calcular_consumo_medio`.

    Returns:
        - None
    """
    print(f'Consumo médio: {consumo} km/l')

if __name__ == '__main__':
    resultado = calcular_consumo_medio(420.0, 35.0)
    exibir_consumo(resultado)