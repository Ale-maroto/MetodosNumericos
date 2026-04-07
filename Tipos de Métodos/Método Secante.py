# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:13:53 2026

@author: Alejandro
"""

#Versión 3.0.0
#Eliminé eval()
#Cambié error relativo a Error Absoluto
#Mejore el codigo de la grafica

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def metodo_secante():

    x = sp.symbols('x')

    print("METODO DE LA SECANTE\n")

    # Entrada de datos
    funcion = input("Ingrese f(x): ")
    x0 = float(input("Ingrese x0: "))
    x1 = float(input("Ingrese x1: "))
    tol = float(input("Ingrese error permitido: "))

    # Convertir función
    f_expr = sp.sympify(funcion)
    f = sp.lambdify(x, f_expr, "numpy")

    ea = 100
    iteracion = 1
    MAX_ITER = 100

    print("\nIter |     x_i      |    Error")
    print("----------------------------------")

    # Guardar iteraciones
    x_vals_iter = []
    fx_vals_iter = []

    while ea > tol and iteracion <= MAX_ITER:

        f_x0 = f(x0)
        f_x1 = f(x1)

        # Evitar división entre cero
        if (f_x1 - f_x0) == 0:
            print("\n❌ Error: división entre cero.")
            return

        # Fórmula de la secante
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

        # ERROR CORREGIDO (sin división)
        ea = abs(x2 - x1)

        print(f"{iteracion:4} | {x2:12.6f} | {ea:10.6f}")

        # Guardar puntos
        x_vals_iter.append(x2)
        fx_vals_iter.append(f(x2))

        if ea < tol:
            break

        x0, x1 = x1, x2
        iteracion += 1

    print("\nRaíz aproximada:", x2)
    print("Error aproximado:", ea)

    # -------- GRAFICA --------
    x_min = min(x_vals_iter + [x2]) - 1
    x_max = max(x_vals_iter + [x2]) + 1
    x_vals = np.linspace(x_min, x_max, 200)

    y_vals = []
    for val in x_vals:
        try:
            y_vals.append(f(val))
        except:
            y_vals.append(np.nan)

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0)

    plt.scatter(x_vals_iter, fx_vals_iter, color='red', label="Iteraciones")

    plt.title("Método de la Secante")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

metodo_secante()
