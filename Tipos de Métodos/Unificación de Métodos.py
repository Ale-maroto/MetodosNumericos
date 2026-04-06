# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:51:58 2026

@author: Alejandro
"""
#Versión 4.3.0
#Mejore parte de los metodos newton-raphson, secante y punto fijo.

import math
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols('x')

# MENÚ
print("===== METODOS NUMERICOS =====")
print("1. Método de Bisección")
print("2. Método de Regla Falsa")
print("3. Método de Newton-Raphson")
print("4. Método de la Secante")
print("5. Método de Punto Fijo")

opcion = input("Seleccione el método: ")

# FUNCIÓN GENERAL (CORREGIDA)
if opcion != "5":
    funcion = input("\nIngresa la función en términos de x: ")
    f_expr = sp.sympify(funcion)
    f = sp.lambdify(x, f_expr, "math")

# GRAFICAR
def graficar(func, rango=(-5,5), puntos_raiz=[]):
    xs = np.linspace(rango[0], rango[1], 400)
    ys = []

    for val in xs:
        try:
            ys.append(func(val))
        except:
            ys.append(np.nan)

    plt.axhline(0)
    plt.plot(xs, ys)

    for p in puntos_raiz:
        try:
            plt.scatter(p, func(p))
        except:
            pass

    plt.grid()
    plt.show()

# NEWTON-RAPHSON
if opcion == "3":

    x0 = float(input("Valor inicial: "))
    error_permitido = float(input("Error permitido: "))

    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, "math")

    print("\nIter | x_n | f(x_n) | f'(x_n) | Error")
    print("------------------------------------------------")

    error = 100
    i = 1
    puntos = []

    while error > error_permitido:

        if df(x0) == 0:
            print("Error: derivada cero")
            break

        x1 = x0 - f(x0)/df(x0)
        puntos.append(x1)

        if i > 1:
            error = abs((x1 - x0)/x1)

        print(i, "\t", round(x0,6), "\t", round(f(x0),6), "\t", round(df(x0),6), "\t", round(error,6))

        x0 = x1
        i += 1

    print("\nRaíz:", x1)
    graficar(f, puntos_raiz=puntos)

# SECANTE
elif opcion == "4":

    x0 = float(input("x0: "))
    x1 = float(input("x1: "))
    error_permitido = float(input("Error permitido: "))

    print("\nIter | x_(i-1) | x_i | x_(i+1) | Error")
    print("------------------------------------------------")

    error = 100
    i = 1
    puntos = []

    while error > error_permitido:

        if f(x1) - f(x0) == 0:
            print("Error: división entre cero")
            break

        x2 = x1 - (f(x1)*(x1-x0))/(f(x1)-f(x0))
        puntos.append(x2)

        if i > 1:
            error = abs((x2 - x1)/x2)

        print(i, "\t", round(x0,6), "\t", round(x1,6), "\t", round(x2,6), "\t", round(error,6))

        x0 = x1
        x1 = x2
        i += 1

    print("\nRaíz:", x2)
    graficar(f, puntos_raiz=puntos)

# PUNTO FIJO
elif opcion == "5":

    g_funcion = input("Ingresa g(x): ")
    x0 = float(input("Valor inicial: "))
    error_permitido = float(input("Error permitido: "))

    g_expr = sp.sympify(g_funcion)
    g = sp.lambdify(x, g_expr, "math")

    print("\nIter | x_i | x_(i+1) | Error")
    print("------------------------------------------------")

    error = 100
    i = 1
    puntos = []

    while error > error_permitido:

        x1 = g(x0)
        puntos.append(x1)

        if i > 1:
            error = abs((x1 - x0)/x1)

        if abs(x1) > 1e6:
            print("El método diverge")
            break

        print(i, "\t", round(x0,6), "\t", round(x1,6), "\t", round(error,6))

        x0 = x1
        i += 1

    print("\nRaíz:", x1)

    # Graficar f(x) = g(x) - x
    def h(val):
        return g(val) - val

    graficar(h, puntos_raiz=puntos)

# BISECCIÓN Y REGLA FALSA
else:

    a = float(input("a: "))
    b = float(input("b: "))
    error_permitido = float(input("Error permitido: "))

    print("\nIter | a | b | xr | f(xr) | Error")
    print("------------------------------------------------")

    error = abs(b - a)
    i = 1
    puntos = []
    xr_anterior = a

    while error > error_permitido:

        if opcion == "1":
            xr = (a + b)/2
        else:
            if f(a) - f(b) == 0:
                print("Error: división entre cero")
                break
            xr = b - (f(b)*(a-b))/(f(a)-f(b))

        puntos.append(xr)

        if i > 1:
            error = abs((xr - xr_anterior)/xr)

        print(i, "\t", round(a,6), "\t", round(b,6), "\t", round(xr,6), "\t", round(f(xr),6), "\t", round(error,6))

        if f(a)*f(xr) < 0:
            b = xr
        else:
            a = xr

        xr_anterior = xr
        i += 1

    print("\nRaíz:", xr)
    graficar(f, rango=(a-2, b+2), puntos_raiz=puntos)



