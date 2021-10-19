from conversiones_main import *
cls()
print(" _____________________________")
print("[____________MENU_____________]\n")

numero = input(" Ingrese numero: ")
base_origen = int(input(" Base de origen: b"))
base_a_convertir = int(input(" Base a convertir: b"))
print()

if base_origen == base_a_convertir:
    print (" [",numero,"] EN BASE ", base_origen, " =  [",numero,"] EN BASE ",base_a_convertir)


elif base_a_convertir == 10:

    if base_origen >= 11 and base_origen <= 16:   # si el num ingr. está entre 11 y 16, usa "hexa_a_decimal()"
        decimal = hexa_a_decimal(numero, base_origen)
    else:
        entero = string_a_entero(numero)
        decimal = baseX_a_b10(entero, base_origen)

    numero = numero.upper()
    print (" [",numero,"] EN BASE ", base_origen, " =  [",decimal,"] EN BASE ",base_a_convertir)


elif base_a_convertir >= 11 and base_a_convertir <= 16:

    if base_origen <= 10:
        entero = string_a_entero(numero)
        decimal = baseX_a_b10(entero, base_origen)
        hexa = decimal_a_hexa(decimal, base_a_convertir)
    else:
        decimal = hexa_a_decimal(numero, base_origen)
        hexa = decimal_a_hexa(decimal, base_a_convertir)

    numero = numero.upper()   # UPPERCASE
    print (" [",numero,"] EN BASE ", base_origen, " =  [",hexa,"] EN BASE ",base_a_convertir)

elif base_a_convertir > 1 and base_a_convertir < 10:

    if base_origen >= 11:
        decimal = hexa_a_decimal(numero, base_origen)
        convertido = decimal_a_baseX(decimal, base_a_convertir)
    else:
        entero = string_a_entero(numero)
        decimal = baseX_a_b10(entero, base_origen)
        convertido = decimal_a_baseX(decimal, base_a_convertir)
    numero = numero.upper()
    print (" [",numero,"] EN BASE ", base_origen, " =  [",convertido,"] EN BASE ",base_a_convertir)

else: 
    print(" - 'ERROR 404 - 087' -\n")








