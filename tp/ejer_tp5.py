from funciones_tp5 import *

# Ejercisio 1 


    
dni=input("Ingrese el dni ")

print(f"El dni es  {verify_dni(dni)}")
# Ejercisio 2

phrase=input("Ingrese una frase ")
print(f"la longitud de la ultima frase es de {len_last_word(phrase)}")
# Ejercisio 3

while True:
        dni=input("Ingrese un dni :")
        correct_dni=verify_dni(dni)
        if correct_dni:
            break
        else:
            print("El dni ingresado es incorrecto ingrese uno entre 7 y 8 cifras")
full_name=[]
while True:
    print(f"Ingresa el nombre del socio si desea terminar la ejecusion") 
    print("ingrese una respuesta vacia para terminar la ejecusion ")
    name=input()
    if name=="":
        break
    else:
        full_name.append(name.capitalize)


user_id=create_user_name(full_name,dni)
print(f"El usuario es {user_id}")


# Ejercisio 4
# 4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que 
# reciba los dos números, y devuelve si el primero es múltiplo del segundo.


num1=int(input("Ingresa un numero "))
num2=int(input("Ingresa un multiplo del primer numero "))
verify_number=is_multiple(num1,num2)
print(f"{num1} {verify_number} de {num2}")

# Ejercisio 5 
# 5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Crear un programa principal, que utilizando la función anterior,
# vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días que se van a introducir.

min_temp=int(input("Ingrese la temperatura minima"))
max_temp=("Ingrese la temperatura maxima")
medioum=calculate_medioum_temp(min_temp,max_temp)
print(f"La tempetura media entre la minima :{min_temp} y la maxima: {max_temp} es de : {medioum}")

# Ejer6
# 6.	Crea una función que reciba como parámetro un texto y devuelve 
# una cadena con un espacio adicional tras 
# cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
# Crea un programa principal donde se use dicha función.



print("Le agregaremos espacios a tu texto.")
text= input("Ingresa un texto: ")
result = add_spaces(text)
print(result)
#Ejercicio7
numbers7 = []
print("Calcularemos el maximo y el minimo de una lista de nuneros.")
while True:
    num=input("Ingresa un numero: ")
    numbers7.append(float(num))
    option = input("Ingresa enter para salir///Ingresa cualquier caracter para seguir ")
    if option == "":
        break
maximum, minimum = maximum_and_minimum(numbers7)
print("El máximo es:", maximum)
print("El mínimo es:", minimum)

#Ejercicio8
print("Calcularemos el area y el perimetro de una circunferencia.")
radio8 = float(input("Ingresa el radio de la circunferencia: "))
area, perimeter= area_and_perimeter(radio8)
print("El área de la circunferencia es:", area)
print("El perímetro de la circunferencia es:", perimeter)

#Ejercicio9
print("Logueo:")
attemps = 0
while attemps < 3:
    username = input("Nombre de usuario: ")
    password = input("Contraseña: ")
    res, attemps= login(username, password, attemps)
    
    if res:
        print("¡Inicio de sesión exitoso!")
        break
    else:
        print("Nombre de usuario o contraseña incorrectos. Intenta de nuevo.")
if attemps == 3:
    print("Has excedido el número máximo de intentos.")

#Ejercicio10
print("Calcularemos los descuento a aplicar al carrito de compras")
shopping_cart={
    "lechuga": 123,
    "tomate": 212,
    "papa": 350,
    "zanahoria":220
}
shopping_cart2={
    "gomitas": 123,
    "caramelos":212,
    "chocolate": 150
}
shopping_cart3={
    "leche": 1200,
    "queso":660,
    "yogurt": 321
}

#final_price= apply_discount(shopping_cart)
#final_price= apply_discount(shopping_cart2)
final_price= apply_discount(shopping_cart3)
print(f"El precio final de la compra es: {final_price}$" )

#Ejercicio11
print("Aplicaremos funciones sobre una lista")
numbers11=[12,23,1,4,100,50,31]
print("La lista es:")
print("[",end="")
for i in numbers11:
    print(f"{i},", end=" ")
print("]")

result=apply_funcion(multiply_by_two,numbers11)
print("El resultado de multiplicar los numeros de la lista 'x2' es: ",result)

#Ejercicio 12
#phrase = "Mucho gusto un placer en conocerte"
#phrase2="Mi comida favorita son las papas fritas"
phrase3="No me gusta la comida picante"
print("Contaremos la cantidad de letras que tiene cada palabra de la frase: '",phrase3,"'")
result12 = count_lenght_words(phrase3)
print("La frase dividida por  palabra es: ")
print(result12)

#Ejercicio 13
print("Vamos a calcular el modulo de un vector")
#vector13 = [3, 4]
vector13_2=[4,5]
print("El vector es: ",vector13_2)
module = module_vector(vector13_2)
print(f"El módulo del vector {vector13_2} es: {module}")

#Ejercicio 14
print("Le pediremos que ingrese un numero entero para saber si es primo o no ")
number14=int(input("Numero: "))
if prime_number_or_not(number14):
    print("El numero ingresado es primo")
else:
    print("El numero ingresado no es primo")

#Ejercicio 15
print("Vamos a calcular los factoriales de cada numero que ingreses: ")
num=0
calculate_factorial(num)#se ingresa una variable que no va a ser utilizada

#Ejercicio 16

num=input("Ingrese un numero ")
digit=input("Ingrese un digito y se mostrara la cantidad de ocurrencias")

repeat=amount_digit_repeat(num,digit)
print(f" El digito {digit} se repitio {repeat} veces ")

#Ejercisio 17
prime_num=True
while True:
    num=int(input("Ingrese un numero primo si no se cortara la ejecusion "))
    prime_num=is_prime(num)
    if prime_num:
        digit_sum=sum_digit(num)
        print(f"La suma de los digitos es de {digit_sum}")
        digit=input("Ingrese un digito y se mostrara la cantidad de veces que se repite ")
        str_num=str(num)
        digit_repeat=amount_digit_repeat(str_num,digit)
        print(f"La cantidad de veces que se repite el digito {digit} es de {digit_repeat}")
    else:
        break