""" ARCHIVO CONVERTIDOR DE BASE b2 -> b10, A LAS DEMAS BASES """
import os
import re
cls = lambda: os.system("cls")   # lambda sirve para crear funciones pequeñas y "anónimas", actúa como un "def"

def baseX_a_b10(numero_ingresado, base_origen):
    """ conversor de X base  a DECIMAL """
    posicion = 0
    decimal = 0
    negativo = False

    # Invertir la cadena porque debemos recorrerla de derecha a izquierda       

    if numero_ingresado < 0:
        negativo = True
        numero_ingresado *= -1   # si el num ingresado es negativo, lo convierte a positivo para poder operar

    numero_ingresado = str(numero_ingresado)[::-1]
    for digito in numero_ingresado:
        # Elevar X a la posición actual
        multiplicador = int(base_origen**posicion)
        decimal += int(digito) * multiplicador
        posicion += 1
    
    if negativo:
        return (decimal) * -1
    else:
        return decimal

def decimal_a_baseX(decimal_ingresado, base_a_convertir):    
        """ convertidor de base decimal a cualquier otra base """
        negativo = False
        
        if decimal_ingresado < 0:       
            negativo = True
            decimal_ingresado *= -1     # si el num ingresado es negativo, lo convierte a positivo para poder operar

        """ aqui almacenamos el resultado como cadena """
        cadena = ""

        """ mientras se pueda dividir... """
        while decimal_ingresado > 0:
            residuo = int(decimal_ingresado % base_a_convertir)    # el residuo es lo que se va almacenando (unos y ceros)
                        
            decimal_ingresado = int(decimal_ingresado / base_a_convertir)
            # va dividiendo el num ingresado para despues dividirlo y sacar el siguiente residuo
            cadena = str(residuo) + cadena
            resultado = int(cadena)

        if negativo:
            return (resultado) * -1
        else:
            return resultado


def decimal_a_hexa(decimal, base_a_convertir):
    """ funcion DECIMAL A HEXADECIMAL """
    equivalencias = {}
    negativo = False
    hex = ""

    # aca se crea el diccionario con los valores de ABC...
    for x in range(0, base_a_convertir - 10):
        #              
        equivalencias[ x + 10 ] = chr(ord('A') + x)

    if decimal < 0:
        negativo = True
        decimal *= -1
    
    while decimal > 0:
        residuo = decimal % base_a_convertir

        if residuo in equivalencias: 
            caracter_hex = equivalencias[residuo]
        else:
            caracter_hex = str(residuo)
        decimal = int(decimal / base_a_convertir)
        hex = caracter_hex + hex

    if negativo:
        return "-" + hex   # str  
    else:
        return hex

def hexa_a_decimal(caracteres, base_origen):
    """ variables
                < funcion hecha por Marcos Pereyra con algunos cambios mios > """

    negativo = False
    for x in re.finditer("-", caracteres):        # re.finditer (cadena o caracter a buscar, cadena en donde buscar)
        if x:                  
            negativo = True         # si en el FOR encuentra el caracter buscado retorna True y rompe el ciclo
            break


    if negativo:
        caracteres = caracteres.replace("-", "")  # si "negativo" = True  quita "-" pero sigue siendo str

    sumador = -1
    decimal = 0
    equivalencias = {}
    caracteres = caracteres.upper()

    """aca se crea el diccionario con los valores de ABC..."""
    for x in range(0, base_origen - 10):
        equivalencias[(chr(ord('A') + x))] = x + 10

    """este sumador es para elevar el 16^sumador, osea, la posicion en la que se encuentre"""
    for x in caracteres:
        sumador += 1

    """aca ocurre la magia :v, aca transforma de hexa a decimal uwu"""
    for x in caracteres:
        if x in equivalencias:
            decimal += equivalencias[x] * pow(base_origen, sumador)
            sumador -= 1

        elif x not in equivalencias:
            pass

        else:
            decimal += int(x) * pow(base_origen, sumador)
            sumador -= 1

    if negativo:
        return (decimal) * -1      # si "negativo" = True convierte en negativo a la variable, TERMINA EN ENTERO
    else:
        return decimal   # int


def string_a_entero(cadena):
    """ funcion para quitar el caracter "-" de una CADENA de numeros y retornarlo como entero """
    negativo = False
    for x in re.finditer("-", cadena):        # re.finditer (cadena o caracter a buscar, cadena en donde buscar)
        if x:                  
            negativo = True         # si en el FOR encuentra el caracter buscado retorna True y rompe el ciclo
            break

    if negativo:
        cadena = cadena.replace("-", "")
        cadena = int(cadena) * -1
        return cadena
    else:
        cadena = int(cadena)
        return cadena


"""
numero = "232"
base_origen = 16


print(string_a_entero(numero))  # (decimal, base_a_convertir)
print(type(string_a_entero(numero)))    """
