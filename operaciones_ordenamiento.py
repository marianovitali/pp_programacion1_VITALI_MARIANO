"""
Modulo de operaciones con ordenamiento
"""

def intercambiar_posicion(matriz: list, i: int, j: int) -> None:
    """
    Intercambia las posiciones de dos personajes en la matriz.

    Args:
        matriz (list): Matriz bidimensional que se utiliza para el intercambio.
        i (int): Índice de la primera posición a intercambiar.
        j (int): Índice de la segunda posición a intercambiar.

    Returns:
        None
    """

    # tupla unpacking en vez de variable temporal
    matriz[i], matriz[j] = matriz[j], matriz[i]

def obtener_columna(matriz: list, indice_columna: int) -> list:
    """
    Extrae una columna específica de la matriz y la retorna como lista.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
        indice_columna (int): Índice de la columna a extraer (0=nombre, 1=alias, 2=raza,
                            3=genero, 4=poder, 5=inteligencia, 6=velocidad).
    
    Returns:
        list: Lista que contiene todos los valores de la columna especificada,
            en el mismo orden que aparecen en la matriz original.
    """
    columna = []
    for personaje in matriz:
        columna.append(personaje[indice_columna])
    return columna

def trasponer_matriz(matriz: list) -> list:
    """
    Traspone la matriz convirtiendo filas en columnas y columnas en filas.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes, donde cada
                    sublista representa un personaje con estructura 
                    [nombre, alias, raza, genero, poder, inteligencia, velocidad].
    
    Returns:
        list: Matriz traspuesta donde cada fila contiene todos los valores de un atributo:
            - Fila 0: todos los nombres
            - Fila 1: todos los alias  
            - Fila 2: todas las razas
            - Fila 3: todos los géneros
            - Fila 4: todos los poderes
            - Fila 5: todas las inteligencias
            - Fila 6: todas las velocidades
    """

    matriz_traspuesta = []
    numero_columnas = len(matriz[0])

    for col in range(numero_columnas):
        nueva_fila = obtener_columna(matriz, col)
        matriz_traspuesta.append(nueva_fila)
    return matriz_traspuesta

def obtener_razas_unicas(matriz: list) -> list:
    """
    Obtiene una lista de todas las razas únicas presentes en la matriz de personajes.
    Utiliza un conjunto (set) para eliminar duplicados y luego convierte a lista
    para mantener solo valores únicos de razas.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    
    Returns:
        list: Lista con todas las razas únicas encontradas en la matriz, sin duplicados.
    """
    razas_unicas = []
    for personaje in matriz:
        raza = personaje[2]  # Indice 2 = raza
        if raza not in  razas_unicas:
            razas_unicas.append(raza)
    return razas_unicas

def filtrar_por_raza_exacta(matriz: list, raza_buscar: str) -> list:
    """
    Filtra personajes que tengan una raza que coincida exactamente con la especificada.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
        raza_buscar (str): Nombre exacto de la raza a filtrar.
    
    Returns:
        list: Lista de sublistas con los personajes que tienen exactamente la raza especificada.
    """
    personajes_filtrados = []
    for personaje in matriz:
        raza = personaje[2]  # Indice 2 = raza
        if raza == raza_buscar:
            personajes_filtrados.append(personaje)
    return personajes_filtrados

def ordenar_por_mas_poder(matriz: list) -> list:
    """
    Ordena la matriz por poder en orden descendente utilizando algoritmo Selection Sort.
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    
    Returns:
        list: Nueva matriz ordenada descendentemente por poder. La matriz original
            no se modifica.
    """
    matriz_ordenada = []
    for personaje in matriz:
        matriz_ordenada.append(personaje[:])

    # Selection Sort
    for i in range(len(matriz_ordenada) - 1):
        pos_max = encontrar_extremo(matriz_ordenada, i, 4, True)
        intercambiar_posicion(matriz_ordenada, i, pos_max)

    return matriz_ordenada

def agregar_grupo_a_matriz(matriz_destino: list, grupo: list) -> None:
    """
    Agrega todos los personajes de un grupo a la matriz destino.
    
    Args:
        matriz_destino (list): Matriz donde se agregarán los personajes.
        grupo (list): Lista de personajes (sublistas) que se agregarán a la matriz destino.
    
    Returns:
        None: Esta función modifica la matriz_destino directamente y no retorna ningún valor.
    """
    for personaje in grupo:
        matriz_destino.append(personaje)

def ordenar_personalizado(matriz: list) -> list:
    """
    Aplica un ordenamiento personalizado a la matriz de personajes.
    1. Por raza en orden alfabético ascendente
    2. Dentro de cada raza, por poder en orden descendente
    3. Mantiene estabilidad dentro de grupos con mismo poder
    
    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
    
    Returns:
        list: Nueva matriz ordenada según el criterio personalizado.
    """

    razas_unicas = obtener_razas_unicas(matriz)
    razas_ordenadas = sorted(razas_unicas)
    
    matriz_final = []
    for raza in razas_ordenadas:
        grupo_raza = filtrar_por_raza_exacta(matriz, raza)
        grupo_ordenado = ordenar_por_mas_poder(grupo_raza)
        agregar_grupo_a_matriz(matriz_final, grupo_ordenado)

    return matriz_final

def encontrar_extremo(matriz: list, inicio: int, indice_stat: int, buscar_maximo=True):
    """
    Encuentra el maximo o minimo en la matriz desde inicio.

    Args:
        matriz (list): Matriz bidimensional con los datos de los personajes.
        inicio (int): Indice desde donde comenzar a buscar.
        indice_stat (int): Indice del stat a comparar (4=poder, 5=inteligencia, 6=velocidad).
        buscar_maximo (bool): Si es True, busca el máximo y si es False, busca el mínimo.

    Returns:
        int: Indice del personaje con el maximo o minimo en el stat especificado.
    """

    pos_extremo = inicio
    for i in range(inicio + 1, len(matriz)):
        if buscar_maximo:
            if matriz[i][indice_stat] > matriz[pos_extremo][indice_stat]:
                pos_extremo = i
        else:
            if matriz[i][indice_stat] < matriz[pos_extremo][indice_stat]:
                pos_extremo = i

    return pos_extremo

def ordenar_por_stat(matriz: list, indice_stat: int, descendente=True, excluir_raza=None) -> list:
    """
    Ordena la matriz por un stat específico en orden ascendente o descendente

    Args:
        matriz (list): Matriz de personajes
        indice_stat (int): Índice del stat a ordenar (4=poder, 5=inteligencia, 6=velocidad).
        descendente (bool): True para DES, False para ASC
        excluir_raza (str, opcional): None para todos, "Human" para excluir humanos etc.
    Returns:
        list: Nueva matriz ordenada según el stat y criterio especificado.
    """

    matriz_ordenada = []
    for personaje in matriz:
        if excluir_raza is None or excluir_raza not in personaje[2]:
            matriz_ordenada.append(personaje[:])

    # Selection Sort
    for i in range(len(matriz_ordenada) - 1):
        pos_extremo = encontrar_extremo(matriz_ordenada, i, indice_stat, buscar_maximo=descendente)
        intercambiar_posicion(matriz_ordenada, i, pos_extremo)

    return matriz_ordenada