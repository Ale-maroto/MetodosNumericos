# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:11:25 2026

@author: Alejandro
"""

#Versión 2.0.0
# Agrege el codigo para la grafica y tambien agrege lo de las funciones matematicas

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

def newton_raphson():

    x = sp.symbols('x')

    print("METODO DE NEWTON-RAPHSON\n")

    # Entrada de datos
    funcion = input("Ingrese f(x): ")
    x0 = float(input("Ingrese valor inicial: "))
    error_max = float(input("Ingrese error permitido (%): "))

    # Convertir función
    f_expr = sp.sympify(funcion)

    # Función con soporte matemático
    def f(val):
        return eval(funcion, {"x": val, "math": math,
                             "sin": math.sin, "cos": math.cos, "tan": math.tan,
                             "exp": math.exp, "log": math.log, "sqrt": math.sqrt})

    # Derivada simbólica
    df_expr = sp.diff(f_expr, x)

    # Convertir derivada a función evaluable
    df = sp.lambdify(x, df_expr)

    print("\nDerivada calculada:")
    print("f'(x) =", df_expr)

    ea = 100
    iteracion = 1

    print("\nIter |    x_n     |   f(x_n)   |   f'(x_n)  |    Ea %")
    print("---------------------------------------------------------")

    # Guardar iteraciones
    x_vals_iter = []
    fx_vals_iter = []

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

        # Guardar puntos
        x_vals_iter.append(x0)
        fx_vals_iter.append(f(x0))

        x0 = x1
        iteracion += 1

    print("\nRaiz aproximada:", x1)
    print("Error aproximado:", ea, "%")

    # -------- GRAFICA --------
    x_vals = np.linspace(x0-5, x0+5, 200)
    y_vals = [f(val) for val in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0)

    # Puntos de iteraciones
    plt.scatter(x_vals_iter, fx_vals_iter, label="Iteraciones")

    plt.title("Método de Newton-Raphson")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()

    plt.show()

newton_raphson()

