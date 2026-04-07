# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:11:25 2026

@author: Alejandro
"""

#Versión 3.0.0
#Eliminé eval()
#Cambié error relativo a Error Absoluto
#Hice más robusta la gráfica

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def newton_raphson():

    x = sp.symbols('x')

    print("METODO DE NEWTON-RAPHSON\n")

    # Entrada de datos
    funcion = input("Ingrese f(x): ")
    x0 = float(input("Ingrese valor inicial: "))
    error_max = float(input("Ingrese error permitido (%): "))

    # Convertir función
    f_expr = sp.sympify(funcion)
    f = sp.lambdify(x, f_expr, "numpy")

    # Derivada
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, "numpy")

    print("\nDerivada calculada:")
    print("f'(x) =", df_expr)

    ea = 100
    iteracion = 1
    MAX_ITER = 100

    print("\nIter |    x_n     |   f(x_n)   |    Ea")
    print("------------------------------------------")

    # Guardar iteraciones
    x_vals_iter = []
    fx_vals_iter = []

    while ea > error_max and iteracion <= MAX_ITER:

        if df(x0) == 0:
            print("\n❌ Error: derivada cero.")
            return

        x1 = x0 - f(x0)/df(x0)

        # ✅ ERROR CORREGIDO (sin división por cero)
        ea = abs(x1 - x0)

        print(f"{iteracion:4} | {x0:10.6f} | {f(x0):10.6f} | {ea:10.6f}")

        x_vals_iter.append(x0)
        fx_vals_iter.append(f(x0))

        if ea < error_max:
            break

        x0 = x1
        iteracion += 1

    print("\nRaíz aproximada:", x1)
    print("Error aproximado:", ea)

    # -------- GRAFICA --------
    x_vals = np.linspace(x0-5, x0+5, 200)
    y_vals = []

    for val in x_vals:
        try:
            y_vals.append(f(val))
        except:
            y_vals.append(np.nan)

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0)

    plt.scatter(x_vals_iter, fx_vals_iter, label="Iteraciones")

    plt.title("Método de Newton-Raphson")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()

    plt.show()

newton_raphson()
