# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:06:13 2026

@author: Alejandro
"""
# Versión 1.1.0
import sympy as sp

def punto_fijo_mejorado():

    x = sp.symbols('x')

    print("=== METODO DE PUNTO FIJO  ===\n")

    funcion = input("Ingrese f(x)=0: ")
    x0 = float(input("Ingrese valor inicial x0: "))
    error_max = float(input("Ingrese error permitido (%): "))

    f_expr = sp.sympify(funcion)

    # Posibles transformaciones
    g_list = [
        x - f_expr,                         # g(x) = x - f(x)
        x + f_expr,                         # g(x) = x + f(x)
        -f_expr,                            # g(x) = -f(x)
    ]

    # Intentar despejar si es posible
    try:
        soluciones = sp.solve(f_expr, x)
        for sol in soluciones:
            g_list.append(sol)
    except:
        pass

    print("\nProbando transformaciones...\n")

    mejor_g = None

    for i, g_expr in enumerate(g_list):

        try:
            g_deriv = sp.diff(g_expr, x)
            g_deriv_func = sp.lambdify(x, g_deriv)

            val = abs(g_deriv_func(x0))

            print(f"g{i+1}(x) = {g_expr}  --->  |g'(x0)| = {val:.4f}")

            if val < 1:
                mejor_g = g_expr
                print("✔ Esta transformación puede converger\n")
                break
            else:
                print("✖ No converge\n")

        except:
            print("Error evaluando esta transformación\n")

    if mejor_g is None:
        print("No se encontró una transformación adecuada.")
        return

    print("Usando:")
    print("g(x) =", mejor_g)

    g = sp.lambdify(x, mejor_g)

    ea = 100
    iteracion = 1

    print("\nIter |    x_i     |    x_(i+1)   |    Ea %")
    print("------------------------------------------------")

    while ea > error_max:

        x1 = g(x0)

        if iteracion > 1:
            ea = abs((x1 - x0) / x1) * 100

        print(f"{iteracion:4} | {x0:10.6f} | {x1:10.6f} | {ea:10.6f}")

        if abs(x1) > 1e6:
            print("\nEl metodo diverge.")
            return

        x0 = x1
        iteracion += 1

    print("\nRaiz aproximada:", x1)
    print("Error aproximado:", ea, "%")


punto_fijo_mejorado()

