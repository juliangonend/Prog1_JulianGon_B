import pytest
from funciones_tp5 import *  
# ejer1
@pytest.mark.parametrize("a, b", [
    ("1234567", True),
    ("124325672", False),
    ("233", False),
])
def test_verify_dni(a, b):
    assert verify_dni(a) == b
# ejer2
@pytest.mark.parametrize("phrase,len_word",[ 
    ("hola como estas",5),
    ("tres tistres tigres",6),
    ("My nombre es Julian",6),])
def test_len_last_word(phrase,len_word):
    assert len_last_word(phrase)==len_word


# Ejercisio 3
@pytest.mark.parametrize("full_name,dni,user_name",[ 
        (["Julian","Gonzalez"],"1234566","Julian8123"),
        (["Laura","Mar"],"7654321","Laura3765"),
        #([" "],"12345621","incorrecto")
        ])

def test_create_user_name(full_name,dni,user_name):
    assert create_user_name(full_name,dni)==user_name

# Ejer4

@pytest.mark.parametrize("n1,n2,result",[(2,4,"es multiplo"),
                                         (3,6,"es multiplo"),
                                         (4,5,"no es multiplo")])
def verify_is_multiple(n1,n2,result):
    assert is_multiple(n1,n2)==result


# #Ejer5

@pytest.mark.parametrize("min,max,medioum",[(10,20,15),
                                         (3,6,4.5),
                                         (4,8,6)])
def test_calulate_medioum_temp(min,max,medioum):
    assert calculate_medioum_temp(min,max)==medioum
    
#Ejercicio 6
@pytest.mark.parametrize("text6, value6",[
    ("Hola","H o l a "),
    ("Hola, tu","H o l a ,   t u "),
    ("Como estas","C o m o   e s t a s "),
])
def test_add_spaces(text6,value6):
    assert add_spaces(text6)==value6
#Ejercicio 7
@pytest.mark.parametrize("numbers7, max, min",[
    (([23,4,5]),23,4),
    (([12,9,-1]),12,-1),
    (([230,0,1]),230,0),
])
def test_max_min(numbers7, max, min):
    #Se llama a la funcion pasando la lista de los numeros
    maximum, minimum = maximum_and_minimum(numbers7)
    assert maximum==max, minimum==min

#Ejercicio 8
@pytest.mark.parametrize("radio8, area8, perimeter8",[
    (123,47529.16,772.83),
    (12,452.39,75.4),
    (3,28.27,18.85),
])
def test_area_and_perimeter(radio8,area8,perimeter8):
    area, perimeter = area_and_perimeter(radio8)
    assert area==area8, perimeter==perimeter8

#Ejercicio 9
@pytest.mark.parametrize("username, password, attempts, value9",[
    ("wanter","onetwo",0, False),
    ("usuario1","asdasd",0,True),
    ("hello","1234",2, False),
])
def test_login(username,password,attempts, value9):
    login(username, password, attempts)
    if value9==True:
        assert login(username,password,attempts)
    else:
        assert login(username,password,attempts)==(value9,(attempts+1))

#Ejercicio 10
@pytest.mark.parametrize("shopping, value9",[
    ({"lechuga": 123, "tomate": 212, "papa": 350, "zanahoria": 220}, 814.5),
    ({"gomitas": 123, "caramelos": 212, "chocolate": 150}, 436.5),
    ({"leche": 1200, "queso": 660, "yogurt": 321}, 1962.9),
])
def test_apply_discount(shopping,value9):
    assert apply_discount(shopping)==value9

#Ejercicio 11
@pytest.mark.parametrize("funcion11,list11,res11",[
    (multiply_by_two, [12, 23, 1, 4, 100, 50, 31], [24, 46, 2, 8, 200, 100, 62]),
    (multiply_by_two, [121, 10, 44, 312], [242, 20, 88, 624]),
    (multiply_by_two, [3, 13, 21], [6, 26, 42]),
])
def test_funcion(funcion11,list11,res11):
    assert apply_funcion(funcion11, list11) == res11

#Ejercicio 12
@pytest.mark.parametrize("phrase, result",[
    ("Mucho gusto un placer en conocerte",{'Mucho': 5, 'gusto': 5, 'un': 2, 'placer': 6, 'en': 2, 'conocerte': 9}),
    ("Mi comida favorita son las papas fritas",{'Mi': 2, 'comida': 6, 'favorita': 8, 'son': 3, 'las': 3, 'papas': 5, 'fritas': 6}),
    ("No me gusta la comida picante",{'No': 2, 'me': 2, 'gusta': 5, 'la': 2, 'comida': 6, 'picante': 7})
])
def test_count_lenght_words(phrase,result):
    assert count_lenght_words(phrase)==result

#Ejercicio 13
@pytest.mark.parametrize("vector, module",[
    (([4,5]),6.403),
    (([6,3]),6.708),
    (([2,1]),2.236),
])
def test_module_vector(vector, module):
    assert module_vector(vector)==module

#Ejercicio 14
@pytest.mark.parametrize("number14, res14",[
    (1,False),
    (2,True),
    (-10,False),
    (59,True),
    (0,False),
])
def test_prime_number_or_not(number14,res14):
    assert prime_number_or_not(number14)==res14

#Ejercicio 15
@pytest.mark.parametrize("factorial15,res15",[
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_calculate_factorial(factorial15,res15):
    assert factorial(factorial15)==res15

#Ejercicio 16

@pytest.mark.parametrize("num,digit,repeat",[ 
    ("212","2",2),
    ("3521","3",1),
    ("0000","2",0),])


def test_amount_digit_repeat(num,digit,repeat):
    assert amount_digit_repeat(num,digit)==repeat
    
    
# Ejercisio 17
@pytest.mark.parametrize("num, expected", [
    (2, True),     
    (3, True),     
    (4, False),    
    (5, True),   
    (16, False),  
    (17, True),   
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected
    
@pytest.mark.parametrize("num, expected", [
    (12345, 15),   
    (9876, 30),    
    (0, 0),        
    (111, 3),      
    (999999, 54),  
])
def test_sum_digit(num, expected):
    assert sum_digit(num) == expected