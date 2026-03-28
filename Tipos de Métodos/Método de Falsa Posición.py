import sympy as sp

def falsa_posicion():

    x = sp.symbols('x')

    print("METODO DE FALSA POSICION\n")

    funcion = input("Ingrese la funcion f(x): ")
    xl = float(input("Ingrese el limite inferior xl: "))
    xu = float(input("Ingrese el limite superior xu: "))
    error_max = float(input("Ingrese el error aproximado permitido (%): "))

    f = sp.lambdify(x, sp.sympify(funcion))

    # Verificar cambio de signo
    if f(xl) * f(xu) > 0:
        print("\nNo se puede aplicar el metodo.")
        print("La funcion no cambia de signo en el intervalo.")
        return

    print("\nIter |     xl     |     xu     |     xr     |    f(xr)    |    Ea %")
    print("---------------------------------------------------------------------")

    xr_anterior = 0
    ea = 100
    iteracion = 1

    while ea > error_max:

        xr = xu - (f(xu)*(xl-xu))/(f(xl)-f(xu))

        if iteracion > 1:
            ea = abs((xr - xr_anterior)/xr) * 100

        print(f"{iteracion:4} | {xl:10.6f} | {xu:10.6f} | {xr:10.6f} | {f(xr):10.6f} | {ea:10.6f}")

        if f(xl)*f(xr) < 0:
            xu = xr
        else:
            xl = xr

        xr_anterior = xr
        iteracion += 1

    print("\nRaiz aproximada:", xr)
    print("Error aproximado:", ea,"%")

falsa_posicion()