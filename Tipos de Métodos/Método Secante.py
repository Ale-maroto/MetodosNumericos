# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:13:53 2026

@author: Alejandro
"""

import sympy as sp

def metodo_secante():

    x = sp.symbols('x')

    print("METODO DE LA SECANTE\n")

    # Entrada de datos
    funcion = input("Ingrese f(x): ")
    x0 = float(input("Ingrese x0: "))
    x1 = float(input("Ingrese x1: "))
    error_max = float(input("Ingrese error permitido (%): "))

    # Convertir función
    f = sp.lambdify(x, sp.sympify(funcion))

    ea = 100
    iteracion = 1

    print("\nIter |    x_(i-1)   |    x_i     |    x_(i+1)   |    Ea %")
    print("-------------------------------------------------------------")

    while ea > error_max:

        f_x0 = f(x0)
        f_x1 = f(x1)

        # Verificar división entre cero
        if (f_x1 - f_x0) == 0:
            print("\nError: división entre cero. El método no se puede aplicar.")
            return

        # Fórmula de la secante
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)

        # Calcular error
        if iteracion > 1:
            ea = abs((x2 - x1) / x2) * 100

        print(f"{iteracion:4} | {x0:12.6f} | {x1:10.6f} | {x2:12.6f} | {ea:10.6f}")

        # Actualizar valores
        x0 = x1
        x1 = x2

        iteracion += 1

    print("\nRaiz aproximada:", x2)
    print("Error aproximado:", ea, "%")


# Ejecutar
metodo_secante()