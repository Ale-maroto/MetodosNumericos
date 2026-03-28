# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:23:12 2026

@author: Alejandro
"""

import math

# Ingresar la función
funcion = input("Ingresa la función en términos de x: ")

# Crear función evaluable
def f(x):
    return eval(funcion)

# Intervalo
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))

# Error permitido
error_permitido = float(input("Ingresa el error permitido: "))

# Verificar condición del método
if f(a) * f(b) >= 0:
    print("\nNo se puede aplicar el método de bisección en este intervalo.")
    print("f(a)*f(b) debe ser menor que 0.")
else:
    
    print("\nIteraciones del método de bisección:\n")
    print("i\t a\t\t b\t\t p\t\t f(p)\t\t Error")

    i = 1
    error = abs(b - a)

    while error > error_permitido:
        
        p = (a + b) / 2
        fp = f(p)

        print(i, "\t", round(a,6), "\t", round(b,6), "\t", round(p,6), "\t", round(fp,6), "\t", round(error,6))

        if f(a) * fp < 0:
            b = p
        else:
            a = p

        error = abs(b - a)
        i += 1

    print("\nRaíz aproximada:", round(p,6))
    print("Error final:", error)