# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:51:58 2026

@author: Alejandro
"""
#Versión 4.4.0
#Mejore partes impotantes en lo metodos

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = sp.symbols('x')

#MENÚ
print("===== METODOS NUMERICOS =====")
print("1. Método de Bisección")
print("2. Método de Regla Falsa")
print("3. Método de Newton-Raphson")
print("4. Método de la Secante")
print("5. Método de Punto Fijo")

opcion = input("Seleccione el método: ")

#FUNCIÓN
if opcion != "5":
    funcion = input("\nIngresa la función en términos de x: ")
    f_expr = sp.sympify(funcion)
    f = sp.lambdify(x, f_expr, "numpy")

#GRAFICAR
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

#CONFIG 
MAX_ITER = 100

#NEWTON
if opcion == "3":

    x0 = float(input("Valor inicial: "))
    tol = float(input("Error permitido: "))

    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, "numpy")

    print("\nIter | x_n       | f(x_n)    | Error")
    print("----------------------------------------")

    puntos = []

    for i in range(1, MAX_ITER+1):

        if df(x0) == 0:
            print("❌ Derivada cero. Se detiene.")
            break

        x1 = x0 - f(x0)/df(x0)
        puntos.append(x1)

        error = abs(x1 - x0)

        print(f"{i:<4} | {x0:<10.6f} | {f(x0):<10.6f} | {error:<10.6f}")

        if error < tol:
            break

        x0 = x1

    print("\nRaíz aproximada:", x1)
    graficar(f, puntos_raiz=puntos)

# SECANTE
elif opcion == "4":

    x0 = float(input("x0: "))
    x1 = float(input("x1: "))
    tol = float(input("Error permitido: "))

    print("\nIter | x_i       | Error")
    print("-----------------------------")

    puntos = []

    for i in range(1, MAX_ITER+1):

        denom = f(x1) - f(x0)
        if denom == 0:
            print("❌ División entre cero.")
            break

        x2 = x1 - f(x1)*(x1-x0)/denom
        puntos.append(x2)

        error = abs(x2 - x1)

        print(f"{i:<4} | {x1:<10.6f} | {error:<10.6f}")

        if error < tol:
            break

        x0, x1 = x1, x2

    print("\nRaíz aproximada:", x2)
    graficar(f, puntos_raiz=puntos)

#PUNTO FIJO
elif opcion == "5":

    g_funcion = input("Ingresa g(x): ")
    x0 = float(input("Valor inicial: "))
    tol = float(input("Error permitido: "))

    g_expr = sp.sympify(g_funcion)
    g = sp.lambdify(x, g_expr, "numpy")

    print("\nIter | x_i       | Error")
    print("-----------------------------")

    puntos = []

    for i in range(1, MAX_ITER+1):

        x1 = g(x0)
        puntos.append(x1)

        error = abs(x1 - x0)

        print(f"{i:<4} | {x1:<10.6f} | {error:<10.6f}")

        if error < tol:
            break

        if abs(x1) > 1e6:
            print("❌ El método diverge.")
            break

        x0 = x1

    print("\nRaíz aproximada:", x1)

    # Graficar f(x)=g(x)-x
    def h(val):
        return g(val) - val

    graficar(h, puntos_raiz=puntos)

#BISECCIÓN Y FALSA
else:

    a = float(input("a: "))
    b = float(input("b: "))
    tol = float(input("Error permitido: "))

    print("\nIter | xr        | Error")
    print("-----------------------------")

    puntos = []
    xr_old = a

    for i in range(1, MAX_ITER+1):

        if opcion == "1":
            xr = (a + b)/2
        else:
            denom = f(a) - f(b)
            if denom == 0:
                print("❌ División entre cero.")
                break
            xr = b - f(b)*(a-b)/denom

        puntos.append(xr)

        error = abs(xr - xr_old)

        print(f"{i:<4} | {xr:<10.6f} | {error:<10.6f}")

        if error < tol:
            break

        if f(a)*f(xr) < 0:
            b = xr
        else:
            a = xr

        xr_old = xr

    print("\nRaíz aproximada:", xr)
    graficar(f, rango=(a-2, b+2), puntos_raiz=puntos)


