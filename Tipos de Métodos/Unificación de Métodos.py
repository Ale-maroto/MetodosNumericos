# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:51:58 2026

@author: Alejandro
"""
#Versión 4.0.0
#Agrege el método de punto fijo

import math
import sympy as sp

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
# FUNCIÓN GENERAL
# -------------------------
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
# NEWTON-RAPHSON
# -------------------------
if opcion == "3":

    x0 = float(input("Ingresa el valor inicial: "))
    error_permitido = float(input("Ingresa el error permitido: "))

    f_expr = sp.sympify(funcion)
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, "math")

    print("\nDerivada:", df_expr)

    print("\nIter | x_n | f(x_n) | f'(x_n) | Error")
    print("------------------------------------------------")

    i = 1
    error = 100

    while error > error_permitido:

        if df(x0) == 0:
            print("\nError: derivada cero.")
            break

        x1 = x0 - f(x0) / df(x0)

        if i > 1:
            error = abs((x1 - x0) / x1)

        print(i, "\t", round(x0,6), "\t", round(f(x0),6), "\t", round(df(x0),6), "\t", round(error,6))

        x0 = x1
        i += 1

    print("\nRaíz aproximada:", round(x1,6))
    print("Error final:", error)

# -------------------------
# SECANTE
# -------------------------
elif opcion == "4":

    x0 = float(input("Ingresa x0: "))
    x1 = float(input("Ingresa x1: "))
    error_permitido = float(input("Ingresa el error permitido: "))

    print("\nIter | x_(i-1) | x_i | x_(i+1) | Error")
    print("------------------------------------------------")

    i = 1
    error = 100

    while error > error_permitido:

        if f(x1) - f(x0) == 0:
            print("\nError: división entre cero.")
            break

        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))

        if i > 1:
            error = abs((x2 - x1) / x2)

        print(i, "\t", round(x0,6), "\t", round(x1,6), "\t", round(x2,6), "\t", round(error,6))

        x0 = x1
        x1 = x2
        i += 1

    print("\nRaíz aproximada:", round(x2,6))
    print("Error final:", error)

# -------------------------
# PUNTO FIJO
# -------------------------
elif opcion == "5":

    g_funcion = input("Ingresa g(x): ")
    x0 = float(input("Ingresa el valor inicial: "))
    error_permitido = float(input("Ingresa el error permitido: "))

    try:
        g_expr = sp.sympify(g_funcion)
        g = sp.lambdify(x, g_expr, "math")
    except:
        print("Error en g(x).")
        exit()

    # Verificar convergencia
    try:
        g_deriv = sp.lambdify(x, sp.diff(g_expr, x), "math")
        val = abs(g_deriv(x0))
        print(f"\n|g'(x0)| = {val:.4f}")

        if val >= 1:
            print("⚠ Puede no converger\n")
        else:
            print("✔ Convergencia probable\n")
    except:
        print("No se pudo evaluar la derivada.\n")

    print("\nIter | x_i | x_(i+1) | Error")
    print("------------------------------------------------")

    i = 1
    error = 100

    while error > error_permitido:

        try:
            x1 = g(x0)
        except:
            print("Error numérico.")
            break

        if i > 1:
            error = abs((x1 - x0) / x1)

        print(i, "\t", round(x0,6), "\t", round(x1,6), "\t", round(error,6))

        if abs(x1) > 1e6:
            print("\nEl método diverge.")
            break

        x0 = x1
        i += 1

    print("\nRaíz aproximada:", round(x1,6))
    print("Error final:", error)

# -------------------------
# BISECCIÓN Y REGLA FALSA
# -------------------------
else:

    a = float(input("Ingresa el valor de a: "))
    b = float(input("Ingresa el valor de b: "))
    error_permitido = float(input("Ingresa el error permitido: "))

    if f(a) * f(b) >= 0:
        print("\nNo se puede aplicar el método en este intervalo.")
    else:

        print("\nIter | a | b | xr | f(xr) | Error")
        print("------------------------------------------------")

        i = 1
        xr_anterior = a
        error = abs(b - a)

        while error > error_permitido:

            if opcion == "1":
                xr = (a + b) / 2
            elif opcion == "2":
                xr = b - (f(b) * (a - b)) / (f(a) - f(b))
            else:
                print("Opción inválida")
                break

            fxr = f(xr)

            if i > 1:
                error = abs((xr - xr_anterior) / xr)

            print(i, "\t", round(a,6), "\t", round(b,6), "\t", round(xr,6), "\t", round(fxr,6), "\t", round(error,6))

            if f(a) * fxr < 0:
                b = xr
            else:
                a = xr

            xr_anterior = xr
            i += 1

        print("\nRaíz aproximada:", round(xr,6))
        print("Error final:", error)



