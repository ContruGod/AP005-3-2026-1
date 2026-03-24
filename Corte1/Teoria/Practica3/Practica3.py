while True:
    a = input("Por favor ingrese un número: ")

    try:
        num = int(a)

        if num % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")

    except ValueError:
        print("Error: debes ingresar un número válido")

    hacer = input("Para repetir digite 1: ")
    if hacer != "1":
        print("Programa finalizado.")
        break
