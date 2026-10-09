"""
SECAO 4 - FUNÇÕES E PROCEDIMENTOS
EXERCICIO 09
AUTOR: WELLINGTON M. SANTOS
DATA: 2026-10-08
"""

def calcular_tempo_estimado(distancia: float, velocidade: float) -> float:
    """
    Calcula o tempo estimado da entrega em horas.

    Args:
        distancia (float): Distância da entrega em quilômetros.
        velocidade (float): Velocidade média do veículo em km/h.

    Returns:
        float: Tempo estimado da entrega em horas.

    metrica:
        >>> calcular_tempo_estimado(10, 70)
        0.14285714285714285
    """
    return distancia / velocidade


def classificar_entrega(tempo: float) -> str:
    """
    Classifica a entrega com base no tempo estimado.

    - "Entrega rápida" se tempo <= 1
    - "Entrega normal" se 1 < tempo <= 3
    - "Entrega demorada" se tempo > 3

    Args:
        tempo (float): Tempo calculado pela função calcular_tempo_estimado.

    Returns:
        str: Classificação da entrega.
    """
    if tempo <= 1:
        return "Entrega rápida"
    elif tempo <= 3:
        return "Entrega normal"
    else:
        return "Entrega demorada"


def exibir_resumo_entrega(tempo_estimado: float, classificacao: str) -> None:
    """
    Exibe o resumo da entrega de forma legível (horas e minutos).

    Args:
        tempo_estimado (float): Tempo estimado em horas.
        classificacao (str): Classificação da entrega.

    Returns:
        None
    """
    horas = int(tempo_estimado)
    minutos = int(round((tempo_estimado - horas) * 60))

    if horas == 0:
        tempo_formatado = f"{minutos} minutos"
    elif minutos == 0:
        tempo_formatado = f"{horas} hora{'s' if horas > 1 else ''}"
    else:
        tempo_formatado = f"{horas}h {minutos}min"

    print(f"Tempo estimado: {tempo_formatado}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    distancias  = [10., 50., 120., 5., 200.]
    velocidades = [70., 40., 60., 80., 50.]

    print()
    for idx, metrica in enumerate(zip(distancias, velocidades), start=1):
        print('-'*50)
        print(f'Exemplo - {idx}\nDistância {metrica[0]} km - Velocidade {metrica[1]} km/h')
        tempo = calcular_tempo_estimado(distancia=metrica[0], velocidade=metrica[1])
        classificacao = classificar_entrega(tempo)
        exibir_resumo_entrega(tempo, classificacao)
    print('-'*50)