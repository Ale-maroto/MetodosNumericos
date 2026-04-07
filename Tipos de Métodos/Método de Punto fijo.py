# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:06:13 2026

@author: Alejandro
"""
#Versión 5.0.0
#Sin eval()
#Sin división por cero
#Error absoluto (estable)
#Verificación de convergencia

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def punto_fijo():

    x = sp.symbols('x')

    print("=== METODO DE PUNTO FIJO ===\n")

    # Entrada de datos
    g_funcion = input("Ingrese g(x): ")
    x0 = float(input("Ingrese valor inicial x0: "))
    tol = float(input("Ingrese error permitido: "))

    try:
        g_expr = sp.sympify(g_funcion)
        g = sp.lambdify(x, g_expr, "numpy")
    except:
        print("❌ Error en la función g(x).")
        return

    # Verificar convergencia
    try:
        g_deriv_expr = sp.diff(g_expr, x)
        g_deriv = sp.lambdify(x, g_deriv_expr, "numpy")

        val = abs(g_deriv(x0))
        print(f"\n|g'(x0)| = {val:.4f}")

        if val >= 1:
            print("⚠ Puede NO converger\n")
        else:
            print("✔ Convergencia probable\n")
    except:
        print("No se pudo evaluar la derivada.\n")

    ea = 100
    iteracion = 1
    MAX_ITER = 100

    print("Iter |     x_i     |    Error")
    print("--------------------------------")

    # Guardar iteraciones
    x_vals_iter = []
    gx_vals_iter = []

    while ea > tol and iteracion <= MAX_ITER:

        try:
            x1 = g(x0)
        except:
            print("❌ Error numérico.")
            return

        # ERROR CORREGIDO (sin división)
        ea = abs(x1 - x0)

        print(f"{iteracion:4} | {x1:10.6f} | {ea:10.6f}")

        x_vals_iter.append(x1)
        gx_vals_iter.append(g(x1))

        if ea < tol:
            break

        if abs(x1) > 1e6:
            print("\n❌ El método diverge.")
            return

        x0 = x1
        iteracion += 1

    print("\nRaíz aproximada:", x1)
    print("Error aproximado:", ea)

    # -------- GRAFICA --------
    def h(val):
        return g(val) - val

    x_min = min(x_vals_iter + [x1]) - 1
    x_max = max(x_vals_iter + [x1]) + 1
    x_vals = np.linspace(x_min, x_max, 200)

    y_vals = []
    for val in x_vals:
        try:
            y_vals.append(h(val))
        except:
            y_vals.append(np.nan)

    plt.plot(x_vals, y_vals, label="g(x) - x")
    plt.axhline(0)

    plt.scatter(x_vals_iter, [0]*len(x_vals_iter), label="Iteraciones")

    plt.title("Método de Punto Fijo")
    plt.xlabel("x")
    plt.ylabel("g(x) - x")
    plt.legend()
    plt.grid()
    plt.show()


punto_fijo()
