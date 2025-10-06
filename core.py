"""
Modulo principal del programa.
"""

from utn_fra.datasets import (
lista_nombre_heroes_pp, lista_alias_pp,
    lista_razas_pp, lista_generos_pp,
    lista_poderes_pp, lista_inteligencias_pp,
lista_velocidades_pp
)

import menu
import operaciones_datos
import operaciones_estadisticas
import operaciones_ordenamiento
import utils

def ejecutar_programa() -> None:
    """
    Función principal que ejecuta el programa de análisis de datos de superhéroes y villanos.
    
    Args:
        Ninguno
        
    Returns:
        None
    """
    matriz = []

    print("¡Bienvenido a la aplicacion de analisis de datos de superheroes y villanos!")
    input("Presione Enter para continuar...")

    while True:
        opcion = menu.pedir_opcion()
        match opcion:
            case 1:
                matriz = operaciones_datos.crear_matriz(
                    lista_nombre_heroes_pp, lista_alias_pp,
                    lista_razas_pp, lista_generos_pp,
                    lista_poderes_pp, lista_inteligencias_pp,
                    lista_velocidades_pp
                )
                print(f"Matriz cargada con {len(matriz)} personajes.\n")
                input("Presione Enter para continuar...")
            case 2:
                if utils.verificar_matriz_vacia(matriz, "agregar personaje"):   
                    continue
                nuevo_personaje = menu.pedir_datos_personaje()
                if utils.validar_personaje_completo(nuevo_personaje):
                    matriz = operaciones_datos.agregar_personaje(matriz, nuevo_personaje)
                    print(f"Personaje {nuevo_personaje[0]} agregado exitosamente.")
                else:
                    print("No se pudo agregar el personaje. Datos incompletos.")
                input("Presione Enter para continuar...")
            case 3:
                cantidad = operaciones_datos.mostrar_cantidad_personajes(len(matriz))
            case 4:
                personajes_human = operaciones_datos.filtrar_personajes_raza(matriz, "Human")
                print(f"Cantidad de personajes Human: {len(personajes_human)}")
                input("Presione Enter para continuar...")
            case 5:
                personajes_human = operaciones_datos.filtrar_personajes_raza(matriz, "Human")
                cantidad_no_human = len(matriz) - len(personajes_human)
                print(f"Cantidad de personajes que no son Human: {cantidad_no_human}")
                input("Presione Enter para continuar...")
            case 6:
                menu.mostrar_detalle_personajes(matriz)
            case 7:
                saiyans = operaciones_datos.filtrar_personajes_raza(matriz, "Saiyan")
                menu.mostrar_detalle_personajes(saiyans, "PERSONAJES DE RAZA SAIYAN")
            case 8:
                if utils.verificar_matriz_vacia(matriz, "encontrar personajes mas poderosos"):
                    continue
                mas_poderosos = operaciones_datos.encontrar_personajes_mas_poderosos(matriz)
                menu.mostrar_detalle_personajes(mas_poderosos, "PERSONAJES MAS PODEROSOS")
            case 9:
                if utils.verificar_matriz_vacia(matriz, "encontrar personajes mas inteligentes"):
                    continue
                mas_inteligentes = operaciones_datos.encontrar_personajes_mas_inteligente(matriz)
                menu.mostrar_detalle_personajes(mas_inteligentes, "PERSONAJES MAS INTELIGENTES")
            case 10:
                if utils.verificar_matriz_vacia(matriz, "filtrar por velocidad"):
                    continue
                personajes_filtrados, promedio = operaciones_estadisticas.filtrar_menos_velocidad(matriz)
                print(f"Promedio de Velocidad: {promedio:.2f}")
                menu.mostrar_detalle_personajes(personajes_filtrados, "PERSONAJES CON VELOCIDAD MENOR AL PROMEDIO")
            case 11:
                if utils.verificar_matriz_vacia(matriz, "filtrar personajes debiles"):
                    continue
                personajes, poder_min_saiyan = operaciones_estadisticas.filtrar_debiles(matriz)
                print(f"Poder minimo entre Saiyan: {poder_min_saiyan}")
                menu.mostrar_detalle_personajes(personajes, "PERSONAJES MAS DEBILES QUE LOS SAIYAN")
            case 12:
                if utils.verificar_matriz_vacia(matriz, "filtrar no-binario veloces"):
                    continue
                personajes, max_velocidad = operaciones_estadisticas.filtrar_no_binario_veloces(matriz)
                print(f"Maxima Velocidad No-Binario: {max_velocidad:.2f}")
                menu.mostrar_detalle_personajes(personajes, "PERSONAJES NO-BINARIO CON VELOCIDAD MAXIMA")
            case 13:
                if utils.verificar_matriz_vacia(matriz, "calcular promedios de inteligencia"):
                    continue
                promedio_inteligencia, promedio_poder = operaciones_estadisticas.calcular_promedio_android(matriz)
                print(f"Promedio de Inteligencia de Android: {promedio_inteligencia:.2f}")
                print(f"Promedio de Poder de Android: {promedio_poder:.2f}")
                input("Presione Enter para continuar...")
            case 14:
                if utils.verificar_matriz_vacia(matriz, "filtrar personajes Kryptonian"):
                    continue
                personajes, promedio_poder_kryptonian = operaciones_estadisticas.filtrar_kryptonian_poder(matriz)
                print(f"Promedio de Poder de Kryptonian: {promedio_poder_kryptonian:.2f}")
                menu.mostrar_detalle_personajes(personajes, "PERSONAJES NO KRYPTONIAN CON PODER SUPERIOR AL PROMEDIO DE KRYPTONIAN")
            case 15:
                if utils.verificar_matriz_vacia(matriz, "filtrar personajes Saiyan Power"):
                    continue
                personajes, poder_minimo_saiyan = operaciones_estadisticas.filtrar_saiyan_poder(matriz)
                print(f"Indice de Ataque Saiyan: {poder_minimo_saiyan:.2f}")
                menu.mostrar_detalle_personajes(personajes, "PERSONAJES NO SAIYAN CON STATS POR DEBAJO DEL INDICE DE ATAQUE SAIYAN")
            case 16:
                if utils.verificar_matriz_vacia(matriz, "ordenar personajes por inteligencia"):
                    continue
                matriz_ordenada = operaciones_ordenamiento.ordenar_por_stat(matriz, 5, descendente=True)
                menu.mostrar_detalle_personajes(matriz_ordenada, "PERSONAJES ORDENADOS POR MAS INTELIGENTE (DESCENDENTE)")
            case 17:
                if utils.verificar_matriz_vacia(matriz, "ordenar personajes por menos inteligencia"):
                    continue
                matriz_ordenada = operaciones_ordenamiento.ordenar_por_stat(matriz, 5, descendente=False, excluir_raza="Human")
                menu.mostrar_detalle_personajes(matriz_ordenada, "PERSONAJES (MENOS HUMAN) ORDENADOS POR MENOS INTELIGENTE (ASCENDENTE)")
            case 18:
                if utils.verificar_matriz_vacia(matriz, "ordenar personajes por poder"):
                    continue
                matriz_ordenada = operaciones_ordenamiento.ordenar_por_stat(matriz, 4, descendente=True, excluir_raza="Human")
                menu.mostrar_detalle_personajes(matriz_ordenada, "PERSONAJES (MENOS HUMAN) ORDENADOS POR MAS PODER (DESCENDENTE)")
            case 19:
                if utils.verificar_matriz_vacia(matriz, "ordenar personajes por velocidad"):
                    continue
                matriz_ordenada = operaciones_ordenamiento.ordenar_por_stat(matriz, 6, descendente=True)
                menu.mostrar_detalle_personajes(matriz_ordenada, "PERSONAJES ORDENADOS POR MAS VELOCIDAD (DESCENDENTE)")
            case 20:
                if utils.verificar_matriz_vacia(matriz, "ordenar personajes por criterio personalizado"):
                    continue
                matriz_ordenada = operaciones_ordenamiento.ordenar_personalizado(matriz)
                menu.mostrar_detalle_personajes(matriz_ordenada, "PERSONAJES ORDENADOS ALFABETICAMENTE POR RAZA (PODER DESCENDENTE)")
            case 21:
                if utils.verificar_matriz_vacia(matriz, "trasponer datos"):
                    continue
                matriz_traspuesta = operaciones_ordenamiento.trasponer_matriz(matriz)
                menu.mostrar_matriz_traspuesta(matriz_traspuesta)
            case 22:
                print("¡Hasta luego!")
                break



