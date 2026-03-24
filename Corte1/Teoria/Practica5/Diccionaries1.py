# Diccionario que guarda temperaturas por ubicación
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

# Diccionario con cantidad de cámaras por zona
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Mostrar el diccionario de sensores
print(sensors)

# Mostrar el diccionario de cámaras
print(num_cameras)

# Diccionario que traduce palabras a otro idioma
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}

# Mostrar las traducciones
print(translations)


## Ejemplo de error en diccionarios:

# Esto es inválido porque las listas NO pueden ser claves (son mutables)
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}

# Intentar imprimir esto generaría un error
print(powers)


# Diccionario con familias y nombres de sus hijos
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

# Mostrar el diccionario de hijos
print(children)


# Crear un diccionario vacío
my_empty_dictionary = {}

# Mostrar el diccionario vacío
print(my_empty_dictionary)


# Diccionario con productos y precios
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# Mostrar menú antes de agregar algo nuevo
print("Before: ", menu)

# Agregar un nuevo producto al menú
menu["cheesecake"] = 8

# Mostrar menú actualizado
print("After", menu)


# Diccionario inicial de animales en el zoológico
animals_in_zoo = {"dinosaurs": 0}

# Se redefine el diccionario (se pierde el anterior)
animals_in_zoo = {"dinosaurs": 0}

# Se vuelve a redefinir con otro contenido
animals_in_zoo = {"horses": 2}

# Mostrar el resultado final
print(animals_in_zoo)


## Agregar varios elementos de una vez

# Diccionario base de sensores
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}

# Mostrar antes de actualizar
print("Before", sensors)

# Agregar varias claves y valores
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})

# Mostrar después de actualizar
print("After", sensors)


# Diccionario con usuarios y sus IDs
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

# Mostrar usuarios iniciales
print(user_ids)

# Agregar nuevos usuarios
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

# Mostrar usuarios actualizados
print(user_ids)


## Modificar valores existentes

# Agregar o cambiar un elemento
menu["banana"] = 3

# Diccionario de menú
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}

# Mostrar antes del cambio
print("Before: ", menu)

# Cambiar el precio de un producto existente
menu["oatmeal"] = 5

# Mostrar después del cambio
print("After", menu)


# Diccionario con ganadores de premios
oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

# Mostrar antes de modificar
print("Before", oscar_winners)
print()

# Agregar nueva categoría
oscar_winners.update({"Supporting Actress": "Viola Davis"})

# Mostrar después de agregar
print("After1", oscar_winners)
print()

# Cambiar el valor de una categoría existente
oscar_winners["Best Picture"] = "Moonlight"

# Mostrar después del cambio
print("After2", oscar_winners)


### Crear diccionarios usando comprensión

# Lista de nombres
names = ['Jenny', 'Alexus', 'Sam', 'Grace']

# Lista de alturas
heights = [61, 70, 67, 64]

# Combinar listas en pares (tuplas)
zipStudents = zip(names, heights)

# Mostrar objeto zip
print("zipStudents: ", zipStudents)

# Crear diccionario usando comprensión
students = {key: value for key, value in zip(names, heights)}

# Mostrar el diccionario
print(students)


# Lista de bebidas
drinks = ["espresso", "chai", "decaf", "drip"]

# Cantidad de cafeína
caffeine = [64, 40, 0, 120]

# Combinar listas
zipped_drinks = zip(drinks, caffeine)

# Mostrar zip
print(zipped_drinks)

# Crear diccionario con comprensión
drinks_to_caffeine = {key: value for key, value in zipped_drinks}

# Mostrar resultado
print(drinks_to_caffeine)


# Lista de canciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]

# Número de reproducciones
playcounts = [78, 29, 44, 21, 89, 5]

# Crear diccionario combinando ambas listas
plays = {key: value for key, value in zip(songs, playcounts)}

# Mostrar diccionario
print(plays)

# Agregar nueva canción
plays.update({"Purple Haze": 1})

# Modificar reproducciones de una canción existente
plays.update({"Respect": 94})

# Mostrar cambios
print("After: ", plays)

# Diccionario que contiene otros diccionarios (anidado)
library = {"The Best Songs": plays, "Sunday Feelings": {}}

# Mostrar la biblioteca completa
print(library)
