# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:06:13 2026

@author: Alejandro
"""
# Versión 1.0.0

import sympy as sp

def punto_fijo():

    x = sp.symbols('x')

    print("METODO DE PUNTO FIJO\n")

    # Entrada de datos
    funcion = input("Ingrese f(x) = 0: ")
    x0 = float(input("Ingrese valor inicial x0: "))
    error_max = float(input("Ingrese error permitido (%): "))

    f_expr = sp.sympify(funcion)

    # Intento automático de despeje: x = x - f(x)
    g_expr = x - f_expr

    print("\nTransformacion utilizada:")
    print("g(x) =", g_expr)

    g = sp.lambdify(x, g_expr)

    ea = 100
    iteracion = 1

    print("\nIter |    x_i     |    x_(i+1)   |    Ea %")
    print("------------------------------------------------")

    while ea > error_max:

        x1 = g(x0)

        if iteracion > 1:
            ea = abs((x1 - x0) / x1) * 100

        print(f"{iteracion:4} | {x0:10.6f} | {x1:10.6f} | {ea:10.6f}")

        # Control de divergencia
        if abs(x1) > 1e6:
            print("\nEl metodo diverge.")
            return

        x0 = x1
        iteracion += 1

    print("\nRaiz aproximada:", x1)
    print("Error aproximado:", ea, "%")


# Ejecutar
punto_fijo()