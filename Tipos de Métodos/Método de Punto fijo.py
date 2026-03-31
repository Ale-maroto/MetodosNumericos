# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:06:13 2026

@author: Alejandro
"""
#Versión 4.0.0
#Agrege las funciones matematicas y ltambien la grafica
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

def punto_fijo():

    x = sp.symbols('x')

    print("=== METODO DE PUNTO FIJO ===\n")

    # Entrada de datos
    g_funcion = input("Ingrese g(x): ")
    x0 = float(input("Ingrese valor inicial x0: "))
    error_max = float(input("Ingrese error permitido (%): "))

    try:
        g_expr = sp.sympify(g_funcion)

        # Función con soporte matemático
        def g(val):
            return eval(g_funcion, {"x": val, "math": math,
                                   "sin": math.sin, "cos": math.cos, "tan": math.tan,
                                   "exp": math.exp, "log": math.log, "sqrt": math.sqrt})
    except:
        print("Error en la función g(x).")
        return

    # Verificar convergencia
    try:
        g_deriv = sp.lambdify(x, sp.diff(g_expr, x), "math")
        val = abs(g_deriv(x0))
        print(f"\n|g'(x0)| = {val:.4f}")

        if val >= 1:
            print("⚠ Advertencia: puede NO converger\n")
        else:
            print("✔ Condición de convergencia cumplida\n")
    except:
        print("No se pudo evaluar la derivada.\n")

    ea = 100
    iteracion = 1

    print("Iter |    x_i     |    x_(i+1)   |    Ea %")
    print("------------------------------------------------")

    # Guardar iteraciones
    x_vals_iter = []
    gx_vals_iter = []

    while ea > error_max:

        try:
            x1 = g(x0)
        except:
            print("\nError numérico.")
            return

        if iteracion > 1:
            if x1 != 0:
                ea = abs((x1 - x0) / x1) * 100
            else:
                ea = 0

        print(f"{iteracion:4} | {x0:10.6f} | {x1:10.6f} | {ea:10.6f}")

        # Guardar puntos
        x_vals_iter.append(x0)
        gx_vals_iter.append(g(x0))

        # Control de divergencia
        if abs(x1) > 1e6:
            print("\nEl método diverge.")
            return

        x0 = x1
        iteracion += 1

    print("\nRaiz aproximada:", x1)
    print("Error aproximado:", ea, "%")

    # -------- GRAFICA --------
    x_min = min(x_vals_iter + [x1]) - 1
    x_max = max(x_vals_iter + [x1]) + 1
    x_vals = np.linspace(x_min, x_max, 200)
    y_vals = [g(val) for val in x_vals]

    plt.plot(x_vals, y_vals, label="g(x)")
    plt.axhline(0)

    # Puntos de iteraciones
    plt.scatter(x_vals_iter, gx_vals_iter, label="Iteraciones")

    plt.title("Método de Punto Fijo")
    plt.xlabel("x")
    plt.ylabel("g(x)")
    plt.legend()
    plt.grid()
    plt.show()


punto_fijo()
