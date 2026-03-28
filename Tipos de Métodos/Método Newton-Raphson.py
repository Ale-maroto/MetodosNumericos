# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:11:25 2026

@author: Alejandro
"""

import sympy as sp

def newton_raphson():

    x = sp.symbols('x')

    print("METODO DE NEWTON-RAPHSON\n")

    # Entrada de datos
    funcion = input("Ingrese f(x): ")
    x0 = float(input("Ingrese valor inicial: "))
    error_max = float(input("Ingrese error permitido (%): "))

    # Convertir función
    f_expr = sp.sympify(funcion)
    f = sp.lambdify(x, f_expr)

    # Derivar automáticamente
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr)

    print("\nDerivada calculada:")
    print("f'(x) =", df_expr)

    ea = 100
    iteracion = 1

    print("\nIter |    x_n     |   f(x_n)   |   f'(x_n)  |    Ea %")
    print("---------------------------------------------------------")

    while ea > error_max:

        # Verificar si la derivada es cero
        if df(x0) == 0:
            print("\nError: la derivada es cero. El método no se puede aplicar.")
            return

        # Fórmula de Newton
        x1 = x0 - f(x0)/df(x0)

        # Calcular error
        if iteracion > 1:
            ea = abs((x1 - x0)/x1) * 100

        print(f"{iteracion:4} | {x0:10.6f} | {f(x0):10.6f} | {df(x0):10.6f} | {ea:10.6f}")

        x0 = x1
        iteracion += 1

    print("\nRaiz aproximada:", x1)
    print("Error aproximado:", ea, "%")


# Ejecutar
newton_raphson()
