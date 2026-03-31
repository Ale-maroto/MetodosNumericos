# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:06:13 2026

@author: Alejandro
"""
# Versión 3.0.0

import sympy as sp

def punto_fijo():

    x = sp.symbols('x')

    print("=== METODO DE PUNTO FIJO ===\n")

    # Entrada de datos
    g_funcion = input("Ingrese g(x): ")
    x0 = float(input("Ingrese valor inicial x0: "))
    error_max = float(input("Ingrese error permitido (%): "))

    try:
        g_expr = sp.sympify(g_funcion)
        g = sp.lambdify(x, g_expr, "math")
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

        # control de divergencia
        if abs(x1) > 1e6:
            print("\nEl método diverge.")
            return

        x0 = x1
        iteracion += 1

    print("\nRaiz aproximada:", x1)
    print("Error aproximado:", ea, "%")


# Ejecutar
punto_fijo()

