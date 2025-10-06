"""
Funciones de utilidad para validacion y verificacion de datos."""
def verificar_matriz_vacia(matriz: list, nombre_operacion: str = "operacion") -> bool:
    """
    Verifica si una matriz está vacía y muestra un mensaje de error personalizado si es así.
    
    Args:
        matriz (list): Lista que representa la matriz a verificar. Puede estar vacía o contener datos.
        nombre_operacion (str, opcional): Nombre descriptivo de la operación que se intentaba realizar.
    
    Returns:
        bool: True si la matriz está vacía (indicando que hay un error), 
            False si la matriz contiene datos (puede continuar la operación).
    """
    if not matriz:
        print(f"Error: No se puede realizar la {nombre_operacion} porque la matriz esta vacia.")
        input("Presione Enter para continuar...")
        return True
    return False

def validar_texto(mensaje: str) -> str:
    """
    Solicita y valida la entrada de texto del usuario asegurando que no esté vacío y no contenga números.

    
    Args:
        mensaje (str): Mensaje que se mostrará al usuario para solicitar la entrada de texto.
    
    Returns:
        str: Texto válido ingresado por el usuario que cumple con los criterios.
    """
    
    texto = input(mensaje)

    if texto ==  "":
        print("Error: El texto no puede estar vacio.")
        return validar_texto(mensaje)
    
    for caracter in texto:
        if caracter.isdigit():
            print("Error: El texto no puede contener numeros.")
            return validar_texto(mensaje)
    return texto
        
def validar_numero(mensaje: str) -> int:
    """
    Solicita y valida la entrada de un número entero positivo del usuario.
    
    Args:
        mensaje (str): Mensaje que se mostrará al usuario para solicitar la entrada numérica.

    
    Returns:
        int: Número entero positivo (mayor o igual a 0) validado ingresado por el usuario.
    """
    
    try:
        numero = int(input(mensaje))
        if numero < 0:
            print("Error: El numero debe ser positivo.")
            return validar_numero(mensaje)
        return numero
    except ValueError:
        print("Error: Debe ingresar un numero valido.")
        return validar_numero(mensaje)
    
def validar_personaje_completo(personaje: list) -> bool:
    """
    Valida que un personaje tenga todos los datos requeridos y estén completos.
    Args:
        personaje (list): Lista con los datos del personaje a validar.
    
    Returns:
        bool: True si el personaje tiene exactamente 7 datos y todos están completos (no vacíos ni None).
            False si falta algún dato, hay datos de más, o algún campo está vacío/None.

    """
    if len(personaje) != 7:
        print("Error: El personaje debe tener 7 datos (nombre, alias, raza, genero, poder, inteligencia, velocidad).")
        return False
    for dato in personaje:
        if dato is None or dato == "":
            print("Error: Todos los datos del personaje deben estar completos.")
            return False
    return True