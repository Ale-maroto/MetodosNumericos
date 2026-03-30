#Versión 2.0.0
#Se agrego código para gráficar
#Y tambien agregar las funciones matematicas

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import math

def falsa_posicion():

    x = sp.symbols('x')

    print("METODO DE FALSA POSICION\n")

    funcion = input("Ingrese la funcion f(x): ")
    xl = float(input("Ingrese el limite inferior xl: "))
    xu = float(input("Ingrese el limite superior xu: "))
    error_max = float(input("Ingrese el error aproximado permitido (%): "))

    # Función con soporte matemático
    def f(val):
        return eval(funcion, {"x": val, "math": math,
                             "sin": math.sin, "cos": math.cos, "tan": math.tan,
                             "exp": math.exp, "log": math.log, "sqrt": math.sqrt})

    if f(xl) * f(xu) > 0:
        print("\nNo se puede aplicar el metodo.")
        return

    print("\nIter | xl | xu | xr | f(xr) | Ea %")

    xr_anterior = 0
    ea = 100
    iteracion = 1

    xr_vals = []
    fx_vals = []

    while ea > error_max:

        xr = xu - (f(xu)*(xl-xu))/(f(xl)-f(xu))

        if iteracion > 1:
            ea = abs((xr - xr_anterior)/xr) * 100

        print(iteracion, xl, xu, xr, f(xr), ea)

        xr_vals.append(xr)
        fx_vals.append(f(xr))

        if f(xl)*f(xr) < 0:
            xu = xr
        else:
            xl = xr

        xr_anterior = xr
        iteracion += 1

    print("\nRaiz aproximada:", xr)

    # -------- GRAFICA --------
    x_vals = np.linspace(xl-1, xu+1, 100)
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")
    plt.axhline(0)
    plt.scatter(xr_vals, fx_vals, label="Iteraciones")

    plt.title("Método de Falsa Posición")
    plt.legend()
    plt.grid()
    plt.show()

falsa_posicion()
