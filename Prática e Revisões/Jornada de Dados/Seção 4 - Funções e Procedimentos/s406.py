"""
    SECAO 4 - FUNÇÕES E PROCEDIMENTOS
    EXERCICIO 06
    AUTOR: WELLINGTON M. SANTOS
    DATA: 2026-10-05
"""

def converter_celsius_para_fahrenheit(celsius: float) -> float:
    """
    Recebe uma temperatura Celsius e retorna o valor convertido para Fahrenheit.

    Fórmula: fahrenheit = (celsius * 9 / 5) + 32

    Args:
        - celsius (float): temperatura em celsius
    Returns:
        - float: Temperatura convertida para escala Fahrenheit 
    """
    try:
        celsius_float = float(celsius)
        return (celsius_float * 9 / 5) + 32
    except (ValueError, TypeError):
        raise ValueError("Erro: O valor precisa ser um número válido. Ex.: 35.2 | 41 | -2")

if __name__ == '__main__':
    print('-'*50)
    for temp in [-23, -3, 0.0, 20, 41]:
        print(f'Celsius[{temp}°C] - Fahrenheit[{converter_celsius_para_fahrenheit(celsius=temp):.2f}]')
    print('-'*50)