"""
Modulo para ooperaciones con datos y matriz
"""
import utils
from utn_fra.datasets import (
lista_nombre_heroes_pp, lista_alias_pp,
    lista_razas_pp, lista_generos_pp,
    lista_poderes_pp, lista_inteligencias_pp,
lista_velocidades_pp
)


def crear_matriz(lista_nombre: list, lista_alias: list, lista_razas: list,
                lista_generos: list, lista_poderes: list, lista_inteligencias: list,
                lista_velocidades: list) -> list:
    """
    Crea una matriz bidimensional con los datos de los personajes organizados por filas.
    Cada fila representa un personaje y cada columna representa un atributo específico.
    
    Args:
        lista_nombre (list): Lista con los nombres de los personajes.
        lista_alias (list): Lista con los alias/apodos de los personajes.
        lista_razas (list): Lista con las razas de los personajes.
        lista_generos (list): Lista con los géneros de los personajes.
        lista_poderes (list): Lista con los valores de poder de los personajes (numérico).
        lista_inteligencias (list): Lista con los valores de inteligencia de los personajes (numérico).
        lista_velocidades (list): Lista con los valores de velocidad de los personajes (numérico).
        
    Returns:
        list: Matriz bidimensional donde cada sublista representa un personaje con estructura:
            [nombre, alias, raza, genero, poder, inteligencia, velocidad].
    """

    matriz = []

    for i in range(len(lista_nombre)):
        fila = [
            lista_nombre[i],
            lista_alias[i],
            lista_razas[i],
            lista_generos[i],
            lista_poderes[i],
            lista_inteligencias[i],
            lista_velocidades[i]
        ]
        matriz.append(fila)

    return matriz

def mostrar_cantidad_personajes(cantidad: int) -> None:
    """
    Muestra en pantalla la cantidad total de personajes cargados en el sistema.

    
    Args:
        cantidad (int): Número entero que representa la cantidad de personajes a mostrar.
        
    Returns:
        None:
    """
    print(f"Cantidad de personajes: {cantidad}")
    input("Presione Enter para continuar...")


def filtrar_personajes_raza(matriz: list, tipo_raza: str) -> list:
    """
    Filtra y retorna todos los personajes que pertenecen a una raza específica.

    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes, donde cada
                    sublista tiene la estructura [nombre, alias, raza, genero, poder, inteligencia, velocidad].
        tipo_raza (str): Nombre o parte del nombre de la raza a filtrar (ej: "Human", "Saiyan").
        
    Returns:
        list: Lista de sublistas con los personajes que coinciden con la raza especificada.
            Cada elemento mantiene la estructura original [nombre, alias, raza, genero, poder, inteligencia, velocidad].
    """

    personajes_filtrados = []

    for personaje in matriz:
        raza = personaje[2]

        if f"{tipo_raza} " in f" {raza} ":
            personajes_filtrados.append(personaje)

    return personajes_filtrados

def encontrar_personajes_mas_poderosos(matriz: list) -> list:
    """
    Encuentra y retorna todos los personajes que tienen el valor máximo de poder.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.

        
    Returns:
        list: Lista de sublistas con todos los personajes que tienen el poder máximo.

    """

    max_poder = matriz[0][4] # Poder del primer pj.
    personajes_mas_poderosos = [matriz[0]] # primer pj

    for personaje in matriz[1:]:
        poder_actual = personaje[4]

        if poder_actual > max_poder:
            max_poder = poder_actual
            personajes_mas_poderosos = [personaje]

        elif poder_actual == max_poder:
            personajes_mas_poderosos.append(personaje)
    
    return personajes_mas_poderosos

def encontrar_personajes_mas_inteligente(matriz: list) -> list:
    """
    Encuentra y retorna todos los personajes que tienen el valor máximo de inteligencia.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
        
    Returns:
        list: Lista de sublistas con todos los personajes que tienen la inteligencia máxima.
    """

    max_inteligencia = matriz[0][5] # Inteligencia del primer pj.
    personajes_mas_inteligentes = [matriz[0]] # primer pj

    for personaje in matriz[1:]:
        inteligencia_actual = personaje[5]

        if inteligencia_actual > max_inteligencia:
            max_inteligencia = inteligencia_actual
            personajes_mas_inteligentes = [personaje]

        elif inteligencia_actual == max_inteligencia:
            personajes_mas_inteligentes.append(personaje)

    return personajes_mas_inteligentes

def agregar_personaje(matriz: list, nuevo_personaje: list) -> list:
    """
    Agrega un nuevo personaje a la matriz existente sin modificar la matriz original.
    
    Args:
        matriz (list): Matriz bidimensional existente con los datos de los personajes.
        nuevo_personaje (list): Lista con los datos del nuevo personaje a agregar.
        
    Returns:
        list: Nueva matriz que incluye todos los personajes originales más el nuevo personaje.
    """
    matrix_auxiliar = []
    for personaje in matriz:
        matrix_auxiliar.append(personaje[:])
    matrix_auxiliar.append(nuevo_personaje)
    return matrix_auxiliar