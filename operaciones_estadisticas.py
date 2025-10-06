"""
Modulo de operaciones con estadisticas
"""
from typing import Optional, Tuple

from utn_fra.datasets import (
lista_nombre_heroes_pp, lista_alias_pp,
    lista_razas_pp, lista_generos_pp,
    lista_poderes_pp, lista_inteligencias_pp,
lista_velocidades_pp
)


def calcular_promedio(matriz: list, indice_stat: int, filtro_raza: Optional[str] = None) -> float:
    """
    Calcula el promedio de una estadística específica en la matriz de personajes.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
        indice_stat (int): Índice de la columna de la estadística a promediar:
                        4 = poder, 5 = inteligencia, 6 = velocidad.
        filtro_raza (str, opcional): Nombre o parte del nombre de la raza para filtrar. 
                        None calcula todas
    
    Returns:
        float: Promedio de la estadística especificada.
    """
    suma = 0
    cantidad = 0

    for personaje in matriz:
        raza = personaje[2]
        stat = personaje[indice_stat]

        if filtro_raza is None or filtro_raza in raza:
            suma += stat
            cantidad += 1

    if cantidad == 0:
        return 0

    promedio = suma / cantidad
    return promedio


def filtrar_menos_velocidad(matriz: list) -> Tuple[list, float]:
    """
    Filtra y retorna los personajes cuya velocidad es menor al promedio general de velocidad.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    
    Returns:
        tuple: Tupla que contiene:
            - list: Lista de listas con los personajes que tienen velocidad menor al promedio.
            - float: Valor del promedio de velocidad calculado para todos los personajes.
    """

    promedio = calcular_promedio(matriz, 6)  # Indice 6 = velocidad
    personajes_filtrados = []

    for personaje in matriz:
        velocidad = personaje[6]
        if velocidad < promedio:
            personajes_filtrados.append(personaje)

    return personajes_filtrados, promedio

def filtrar_debiles(matriz: list) -> Tuple[list, float]:
    """
    Filtra personajes cuyo poder sea inferior al poder mínimo encontrado entre los Saiyans.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    
    Returns:
        tuple: Tupla que contiene:
            - list: Lista de listas con los personajes que tienen poder menor al mínimo Saiyan.
            - int: Valor del poder mínimo encontrado entre los Saiyans.
    """

    poder_minimo_saiyan = None

    for personaje in matriz:
        raza = personaje[2]
        poder = personaje[4]

        if "Saiyan" in raza:
            if poder_minimo_saiyan is None or poder < poder_minimo_saiyan:
                poder_minimo_saiyan = poder

    if poder_minimo_saiyan is None:
        return [], 0  # No hay Saiyans en la matriz

    personajes_filtrados = []
    for personaje in matriz:
        if personaje[4] < poder_minimo_saiyan:
            personajes_filtrados.append(personaje)

    return personajes_filtrados, poder_minimo_saiyan


def calcular_promedio_android(matriz: list) -> Tuple[float, float]:
    """
    Calcula los promedios de inteligencia y poder específicamente para personajes de raza Android.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    
    Returns:
        tuple: Tupla que contiene:
            - float: Promedio de inteligencia de los personajes Android. Retorna 0 si no hay Androids.
            - float: Promedio de poder de los personajes Android. Retorna 0 si no hay Androids.
    """
    promedio_inteligencia = calcular_promedio(matriz, 5, filtro_raza="Android")  # Indice 5 = inteligencia
    promedio_poder = calcular_promedio(matriz, 4, filtro_raza="Android")  # Indice 4 = poder

    return promedio_inteligencia, promedio_poder

def filtrar_kryptonian_poder(matriz: list) -> Tuple[list, float]:
    """
    Filtra personajes NO Kryptonianos cuyo poder supere el promedio de poder de los Kryptonianos.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    
    Returns:
        tuple: Tupla que contiene:
            - list: Lista de sublistas con los personajes no Kryptonianos que superan 
                el promedio de poder Kryptoniano.
            - float: Promedio de poder calculado para los personajes Kryptonianos.
                    Retorna 0 si no hay Kryptonianos en la matriz.
    """
    promedio_poder_kryptonian = calcular_promedio(matriz, 4, filtro_raza="Kryptonian")  # Indice 4 = poder
    personajes_filtrados = []

    for personaje in matriz:
        raza = personaje[2]
        poder = personaje[4]

        if "Kryptonian" not in raza and poder > promedio_poder_kryptonian:
            personajes_filtrados.append(personaje)

    return personajes_filtrados, promedio_poder_kryptonian



def filtrar_saiyan_poder(matriz: list) -> Tuple[list, float]:
    """
    Filtra personajes NO Saiyans cuyo indice de ataque esté por debajo del índice promedio Saiyan.
    Calcula el "índice de ataque Saiyan" como el promedio de (poder + inteligencia + velocidad) / 3
    de todos los Saiyans, y luego encuentra personajes de otras razas con índice inferior.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    
    Returns:
        tuple: Tupla que contiene:
            - list: Lista de sublistas con los personajes no Saiyans que tienen un índice
                de ataque menor al índice promedio Saiyan.
            - float: Valor del índice de ataque promedio calculado para los Saiyans
                    (promedio de poder + inteligencia + velocidad).
    """

    promedio_poder_saiyan = calcular_promedio(matriz, 4, "Saiyan")  # Indice 4 = poder
    promedio_inteligencia_saiyan = calcular_promedio(matriz, 5, "Saiyan")  # Indice 5 = inteligencia
    promedio_velocidad_saiyan = calcular_promedio(matriz, 6, "Saiyan")  # Indice 6 = velocidad

    indice_ataque_saiyan = (promedio_poder_saiyan + promedio_inteligencia_saiyan + promedio_velocidad_saiyan) / 3

    personajes_filtrados = []

    for personaje in matriz:
        raza = personaje[2]
        poder = personaje[4]
        inteligencia = personaje[5]
        velocidad = personaje[6]

        if "Saiyan" not in raza:
            indice_personaje = (poder + inteligencia + velocidad) / 3
            if indice_personaje < indice_ataque_saiyan:
                personajes_filtrados.append(personaje)

    return personajes_filtrados, indice_ataque_saiyan


def filtrar_no_binario_veloces(matriz: list) -> Tuple[list, Optional[float]]:
    """
    Filtra personajes de género No-Binario que tengan la velocidad máxima entre todos los No-Binarios.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    Returns:
        tuple: Tupla que contiene:
            - list: Lista de sublistas con los personajes No-Binarios que tienen la velocidad máxima.
            - int/float: Valor de la velocidad máxima encontrada entre los personajes No-Binarios.
                        None si no hay personajes No-Binarios en la matriz.
    """
    max_velocidad = None
    for personaje in matriz:
        if personaje[3] == "No-Binario":  # Indice 3 = genero
            velocidad = personaje[6]  # Indice 6 = velocidad
            if max_velocidad is None or velocidad > max_velocidad:
                max_velocidad = velocidad

    if max_velocidad is None:
        return []  # No hay personajes de genero no-Binario
    
    personajes_filtrados = []
    for personaje in matriz:
        if personaje[3] == "No-Binario" and personaje[6] == max_velocidad:
            personajes_filtrados.append(personaje)

    return personajes_filtrados, max_velocidad