from collections import Counter
import random


# 1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista.
# Para finalizar # el usuario debe ingresar 0, el cual no debe guardarse.

num_list=[]

print("Ingresar 3 numeross y se guardaran en una lista")
while True:
    print(f"Ingrese otro numero")
    print("Si desea salir Ingrese 0")
    num=int(input())
    if (num!=0):
        num_list.append(num)
    else:
        break
print(f"Lista : {num_list}")
    
# 2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, 
# eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
print("Ingrese el numero que desea buscar ")
delete_num=False
find_num=int(input(" "))

if find_num in num_list:
    num_list.remove(find_num)
    print(f"El número {find_num} ha sido eliminado de la lista.")
    print(f"La nueva lista es: {num_list}")
else:
    print(f"El número {find_num} no está en la lista.")
# 3.	Imprimir la sumatoria de todos los números de la lista.
sum_num=0
for num in num_list:
    sum_num+=num
print(f"La suma de los numeros es : {sum_num}")
# 4.	Solicitar al usuario otro número y crear una lista con los elementos de la lista original, 
# que sean menores que el número dado. 
# Imprimir esta nueva lista, iterando por ella.
print("Ingrese un numero y se creara una lista con numeros menores al ingresado")
max_num=int(input())
second_num_list=[]

for num in num_list:
    if num < max_num:
       second_num_list.append(num)
print(f"La nueva lista con numeros menores a {max_num} es :")
print(second_num_list)
# 5.	Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta 
# por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original 
# es [5,16,2,5,57,5,2], la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]

list_with_out_tupple=[5,16,2,5,57,5,2]
print(f"Lista sin tuplas {list_with_out_tupple}")
list_tupple = [(list_with_out_tupple[i],list_with_out_tupple[i]+1 ) for i in range(0, len(list_with_out_tupple), 2)]

print(f"Lista con tuplas {list_tupple}")
# 6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. 
# A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.
# a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
# b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
primary_list=[]
secundary_list=[]
print("Ingrese los alumnos de primaria")
while True:
    print("Ingrese alumno")
    alum=input("Si desea salir ingrese x ")
    if alum!="x":
                primary_list.append(alum.capitalize())
    else:
        break
print("Ingrese los alumnos de secundaria")

while True:
    print("Ingrese alumno")
    alum=input("Si desea salir ingrese x ")
    if alum!="x":
            secundary_list.append(alum.capitalize())
    else:
        break
repeated_names=[]
no_repeated_names=[]
for alum in primary_list:
    if alum in secundary_list:
        repeated_names.append(alum)
    else: 
        no_repeated_names.append(alum)
school_list=primary_list+ secundary_list
for names in repeated_names:
    school_list.remove(names)
print(f"Nombres de los alumnos del nivel primario son {school_list}")
print(f" Los nombres repetidos son {repeated_names}")
print(f" Los nombres del nivel primario que no son repetidos en el nivel secundario son : {no_repeated_names}") 
# 7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings.     
# Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
# ‘r’:5
# ‘%’:3
# ‘a’:8
# ‘9’:1
list_string=[]
for i in range (0,3):
    word=input("Ingrese un string ")
    list_string.append(word)
char_of_list=[]
for string in list_string:
    for l in string:
        if l !=" ":
            char_of_list.append(l)
char_of_list.sort()
print(char_of_list)
count_list=Counter(char_of_list)

for char,count_char in count_list.items():
    print(f"El caracter :{char} se repite :{count_char}")

# 8.	Diez equipos de la liga inter-barrial identificados con los números 1, 2, 3, 4, …, 10, participaron en un 
# campeonato de fútbol con modalidad todos contra todos.
# Los goles anotados en cada encuentro se registraron en el siguiente cuadro:
 
# Escriba un programa que:
# o	Lea el cuadro de goles en un arreglo de dos dimensiones.
# o	Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
# o	Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
# o	Determine la cantidad de puntos obtenidos por cada equipo.

rows= 10
columns = 10
#Crea 10 columnas por cada una de las 10 filas de la lista
goals = [[0 for j in range(columns)] for i in range(rows)]

#Declara la cantidad de goles por partido
for r in range(rows):
    for c in range(columns):
        if r == c :
            goals[r][c] = 0
        else:
            goals[r][c] = random. randint(0, 6)

#Imprime la matriz
print("La tabla de goles: ")
for row in goals:
    print(row)

for r in range(rows):
    goals_scored = 0
    goals_allowed = 0
    win = 0
    lose= 0
    tie = 0
    print(f"-----Equipo {(r+1)}-----")
    for c in range(columns):
        #Sumar los goles anotados
        goals_scored += goals[r][c]
        #Suma de goles recibidos
        goals_allowed += goals[c][r]
        #Compara con la posicion contraria en la matriz
        if goals[r][c]> goals[c][r]:
            win += 1
        elif goals[r][c]==goals[c][r]:
            tie += 1
        else:
            lose +=1
    print(f"La cantidad de victorias es {win}")
    print(f"La cantidad de derrotas es {lose}")
    print(f"La cantidad de empates es {tie}")
    print(f"Goles hechos {goals_scored}\nGoles recibidos {goals_allowed}")



