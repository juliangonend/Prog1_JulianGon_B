# Ejer 1
def  verify_dni(dni):
    if len(dni)>=7 and len(dni)<=8:
        return True
    else:
        return False
# Ejer 2
def len_last_word(phrase):
    separate_word=phrase.split()
    if separate_word:
        last_word=separate_word[-1]
        return len(last_word)
    else:
        return 0
# Ejer 3
def create_user_name(full_name,dni):
  
    if full_name!=None:
            name=full_name[0]
            adreess=full_name[-1]
            len_adreess=str(len(adreess))
            print(name)
            user_id=name+len_adreess+dni[:3]
            return user_id
    else:
        return "incorrecto"
# Ejer 4
def is_multiple(n1,n2):
    if n2%n1==0:
        return "es multiplo"
    else:
        return "no es multiplo"
# Ejer 5
def calculate_medioum_temp(min,max):
    medioum=float((min+max)/2)
    return (medioum)
#Funcion ejercicio 6
def add_spaces(text):
    result = ''
    for letter in text:
        result += letter + ' '
    return result
#Funcion ejercicio 7
def maximum_and_minimum(list):
    maximum = max(list)
    minimum = min(list)
    return maximum, minimum
#Funcion ejercicio 8
import math
def area_and_perimeter(radio):
    area = math.pi * radio**2
    area2=round(area,2)
    perimeter = 2 * math.pi * radio
    perimeter2=round(perimeter,2)
    return area2, perimeter2
#Funcion ejercicio 9
def login(username9, password9,attemps9):
    if username9 == "usuario1" and password9 == "asdasd":
        return True
    else:
        attemps9+=1
        return False, attemps9
#Funcion ejercicio 10
def apply_discount(cart):
    total = 0
    for product, price in cart.items():
        discount = price * 0.10 # Multiplica por 0.01 para obtener el porcentaje en decimal
        final_price = price - discount
        total += final_price
    return abs(total)
#Funcion ejercicio 11
def apply_funcion(funcion, list11):
    return [funcion(element) for element in list11]

def multiply_by_two(num):
    return num*2
#Funcion ejercicio 12
def count_lenght_words(phrase):
    # Dividir la frase en palabras utilizando split()
    words = phrase.split()
    dictionary = {}
    for i in words:
        dictionary[i] = len(i)

    return dictionary
#Funcion ejercicio 13
def module_vector(vector13):
    sum_squares = sum(x**2 for x in vector13)
    module13 = math.sqrt(sum_squares)
    module13_1=round(module13,3)
    return module13_1
#Funcion ejercicio 14
def prime_number_or_not(number):
    if number<2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i ==0:
            return False
    return True
#Funcion ejercicio 15
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
def calculate_factorial(n):#en ningun momento la variable n es ejecutada, solamente se la llama para que se ejecute correctamente el programa y no marque errror.
    read = 0
    while True:
        number = int(input("Ingresa un número (-1 para salir): "))
        if number == -1:
            break
        else:
            print("El factorial de", number, "es:", factorial(number))
        read+=1
    print("El total de numeros ingresados es: ",read)
#Funcion ejercicio 16
# reutilizada en ejer 17
def amount_digit_repeat(num,digit):
    repeat=0
    for i in num:
        if i==digit:
            repeat+=1
    return repeat

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print(f" {num} / {i}")
            return False
        
    return True

def sum_digit(num):
    str_num=str(num)
    digit_sum=0
    for i in str_num :
        digit_sum+= int(i)
    
    return digit_sum