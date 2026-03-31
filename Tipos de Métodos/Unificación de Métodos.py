# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:51:58 2026

@author: Alejandro
"""
#Versión 1.1.0
#Cambie el menu al principio y luego la función.
import math

# -------------------------
# Función evaluable
# -------------------------
def f(x):
    return eval(funcion, {
        "x": x,
        "exp": math.exp,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e
    })

# -------------------------
# MENÚ PRINCIPAL
# -------------------------
print("===== METODOS NUMERICOS =====")
print("1. Método de Bisección")
print("2. Método de Regla Falsa")

opcion = input("Seleccione el método: ")

# -------------------------
# DATOS
# -------------------------
funcion = input("\nIngresa la función en términos de x: ")
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
error_permitido = float(input("Ingresa el error permitido: "))

# -------------------------
# VALIDACIÓN
# -------------------------
if f(a) * f(b) >= 0:
    print("\nNo se puede aplicar el método en este intervalo.")
    print("f(a)*f(b) debe ser menor que 0.")
else:

    print("\nIteraciones:\n")
    print("i\t a\t\t b\t\t xr\t\t f(xr)\t\t Error")

    i = 1
    xr_anterior = a
    error = abs(b - a)

    while error > error_permitido:

        # BISECCIÓN
        if opcion == "1":
            xr = (a + b) / 2

        # REGLA FALSA
        elif opcion == "2":
            xr = b - (f(b) * (a - b)) / (f(a) - f(b))

        else:
            print("Opción inválida")
            break

        fxr = f(xr)

        if i > 1:
            error = abs((xr - xr_anterior) / xr)

        print(i, "\t", round(a,6), "\t", round(b,6), "\t", round(xr,6), "\t", round(fxr,6), "\t", round(error,6))

        # Actualizar intervalo
        if f(a) * fxr < 0:
            b = xr
        else:
            a = xr

        xr_anterior = xr
        i += 1

    print("\nRaíz aproximada:", round(xr,6))
    print("Error final:", error)



