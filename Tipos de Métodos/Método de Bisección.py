# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 13:23:12 2026

@author: Alejandro
"""

#Versión 2.1.0
#Se me olvido agregar las funciones matematicas
 
import math
import numpy as np
import matplotlib.pyplot as plt

# Ingresar la función
funcion = input("Ingresa la función en términos de x: ")

# Crear función evaluable (con funciones matemáticas habilitadas)
def f(x):
    return eval(funcion, {"x": x, "math": math, 
                          "sin": math.sin, "cos": math.cos, "tan": math.tan,
                          "exp": math.exp, "log": math.log, "sqrt": math.sqrt})

# Intervalo
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))

# Error permitido
error_permitido = float(input("Ingresa el error permitido: "))

# Verificar condición
if f(a) * f(b) >= 0:
    print("\nNo se puede aplicar el método de bisección en este intervalo.")
else:
    
    print("\ni\t a\t\t b\t\t p\t\t f(p)\t\t Error")

    i = 1
    error = abs(b - a)

    p_vals = []
    fp_vals = []

    while error > error_permitido:
        
        p = (a + b) / 2
        fp = f(p)

        print(i, "\t", round(a,6), "\t", round(b,6), "\t", round(p,6), "\t", round(fp,6), "\t", round(error,6))

        p_vals.append(p)
        fp_vals.append(fp)

        if f(a) * fp < 0:
            b = p
        else:
            a = p

        error = abs(b - a)
        i += 1

    print("\nRaíz aproximada:", round(p,6))
    print("Error final:", error)

    # -------- GRAFICA --------
    x_vals = np.linspace(a-1, b+1, 100)
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0)
    plt.scatter(p_vals, fp_vals, label="Iteraciones")

    plt.title("Método de Bisección")
    plt.legend()
    plt.grid()
    plt.show()
