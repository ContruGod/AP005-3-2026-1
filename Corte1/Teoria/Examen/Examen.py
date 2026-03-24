# Categorías disponibles (no cambian durante el programa)
categorias = ("CPU", "GPU", "RAM", "Almacenamiento", "Fuente", "Motherboard")

# Lista donde se guardan todos los componentes
inventario = [
    {"codigo": 1001, "nombre": "Ryzen 5 5600X", "precio": 650000, "cantidad": 5, "categoria": "CPU"},
    {"codigo": 1002, "nombre": "Intel i5 12400F", "precio": 700000, "cantidad": 3, "categoria": "CPU"},
    {"codigo": 2001, "nombre": "RTX 3060", "precio": 1800000, "cantidad": 2, "categoria": "GPU"},
    {"codigo": 2002, "nombre": "RX 6600", "precio": 900000, "cantidad": 4, "categoria": "GPU"},
    {"codigo": 3001, "nombre": "16GB DDR4", "precio": 120000, "cantidad": 10, "categoria": "RAM"},
    {"codigo": 4001, "nombre": "SSD 1TB", "precio": 300000, "cantidad": 6, "categoria": "Almacenamiento"},
    {"codigo": 5001, "nombre": "Fuente 650W", "precio": 280000, "cantidad": 4, "categoria": "Fuente"},
    {"codigo": 6001, "nombre": "B550 Motherboard", "precio": 500000, "cantidad": 3, "categoria": "Motherboard"}
]

# Función para validar que el usuario solo ingrese números
def solo_numeros(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)
        else:
            print("Error: solo se permiten números")

print("BIENVENIDO AL INVENTARIO DE COMPONENTES DE PC")

# Bucle principal del programa
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar componente")
    print("2. Mostrar componentes")
    print("3. Buscar componente")
    print("4. Eliminar componente")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Agregar componente (con verificación por código)
    if opcion == "1":
        codigo = solo_numeros("Código del componente: ")

        # Buscar si ya existe
        encontrado = False
        for c in inventario:
            if c["codigo"] == codigo:
                print("El componente ya existe:")
                print(f"Nombre: {c['nombre']}")
                print(f"Cantidad actual: {c['cantidad']}")

                cantidad = solo_numeros("Cantidad a agregar: ")
                c["cantidad"] += cantidad

                print("Cantidad actualizada correctamente")
                encontrado = True
                break

        # Si no existe, se crea uno nuevo
        if not encontrado:
            nombre = input("Nombre: ")
            precio = solo_numeros("Precio: ")
            cantidad = solo_numeros("Cantidad: ")

            print("Categorías disponibles:", categorias)
            categoria = input("Categoría: ")

            if categoria not in categorias:
                print("Categoría no válida")
                continue

            componente = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "categoria": categoria
            }

            inventario.append(componente)
            print("Componente agregado correctamente")

    # Mostrar todos los componentes
    elif opcion == "2":
        if len(inventario) == 0:
            print("No hay componentes registrados")
        else:
            print("\n--- LISTA DE COMPONENTES ---")
            for c in inventario:
                print(f"Código: {c['codigo']} | Nombre: {c['nombre']} | Precio: {c['precio']} | Cantidad: {c['cantidad']} | Categoría: {c['categoria']}")

    # Buscar componente por código
    elif opcion == "3":
        buscar = solo_numeros("Ingrese el código a buscar: ")
        encontrado = False

        for c in inventario:
            if c["codigo"] == buscar:
                print("\nComponente encontrado:")
                print(f"Código: {c['codigo']}")
                print(f"Nombre: {c['nombre']}")
                print(f"Precio: {c['precio']}")
                print(f"Cantidad: {c['cantidad']}")
                print(f"Categoría: {c['categoria']}")
                encontrado = True

        if not encontrado:
            print("Componente no encontrado")

    # Eliminar o reducir cantidad
    elif opcion == "4":
        eliminar = solo_numeros("Código del componente a eliminar: ")
        encontrado = False

        for c in inventario:
            if c["codigo"] == eliminar:
                encontrado = True

                print("\nComponente encontrado:")
                print(f"Código: {c['codigo']}")
                print(f"Nombre: {c['nombre']}")
                print(f"Precio: {c['precio']}")
                print(f"Cantidad: {c['cantidad']}")
                print(f"Categoría: {c['categoria']}")

                cantidad_eliminar = solo_numeros("¿Cuántos desea eliminar?: ")

                if cantidad_eliminar >= c["cantidad"]:
                    inventario.remove(c)
                    print("Se eliminó completamente el componente")
                else:
                    c["cantidad"] -= cantidad_eliminar
                    print("Cantidad actualizada")

                break

        if not encontrado:
            print("No se encontró el componente")

    # Salir del programa
    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida, intente de nuevo")
