# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:06:13 2026

@author: Alejandro
"""
#Version 2.0.0

import sympy as sp
import math

def punto_fijo_mejorado():

    x = sp.symbols('x')

    print("=== METODO DE PUNTO FIJO (PRO CORREGIDO) ===\n")

    funcion = input("Ingrese f(x)=0: ")
    x0 = float(input("Ingrese valor inicial x0: "))
    error_max = float(input("Ingrese error permitido (%): "))

    try:
        f_expr = sp.sympify(funcion)
    except:
        print("Error en la función ingresada.")
        return

    # Transformaciones seguras
    g_list = [
        x - f_expr,
        x - 0.1*f_expr,
        x - 0.01*f_expr,
        x + 0.1*f_expr
    ]

    print("\nProbando transformaciones...\n")

    mejor_g = None

    for i, g_expr in enumerate(g_list):

        try:
            g = sp.lambdify(x, g_expr, "math")
            g_deriv = sp.lambdify(x, sp.diff(g_expr, x), "math")

            val = abs(g_deriv(x0))

            print(f"g{i+1}(x) = {g_expr}  --->  |g'(x0)| = {val:.4f}")

            if val < 1:
                mejor_g = g_expr
                print("✔ Posible convergencia\n")
                break
            else:
                print("✖ No converge\n")

        except:
            print(f"g{i+1} inválida\n")

    if mejor_g is None:
        print("No se encontró una transformación automática adecuada.")
        print("Intenta definir manualmente g(x).")
        return

    print("Usando g(x):", mejor_g)

    g = sp.lambdify(x, mejor_g, "math")

    ea = 100
    iteracion = 1

    print("\nIter |    x_i     |    x_(i+1)   |    Ea %")
    print("------------------------------------------------")

    while ea > error_max:

        try:
            x1 = g(x0)
        except:
            print("\nError numérico durante la iteración.")
            return

        if iteracion > 1:
            ea = abs((x1 - x0) / x1) * 100 if x1 != 0 else 0

        print(f"{iteracion:4} | {x0:10.6f} | {x1:10.6f} | {ea:10.6f}")

        # Control de divergencia
        if abs(x1) > 1e6 or math.isnan(x1):
            print("\nEl método diverge.")
            return

        x0 = x1
        iteracion += 1

    print("\nRaiz aproximada:", x1)
    print("Error aproximado:", ea, "%")

punto_fijo_mejorado()

