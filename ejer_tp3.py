# Ejer 1
word=input("Ingrese una palabra y se le mostrara 10 veces : ")
for i in range(5):
    print(word)
    
# Ejer 2 
birthday_year =int(input(" Ingrese su edad : "))

for year in range(birthday_year+1) :
    if year !=0 :
         print(F"{year}")

# Ejer 3 

postitive_num= int(input("Ingrese un numero entero positivo : "))

odd_numbers=0
for e in range(postitive_num+1):
    if e%2!=0 :
        odd_numbers+=1
print(f" La cantidad de numeros impares es :  {odd_numbers}")

# Ejer 4 
num= int(input("Ingrese un numero entero positivo : "))
k=1
for k in range(num +1):
    print(num-k,end=",")
print(" ")
# Ejer 5 
investment=int(input("Ingrese cuanto desea invertir "))
annual_interest= int(input(" Cual es el interes anual ?  "))
year=int(input("Ingrese cuantos años desea invertir "))

for y in range(year):
    annual_earnings=(investment*annual_interest)/100
    investment= investment + annual_earnings
    print( f" En el año { y+1 } el usuario gano un { annual_earnings}")

# Ejer 6
triang=int(input("Ingrese un numero y se hara uin triangulo rectangulo hasta el numero introducido"))

character="*"
for i in range(triang+1):
    for e in range(i):
        print(character,end=" ")
    print(" ")

# Ejer 7 

for i in range (11):
    for e in range(10):
        if e!=0 or i !=0 :
         print(f"{i} x {e} = {i*e}")
        


# Ejer 8
n=int(input("introduce la altura del triangulo (entero positivo):"))

for i in range(1 , n+1 , 2):

    for j in range(i, 0 ,-2):

     print(j, end=" ")

    print(" ")
# Ejer 9

password="contraseña"
password2="2"

while password!=password2:
    password2=input("Ingrese contraseña : ").lower()

# ejer10

primo=True
num1=int(input("Ingrese un numero entero y se mostrara si es primo o no: "))
for i in range(2,num1,1):
    if num1>1:
        if num1%i==0:
            primo=False;
            break

    else:
        break

if primo==True :
     print(f" El numero {num1} es primo")
else:
     print(f"el numero {num1} no es primo")

# Ejer11

word=input("Ingrese una palabra ")
for letter in word[::-1]:
    print(letter)
# Ejer12
frase=input("Ingrese una frase  ")
letter=input("Ingrese una letra  ")

cont_letter=0
for l in frase:
    if letter == l :
        cont_letter+=1

print(f"La cantidad de veces que se repide es de {cont_letter}")
# Ejer13
word_echo=" "
word=""
while word!="salir":
    word=input("Ingrese una palabra ").lower()
    word_echo=word
    print(f"Eco: {word_echo}")
    
# Ejer14

number=int(input("Ingrese un numero   "))
number2=int(input("Ingrese otro numero  "))

for i in range ( number,number2+1):
    if i %2==0:
        print(f"El numero  {i} es  par ")
    else:
        print(f"El numero  {i} es impar")

# Ejer 15 
number = int(input("Ingrese un numero entero mayor que cero"))
while number<0 :
    if number <=0 :
        number= int(input("Ingrese un numero distinto a 0"))
        
for i in range(1,number):
    if number % i == 0 :
        print(f"El  numero {i } es divisor de {number} ")
    else :
        print(F"El numero {i} no es divisor de {number}")

# Ejer 16
amount_num=int(input("Ingrese cuantos numeros se van a introducir "))
negative=0
for i in range(amount_num):
    number=float(input("Ingrese un numero "));
    if number<0 :
        negative+=1

print(f"SE han introducido {negative} numeros negativos ")

# Ejer 17
frase = input("Ingrese una frase ").lower()
repite_word="aeiou"


for i in repite_word:
    if i  in frase:
        print(i)

# Ejer 18 
last1=0
last2=1
print(f"{last1},{last2}",end=",")
for i in range(9):
    new=last1+last2;
    last1=last2
    last2=new
    print(new , end=",")

# Ejer 19 
objetive=int(input( "Ingrese el objetivo a   ahorrar : " ))
save_money=0
while save_money <= objetive:
     money= int(input("Ingrese cuanto dinero desea ahorrar "))
     if money>= 0 :
          save_money+=money
          print(f"Le faltan {objetive-save_money} para cumplir el objetivo ")
     else: 
          print( "No se pueden ingresar numero negativos ")

# Ejer 20
num=1
addition =0 
while num!= 0 :
     num=int(input("Ingrese un numero: "))
     addition+=num;
     
print(f" La suma de los numeros es {addition}")

# Ejer 21
number=1
max=0

while(number !=0):
     number=int(input("Ingrese un numero "))
     if number > max :
          max=number

print(f" El mayor numero es {max}")

# Ejer 22
number=0
addition=0 
addition_2=0 
while(number!=-1): 
     number=int(input("Ingrese un numero, para salir ingrese '-1': ")) 

     if (number>=0): 



          for n in str(number): 

               n=int(n) 
               addition+=n 
               print(addition)
     else: 
          print("el numero ingresado debe ser positivo") 
     if (number % 2==0):
               addition_2+=1 

print("la cantidad de numeros ingresados pares son: ", addition_2)
# Ejer 23
amount_enter=1
while amount_enter!=0:
     amount_enter= float(input("Ingrese el monto de la compra: "))
     if amount_enter==0:
          print("Termino la carga de los montos ")
# Ejer 24 
print("Ingreese los montos, para calcular el total de su compra")
total_amount = 0
while True:
    amount = float(input("Ingrese el monto(Ingrese un valor 0 para salir): "))

    if amount < 0:
        print("Monto inválido. Por favor, ingrese un nuevo monto.")
        continue
    
    total_amount += amount
    if total_amount > 1000:
        total_amount *= 0.9
    if amount == 0:
        break
print("El total a pagar es: $" + str(total_amount))
#25
number = int(input("Ingrese un número entero positivo: "))
factorial = 1
if number < 0:
    print("El número ingresado debe ser positivo.")
elif number == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, number + 1):
        factorial *= i
    
    print("El factorial de", number, "es",factorial)
          