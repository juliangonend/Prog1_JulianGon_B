
from metodosOrden import *  
# 1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.


number_array = [14, 345, 2, 62, 32, 114, 143]
print(f"Array Desordenado : {number_array}")
bubble_sort(number_array)
print("Arreglo ordenado:")
print(f"Array ordenado : {number_array}")

# 2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.
word_arra=["hola","Juan","arbol","otorrino","futbol","gato"]

print(f"las palabras del array son {word_arra}")
seleccion_sort(word_arra)
print(f"El array ordenado queda como {word_arra}")
# 3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.
book_list=[
    {"titulo":"Harry Poter","autor":"J. K. Rowling","anio_pub":1997,"genero":"ficcion"},
    {"titulo":"Payaso Plin Plin","autor":"Jaimito","anio_pub":1923,"genero":"comedia"},
    {"titulo":"Harry Popoter","autor":"El tio Luis","anio_pub":2023,"genero":"terror"},
    {"titulo":"Futbolito","autor":"Bielsa","anio_pub":2005,"genero":"deporte"},
    {"titulo":"El Despertar","autor":"Mariela Fernandez","anio_pub":2013,"genero":"novela"}
]

print(f"Libros sin ordenar ")
for i in book_list:
    print(i)
autor_sort(book_list)
print(f"Libros ordenados por autor ")
for i in book_list:
    print(i)
# 4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud.
# Puedes utilizar el método de ordenamiento de inserción.
string_arra=["hola","como estas","cirujano","papas a la crema","uno","no"]

print(f"Lista desosrdenada {string_arra}")
len_insert_sort(string_arra)
print(f"Lista Ordenada {string_arra}")
# 5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.
print(f"Ascendente :  {number_array}")
des_bubble_sort(number_array)
print(f"Descendente :  {number_array}")
# 6.	Escribe un programa que tome una lista de números enteros 
# y ordene la lista utilizando el algoritmo de ordenamiento por conteo.
number_list=[3,2,4,9,6,4,1]
number=count_sort(number_list)
print(f"Lista de numeros ; {number}")
# 7.	Crea una lista que contenga tanto números como cadenas de caracteres. 
# Escribe un programa que ordene esta lista de manera que primero estén los números
# ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.
list= ["Manzana", 42, "Gato", 3,"Arbol", "Python", 7, "Libro", 99, "Soleado", "Montaña",33, "Pelota", 1,43,"Elefante"]

order_by_type(list)
print(f"{list}")
# 8.	Implementa el algoritmo de ordenamiento Merge Sort 
number_array = [14, 345, 2, 62, 32, 114, 143]
number_array = merge_sort(number_array)
print (number_array)