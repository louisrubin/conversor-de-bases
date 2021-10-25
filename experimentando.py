import Tkinter as tk
import ttk
import os

cls = lambda: os.system("cls")
cls()

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
