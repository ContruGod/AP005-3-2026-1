#### Acceder a una clave

# Diccionario que guarda alturas de edificios famosos
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Obtener la altura del Burj Khalifa
print(building_heights["Burj Khalifa"])  # Resultado: 828

# Obtener la altura del edificio Ping An
print(building_heights["Ping An"])  # Resultado: 599


# Diccionario con elementos y signos del zodiaco
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Mostrar los signos del elemento tierra
print(zodiac_elements["earth"])

# Mostrar los signos del elemento fuego
print(zodiac_elements["fire"])


## Intento de acceso a clave inexistente

# Diccionario de edificios otra vez
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Esto lanza error porque la clave no existe
print(building_heights["Landmark 81"])


## Evitar errores comprobando la clave

# Clave que queremos consultar
key_to_check = "Landmark 81"

# Revisar si la clave está en el diccionario
if key_to_check in building_heights:
    print(building_heights["Landmark 81"])


# Diccionario del zodiaco nuevamente
zodiac_elements = {
    "water": ["Cancer", "Scorpio", "Pisces"],
    "fire": ["Aries", "Leo", "Sagittarius"],
    "earth": ["Taurus", "Virgo", "Capricorn"],
    "air": ["Gemini", "Libra", "Aquarius"]
}

# Añadir un nuevo par clave-valor
zodiac_elements["energy"] = "Not a Zodiac element"

# Verificar antes de imprimir
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])


## Uso seguro de .get()

# Diccionario de edificios
building_heights = {
    "Burj Khalifa": 828,
    "Shanghai Tower": 632,
    "Abraj Al Bait": 601,
    "Ping An": 599,
    "Lotte World Tower": 554.5,
    "One World Trade": 541.3
}

# Obtener valor de forma segura
building_heights.get("Shanghai Tower")  # Devuelve 632

# Intentar obtener una clave que no existe (retorna None)
building_heights.get("My House")


# Diccionario con IDs de usuarios
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

# Obtener ID del usuario
user_ids.get("teraCoder")

# Asignar valor por defecto si no existe
if user_ids.get("teraCoder") == None:
    tc_id = 1000
else:
    tc_id = user_ids.get("teraCoder")

# Mostrar resultado
print(tc_id)


# Caso de clave inexistente
if user_ids.get("superStackSmash") == None:
    stack_id = 100000

# Mostrar valor asignado
print(stack_id)


### Eliminar una clave

# Diccionario con premios
raffle = {
    223842: "Teddy Bear",
    872921: "Concert Tickets",
    320291: "Gift Basket",
    412123: "Necklace",
    298787: "Pasta Maker"
}

# Quitar un elemento existente
print(raffle.pop(320291, "No Prize"))  # Devuelve "Gift Basket"

# Ver el diccionario actualizado
print(raffle)

# Intentar eliminar una clave que no está
print(raffle.pop(100000, "No Prize"))  # Devuelve "No Prize"

# Ver el diccionario
print(raffle)

# Eliminar otro elemento
print(raffle.pop(872921, "No Prize"))  # Devuelve "Concert Tickets"

# Estado final del diccionario
print(raffle)


# Diccionario con ítems disponibles
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}

# Vida inicial del jugador
health_points = 20

# Sumar valor del item eliminado (si existe)
health_points += available_items.pop("stamina grains", 0)

# Sumar otro item eliminado
health_points += available_items.pop("power stew", 0)

# Intento de eliminar un item inexistente
health_points += available_items.pop("mystic bread", 0)

# Mostrar ítems restantes
print(available_items)

# Mostrar vida total final
print(health_points)


## Obtener todas las claves

# Diccionario de calificaciones
test_scores = {
    "Grace": [80, 72, 90],
    "Jeffrey": [88, 68, 81],
    "Sylvia": [80, 82, 84],
    "Pedro": [98, 96, 95],
    "Martin": [78, 80, 78],
    "Dina": [64, 60, 75]
}

# Convertir claves a lista
print(list(test_scores))

# Recorrer e imprimir nombres
for student in test_scores.keys():
    print(student)


# Otros diccionarios
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# Obtener solo las claves
users = user_ids.keys()
lessons = num_exercises.keys()

# Mostrar claves
print(users)
print(lessons)


## Obtener todos los valores

# Recorrer listas de notas
for score_list in test_scores.values():
    print(score_list)


# Inicializar contador
total_exercises = 0

# Sumar todos los ejercicios
for exercises in num_exercises.values():
    total_exercises += exercises

# Mostrar total
print(total_exercises)


## Obtener claves y valores

# Diccionario de marcas importantes
biggest_brands = {
    "Apple": 184,
    "Google": 141.7,
    "Microsoft": 80,
    "Coca-Cola": 69.7,
    "Amazon": 64.8
}

# Recorrer e imprimir información
for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")


# Diccionario de porcentajes de mujeres por profesión
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

# Mostrar porcentaje por ocupación
for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
