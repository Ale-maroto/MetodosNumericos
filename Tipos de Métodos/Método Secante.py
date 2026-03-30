# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 09:13:53 2026

@author: Alejandro
"""

#Versión 2.0.0
#Agrege la grafica y las funciones matematicas
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

def metodo_secante():

    x = sp.symbols('x')

    print("METODO DE LA SECANTE\n")

    # Entrada de datos
    funcion = input("Ingrese f(x): ")
    x0 = float(input("Ingrese x0: "))
    x1 = float(input("Ingrese x1: "))
    error_max = float(input("Ingrese error permitido (%): "))

    # Función con soporte matemático
    def f(val):
        return eval(funcion, {"x": val, "math": math,
                             "sin": math.sin, "cos": math.cos, "tan": math.tan,
                             "exp": math.exp, "log": math.log, "sqrt": math.sqrt})

    ea = 100
    iteracion = 1

    print("\nIter |    x_(i-1)   |    x_i     |    x_(i+1)   |    Ea %")
    print("-------------------------------------------------------------")

    # Guardar iteraciones
    x_vals_iter = []
    fx_vals_iter = []

    while ea > error_max:

        f_x0 = f(x0)
        f_x1 = f(x1)

        # Verificar división entre cero
        if (f_x1 - f_x0) == 0:
            print("\nError: división entre cero. El método no se puede aplicar.")
            return

        # Fórmula de la secante
        x2 = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)

        # Calcular error
        if iteracion > 1:
            ea = abs((x2 - x1) / x2) * 100

        print(f"{iteracion:4} | {x0:12.6f} | {x1:10.6f} | {x2:12.6f} | {ea:10.6f}")

        # Guardar puntos
        x_vals_iter.append(x1)
        fx_vals_iter.append(f_x1)

        # Actualizar valores
        x0 = x1
        x1 = x2

        iteracion += 1

    print("\nRaiz aproximada:", x2)
    print("Error aproximado:", ea, "%")

    # -------- GRAFICA --------
    x_min = min(x_vals_iter + [x2]) - 1
    x_max = max(x_vals_iter + [x2]) + 1
    x_vals = np.linspace(x_min, x_max, 200)
    y_vals = [f(val) for val in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0)

    # Puntos de iteraciones
    plt.scatter(x_vals_iter, fx_vals_iter, color='red', label="Iteraciones")

    plt.title("Método de la Secante")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()

metodo_secante()
