# Categorías disponibles (no cambian durante el programa)
categorias = ("CPU", "GPU", "RAM", "Almacenamiento", "Fuente", "Motherboard")

# Lista donde se guardan todos los componentes
inventario = []

# Función para validar que el usuario solo ingrese números
def solo_numeros(mensaje):
    while True:
        valor = input(mensaje)
        if valor.isdigit():
            return int(valor)  # devuelve el número convertido a entero
        else:
            print("Error: solo se permiten números")

print("BIENVENIDO AL INVENTARIO DE COMPONENTES DE PC")

# Bucle principal del programa (mantiene el menú activo)
while True:
    print("\n--- MENÚ ---")
    print("1. Agregar componente")
    print("2. Mostrar componentes")
    print("3. Buscar componente")
    print("4. Eliminar componente")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    # Agregar un nuevo componente al inventario
    if opcion == "1":
        codigo = solo_numeros("Código del componente: ")
        nombre = input("Nombre: ")
        precio = solo_numeros("Precio: ")
        cantidad = solo_numeros("Cantidad: ")

        print("Categorías disponibles:", categorias)
        categoria = input("Categoría: ")

        # Verifica que la categoría esté dentro de las permitidas
        if categoria not in categorias:
            print("Categoría no válida")
            continue  # vuelve al menú

        # Revisa si ya existe un componente igual
        encontrado = False
        for c in inventario:
            if (c["codigo"] == codigo and
                c["nombre"] == nombre and
                c["precio"] == precio and
                c["categoria"] == categoria):

                c["cantidad"] += cantidad  # suma la cantidad si ya existe
                print("El componente ya existía, se actualizó la cantidad")
                encontrado = True
                break

        # Si no existe, lo agrega como nuevo
        if not encontrado:
            componente = {
                "codigo": codigo,
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
                "categoria": categoria
            }
            inventario.append(componente)
            print("Componente agregado correctamente")

    # Muestra todos los componentes guardados
    elif opcion == "2":
        if len(inventario) == 0:
            print("No hay componentes registrados")
        else:
            print("\n--- LISTA DE COMPONENTES ---")
            for c in inventario:
                # recorre la lista y muestra cada componente
                print(f"Código: {c['codigo']} | Nombre: {c['nombre']} | Precio: {c['precio']} | Cantidad: {c['cantidad']} | Categoría: {c['categoria']}")

    # Busca un componente usando su código
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

        # si no encuentra coincidencias
        if not encontrado:
            print("Componente no encontrado")

    # Elimina un componente o reduce su cantidad
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

                # si elimina todo o más, borra el componente completo
                if cantidad_eliminar >= c["cantidad"]:
                    inventario.remove(c)
                    print("Se eliminó completamente el componente")
                else:
                    c["cantidad"] -= cantidad_eliminar  # resta la cantidad
                    print("Cantidad actualizada")

                break  # sale del ciclo después de encontrarlo

        if not encontrado:
            print("No se encontró el componente")

    # Sale del programa
    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    # Controla opciones inválidas del menú
    else:
        print("Opción inválida, intente de nuevo")