# 9.	Escribir un programa que simule el juego clásico de Memoria (Memotest) utilizando matrices. El juego consiste en un tablero de cartas boca abajo y el objetivo es encontrar todas las parejas de cartas iguales.
print("!Jugaremos al METATEST¡")
# Crear una matriz para el tablero
board= []
rows = 4
columns = 4

# Crear una lista con las imágenes posibles
images = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# Inicializar el tablero con cartas boca abajo
for i in range(rows):
    row = []
    for j in range(columns):
        row.append('*')
    board.append(row)

# Asignar aleatoriamente las parejas de cartas iguales
couples= images * 2
random.shuffle(couples)

# Función para mostrar el tablero actualizado
def show_board():
    for row in board:
        print(' '.join(row))

# Función para voltear una carta en el tablero
def flip_card(row, column):
    board[row][column] = couples[(row * columns + column) // 2]

# Inicializar el seguimiento de las parejas encontradas
found_couples = 0


# Juego principal
while found_couples< len(images):
    show_board()
    
    # Solicitar al jugador las coordenadas de la primera carta a voltear
    while True:
        row_flip = int(input("Ingrese la fila de la primera carta a voltear (0-3): "))
        column_flip = int(input("Ingrese la columna de la primera carta a voltear (0-3): "))
        if 0 <= row_flip < rows and 0 <= column_flip< columns:
            break
        else:
            print("Coordenadas fuera de los límites. Inténtalo de nuevo.")
    
    # Voltear la primera carta seleccionada por el jugador
    flip_card(row_flip, column_flip)
    show_board()

# Solicitar al jugador las coordenadas de la segunda carta a voltear
    while True:
        row_flip2 = int(input("Ingrese la fila de la segunda carta a voltear (0-3): "))
        column_flip2 = int(input("Ingrese la columna de la segunda carta a voltear (0-3): "))
        if 0 <= row_flip2 < rows and 0 <= column_flip2 < columns:
            break
        else:
            print("Coordenadas fuera de los límites. Inténtalo de nuevo.")
    
    # Voltear la segunda carta seleccionada por el jugador
    flip_card(row_flip2, column_flip2)
    show_board()
# Verificar si las cartas son iguales
    if board[row_flip][column_flip] == board[row_flip2][column_flip2]:
        print("¡Encontraste una pareja!")
        found_couples += 1
    else:
        print("No es una pareja. Inténtalo de nuevo.")

print("¡Felicidades, encontraste todas las parejas!")


# 10.	Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
# a.	la diagonal principal.
# b.	la diagonal inversa.
print("Ingresa el tamaño que desea de la matriz cuadrada")
size_matrix=int(input())
square_matrix=[[None]*size_matrix for _ in range(size_matrix)]
for row in range(size_matrix):
    for col in range(size_matrix):
        print(f"Ingrese que numero desea en el casillero {row}: {col}")
        num=int(input())
        square_matrix[row][col]=num

main_diagonal=[]
reverse_diagonal=[]

for i in range(0,size_matrix):
    main_diagonal.append(square_matrix[i][i])
    reverse_diagonal.append(square_matrix[i][size_matrix-1-i])
print(f"Matriz Cuadrada ")
for row in square_matrix:
    print(row)
print(f"diagonal principal {main_diagonal}")
print(f"diagonal inversa {reverse_diagonal}")

    
    

# 11.	Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
foreign_currency={
    'Euro':'€', 
    'Dollar':'$',
    'Yen':'¥',
    "Peso":"$",
    'Libra':'£'
}
print("Ingrese la moneda que desea y se le mostrara su simbolo")
user_currency=input().capitalize()
if user_currency in foreign_currency:
    print(foreign_currency[user_currency])
else:
    print(f"La divisa {user_currency} no esta registrada")

# 12.	Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>’.
print("Ingrese los siguientes datos")
name=input("nombre :")
age=input("edad :")
loc=input("direccion :")
tel=input("Telefono :")
person={
    "name":name.capitalize(),
    "age":age,
    "loc":loc.capitalize(),
    "tel":tel
}
print(f"El usuario {name} tien {age} , vive en {loc}, y su numero de telefono es {tel}")
# 13.	Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
# un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar 
# un mensaje informando 

print("Ejercicio 13 (diccionario de frutas)")
fruit_prices = {
    'manzana': 1.5,
    'banana': 0.5,
    'naranja': 0.75,
    'pera': 1.0,
    'uva': 2.0
}

# Preguntar al usuario por una fruta y el número de kilos
fruit = input("Ingrese el nombre de una fruta: ").lower()
kilos = float(input("Ingrese el número de kilos: "))

# Calcular el precio de la fruta ingresada por el usuario
if fruit in fruit_prices:
    total_price = fruit_prices[fruit] * kilos
    print(f"El precio de {kilos} kilos de {fruit} es: {total_price}")
else:
    print("La fruta ingresada no está en el diccionario de precios.")
