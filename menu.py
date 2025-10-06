"""
Manejo del menu del programa (imprimir, opciones, etc).
"""
import os

import utils

def limpiar_consola() -> None:
    """
    Limpia la pantalla de la consola utilizando el comando 'cls' del sistema operativo.
    
    Args:
        Ninguno
        
    Returns:
        None
    """
    os.system('cls')


def mostrar_menu_principal() -> None:
    """
    Muestra en pantalla el menú principal del programa con todas las opciones disponibles.
    Imprime un menú numerado del 1 al 22 con las diferentes funcionalidades del sistema.
    
    Args:
        Ninguno
        
    Returns:
        None
    """
    print("\n" + "="*60)
    print("Menu Principal")
    print("01. Crear Matriz")
    print("02. Agregar personaje")
    print("03. Mostrar cantidad de personajes")
    print("04. Mostrar cantidad de personajes Human")
    print("05. Mostrar cantidad de personajes que no sean Human")
    print("06. Mostrar detalle de todos los personajes")
    print("07. Mostrar Saiyan")
    print("08. Mostrar más poderoso")
    print("09. Mostrar más inteligente")
    print("10. Filtrar Menor velocidad")
    print("11. Filtrar Débiles")
    print("12. Filtrar No-Binario Veloces")
    print("13. Promedios Inteligencia")
    print("14. Filtrar Kryptonian")
    print("15. Filtrar Saiyan Power")
    print("16. Ordenar por Más Inteligente")
    print("17. Ordenar por Menos Inteligente [not Human]")
    print("18. Ordenar por Más Poder [not Human]")
    print("19. Ordenar por Más Velocidad")
    print("20. Ordenar personalizado")
    print("21. Trasponer Datos")
    print("22. Salir")
    print("="*60)

def pedir_opcion() -> int:
    """
    Pide una opcion al usuario para el menú principal.
    
    Args:
        Ninguno
        
    Returns:
        int: Número entero entre 1 y 22 que representa la opción seleccionada por el usuario.
    """
    mostrar_menu_principal()
    while True:
        try:
            opcion = int(input("Ingrese una opcion (1-22): "))
            if 1 <= opcion <= 22:
                limpiar_consola()
                return opcion
            else:
                print("Error: La opcion debe estar entre 1 y 22.")
                input("Presione Enter para continuar...")
        except ValueError:
            print("Error: Debe ingresar un numero valido.")
            input("Presione Enter para continuar...")


def mostrar_detalle_personajes(matriz: list, titulo: str = "DETALLE DE TODOS LOS PERSONAJES") -> None:
    """
    Muestra en pantalla el detalle completo de todos los personajes contenidos en la matriz.
    Presenta la información en formato de tabla con columnas para nombre, alias, raza, 
    género, inteligencia, poder y velocidad.
    
    Args:
        matriz (list): Lista de listas donde cada sublista representa un personaje con 
                    sus atributos [nombre, alias, raza, genero, poder, inteligencia, velocidad].
        titulo (str, opcional): Título a mostrar en la cabecera del reporte. 
                            Por defecto: "DETALLE DE TODOS LOS PERSONAJES".                             
    Returns:
        None:
    """
    print(titulo)

    print("\n" + "="*100)
    print(f"{'Nombre':<15} {'Alias':<15} {'Raza':<15} {'Genero':<12} {'Inteligencia':<12} {'Poder':<8} {'Velocidad':<10}")
    print("="*100)

    for personaje in matriz:
        nombre = personaje[0]
        alias = personaje[1][:15]
        raza = personaje[2]
        genero = personaje[3]
        poder = personaje[4]
        inteligencia = personaje[5]
        velocidad = personaje[6]

        print(f"{nombre:<15} {alias:<15} {raza:<15} {genero:<12} {inteligencia:<12} {poder:<8} {velocidad:<10}")

        print("="*100)
    input("Presione Enter para continuar...")
    limpiar_consola()

def mostrar_matriz_traspuesta(matriz_traspuesta: list) -> None:
    """
    Muestra en pantalla la matriz traspuesta de personajes de forma organizada.
    Presenta cada personaje numerado con todos sus atributos en formato vertical,
    facilitando la lectura de los datos transpuestos.
    
    Args:
        matriz_traspuesta (list): Lista de listas donde cada sublista contiene todos los valores
                                de un mismo atributo para todos los personajes. Estructura:
                                [nombres[], alias[], razas[], generos[], poderes[], velocidades[]].                                
    Returns:
        None:
    """
    numero_personajes = len(matriz_traspuesta[0])
    print("MATRIZ TRASPUESTA")
    for i in range(numero_personajes):
        print("="*100)
        print(f"Personaje {i + 1}:")
        print("="*100)
        print(f"    Nombre: {matriz_traspuesta[0][i]}")
        print(f"    Alias: {matriz_traspuesta[1][i]}")
        print(f"    Raza: {matriz_traspuesta[2][i]}")
        print(f"    Genero: {matriz_traspuesta[3][i]}")
        print(f"    Poder: {matriz_traspuesta[4][i]}")
        print(f"    Inteligencia: {matriz_traspuesta[5][i]}")
        print(f"    Velocidad: {matriz_traspuesta[6][i]}")
    print("="*100)
    input("Presione Enter para continuar...")
    limpiar_consola()

def pedir_datos_personaje() -> list:
    """
    Solicita al usuario todos los datos necesarios para crear un nuevo personaje.
    Utiliza funciones de validación para asegurar que los datos ingresados sean correctos.
    
    Args:
        Ninguno
        
    Returns:
        list: Lista con los datos del personaje en el siguiente orden:
            [nombre(str), alias(str), raza(str), genero(str), poder(int/float), 
            inteligencia(int/float), velocidad(int/float)].
    """
    nombre = utils.validar_texto("Ingrese el nombre del personaje: ")
    alias = utils.validar_texto("Ingrese el alias del personaje: ")
    raza = utils.validar_texto("Ingrese la raza del personaje: ")
    genero = utils.validar_texto("Ingrese el genero del personaje: ")
    poder = utils.validar_numero("Ingrese el poder del personaje: ")
    inteligencia = utils.validar_numero("Ingrese la inteligencia del personaje: ")
    velocidad = utils.validar_numero("Ingrese la velocidad del personaje: ")

    return [nombre, alias, raza, genero, poder, inteligencia, velocidad]