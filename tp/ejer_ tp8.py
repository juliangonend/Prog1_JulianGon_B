from func_tp8 import * 

# 1.	Escribir una función que reciba un número positivo n y 
# devuelva la cantidad de dígitos que tiene.
num=1000
amount_digit=total_digit(num)
print(amount_digit)

# 2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.

n,b=5,125
power=is_power_of(n,b)
print(power)

# 3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a. Ejemplo:
string1,string2="tri tri tri tri ","tri"
arr=[]
positions=find_position(string1,string2,0,arr)
print(positions)

# 4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) q
# ue determinen la paridad del numero natural dado, conociendo solo que:
num=11
print(f"El numero {num}  {is_number_even(num)}")
print(f"El numero {num}  {is_number_odd(num)}")
# •	1 es impar.
# •	Si un número es impar, su antecesor es par; y viceversa.

# 5.	Escribir una función recursiva que encuentre el mayor elemento de una lista.
list=[1,32,43,2,3]
biggest_num=list[0]
biggest_num=find_biggest_num(list,1,biggest_num)
print(biggest_num)
# 6.	Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces.
# Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])
list=[1,1,43,2,3]
num=2
new_arr=[]
print(replicate_list(list,new_arr,num))

# 7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
# ● El programa debe pedir al usuario que ingrese un número n, y un número d,
# ● Luego debe calcular el valor de K(n, p) usando una función recursiva,
# ● Debe imprimir el resultado de K(n, p)

n=10
p=12
resultado = K(n, p)
print(f"El resultado de K({n}, {p}) es: {resultado}")
# 8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.
print(pascal_triang(5,3))
# 9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k,
# e imprima todas las posibles cadenas de longitud k 
# formadas con los caracteres dados (permitiendo caracteres repetidos).
print("(9)Combinaciones")
list9 = ['a', 'b', 'c']
k = 4
result= combinations(list9, k)
print(f"Todas las combinaciones de longitud {k} son:")
for combo in result:
    print(combo)
# 10.	La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo). 
# Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). 
# Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.
# Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva el ancho y el largo de la hoja A(N) 
# calculada recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base. La función debe devolver el ancho y el largo -en ese orden- en una tupla.

n= 1
wide, long=measurements_sheet_A(n)
print(f"Las medidas de A{n} son: {wide} mm x {long} mm")