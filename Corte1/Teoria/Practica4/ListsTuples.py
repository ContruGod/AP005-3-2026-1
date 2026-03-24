################# LISTAS ####################
###########################################

# Crea una lista con colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

# Imprime la lista completa
print(my_lista)

# Imprime el tipo de dato (list)
print(type(my_lista))

# Imprime el elemento en la posición 2 (tercer elemento)
print(my_lista[2])

# Imprime el tamaño de la lista
print("my_lista size: ", len(my_lista))

# Imprime los elementos desde la posición 0 hasta la 1
print(my_lista[0:2])

# Imprime los primeros dos elementos (equivalente al anterior)
print(my_lista[:2])

# Agrega un elemento al final de la lista
my_lista.append('Blanco')
print(my_lista)

# Inserta un elemento en la posición 3
my_lista.insert(3, 'Negro')
print(my_lista)

# Agrega varios elementos al final (concatena otra lista)
my_lista.extend(['Marron', 'Gris'])
print(my_lista)

# Busca la posición del elemento 'Azul'
print(my_lista.index('Azul'))

# Elimina el elemento 'Marron'
my_lista.remove('Marron')
print(my_lista)

# Inserta nuevamente 'Marron' en la posición 8
my_lista.insert(8, 'Marron')
print(my_lista)

# Elimina y retorna el último elemento
print(my_lista.pop())

# Guarda el tamaño de la lista
size = len(my_lista)
print("size = ", size)

# Crea una nueva lista repitiendo la original 3 veces
my_lista_3 = my_lista * 3
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()

# Ordena la lista (modifica la original, retorna None)
my_listaSort = my_lista.sort()
print(my_listaSort)  # Siempre imprime None

# Lista de números
my_NumList = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print("Ordering my_NumList: ")

# Ordena de menor a mayor
my_NumList.sort()
print(my_NumList)

# Ordena de mayor a menor
my_NumList.sort(reverse=True)
print("De menor a mayor: ", my_NumList)


################# TUPLAS ####################
###########################################

# Convierte la lista en una tupla (inmutable)
print("###########################")
print("###########################")
print("###########################")
print("############ TUPLAS #########")

my_tupla = tuple(my_lista)

# Imprime espacios
print()
print()

# Imprime la tupla
print("my_tuple: ", my_tupla)

# Accede a elementos por índice
print(my_tupla[0])
print(my_tupla[2])

# Verifica si 'Rojo' está en la tupla (True/False)
print('Rojo' in my_tupla)

# Cuenta cuántas veces aparece 'Rojo'
print(my_tupla.count('Rojo'))

# Tupla con un solo elemento (OJO: aquí es string, no tupla real)
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

# Empaquetado de tupla (sin paréntesis)
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

# Desempaquetado de tupla en variables
nombre, dia, mes, año = my_tupla

# Imprime cada valor
print(nombre)
print(dia)
print(mes)
print(año)

# Imprime todos los valores formateados
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convierte la tupla en lista
my_lista2 = list(my_tupla)

# Imprime la nueva lista
print(my_lista2)
