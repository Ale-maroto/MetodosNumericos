# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:51:58 2026

@author: Alejandro
"""
#Versión 4.1.0
#Quite f(x) de el método punto fijo 
#Tambien puse para graficar cualquier método

import math
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols('x')

# -------------------------
# MENÚ
# -------------------------
print("===== METODOS NUMERICOS =====")
print("1. Método de Bisección")
print("2. Método de Regla Falsa")
print("3. Método de Newton-Raphson")
print("4. Método de la Secante")
print("5. Método de Punto Fijo")

opcion = input("Seleccione el método: ")

# -------------------------
# FUNCIÓN GENERAL (excepto punto fijo)
# -------------------------
if opcion != "5":
    funcion = input("\nIngresa la función en términos de x: ")

    def f(x_val):
        return eval(funcion, {
            "x": x_val,
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
# FUNCIÓN PARA GRAFICAR
# -------------------------
def graficar(func, rango=(-5,5), puntos_raiz=[]):
    xs = np.linspace(rango[0], rango[1], 400)
    ys = []

    for val in xs:
        try:
            ys.append(func(val))
        except:
            ys.append(np.nan)

    plt.axhline(0)
    plt.plot(xs, ys, label="f(x)")

    for p in puntos_raiz:
        plt.scatter(p, func(p), color="red")

    plt.legend()
    plt.grid()
    plt.show()

# -------------------------
# NEWTON-RAPHSON
# -------------------------
if opcion == "3":

    x0 = float(input("Valor inicial: "))
    error_permitido = float(input("Error permitido: "))

    f_expr = sp.sympify(funcion)
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, "math")

    error = 100
    puntos = []

    while error > error_permitido:
        x1 = x0 - f(x0) / df(x0)

        puntos.append(x1)

        error = abs((x1 - x0) / x1)
        x0 = x1

    print("Raíz:", x1)

    graficar(f, puntos_raiz=puntos)

# -------------------------
# SECANTE
# -------------------------
elif opcion == "4":

    x0 = float(input("x0: "))
    x1 = float(input("x1: "))
    error_permitido = float(input("Error permitido: "))

    error = 100
    puntos = []

    while error > error_permitido:

        x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))

        puntos.append(x2)

        error = abs((x2 - x1) / x2)
        x0 = x1
        x1 = x2

    print("Raíz:", x2)

    graficar(f, puntos_raiz=puntos)

# -------------------------
# PUNTO FIJO (CORREGIDO)
# -------------------------
elif opcion == "5":

    g_funcion = input("Ingresa g(x): ")
    x0 = float(input("Valor inicial: "))
    error_permitido = float(input("Error permitido: "))

    g_expr = sp.sympify(g_funcion)
    g = sp.lambdify(x, g_expr, "math")

    error = 100
    puntos = []

    while error > error_permitido:

        x1 = g(x0)
        puntos.append(x1)

        error = abs((x1 - x0) / x1)
        x0 = x1

    print("Raíz:", x1)

    # graficamos g(x)
    graficar(g, puntos_raiz=puntos)

# -------------------------
# BISECCIÓN Y REGLA FALSA
# -------------------------
else:

    a = float(input("a: "))
    b = float(input("b: "))
    error_permitido = float(input("Error permitido: "))

    error = abs(b - a)
    puntos = []

    while error > error_permitido:

        if opcion == "1":
            xr = (a + b) / 2
        else:
            xr = b - (f(b)*(a-b))/(f(a)-f(b))

        puntos.append(xr)

        if f(a)*f(xr) < 0:
            b = xr
        else:
            a = xr

        error = abs(b - a)

    print("Raíz:", xr)

    graficar(f, rango=(a-2, b+2), puntos_raiz=puntos)



