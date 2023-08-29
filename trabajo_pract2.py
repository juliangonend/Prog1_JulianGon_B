import math
# Ejer 1 
ano_computadora= float(input("Ingrese los años que tiene su computadora "))
if ano_computadora<2 :
   
    print("La computadora es nueva ")
else:
    print("La computadora es vieja")
# Ejer2
ano_computadora= float(input("Ingrese los años que tiene su computadora "))
if ano_computadora<0 :
    print(" No se puede ingresar numeros negativos")
if ano_computadora<2 :
    print("La computadora es nueva ")
else:
    print("La computadora es vieja")
# Ejer3
nombre1=input("Ingrese el nombre de la persona 1: ").capitalize()
nombre2=input("Ingrese el nombre de la persona 2: ").capitalize()
if nombre1[0]== nombre2[0]:
    print("Coincidencia")
else:
    print("No coinciden")
# Ejer4
candidato_a="rojo"
candidato_b="verdad"
candidato_c="azul"
candidato_elegido=input("Ingrese el candidato que desea votar : A,B o C :").upper()
if candidato_elegido=="A":
    print(f" Usted a votado por el partido : {candidato_a.upper()}")
elif candidato_elegido=="B":
    print(f" Usted a votado por el partido : {candidato_b.upper()}")
elif candidato_elegido=="C":
    print(f" Usted a votado por el partido : {candidato_c.upper()}")

# Ejer5
letra_ingresada=input("Ingrese una letra ").lower()

if len(letra_ingresada)>1 :
    print("No se puede procesar ya que ingreso mas de una letras")
elif letra_ingresada=="a" or letra_ingresada=="e"or letra_ingresada=="i"or letra_ingresada=="o" or letra_ingresada=="u":
    print(f"la letra {letra_ingresada} es una vocal")
else:
    print(f"la letra {letra_ingresada} es una consonante")

# Ejer 6
ano_bisiesto=int(input("Ingrese una año y se le dira si es bisiesto "))
if ano_bisiesto%400==0 or (ano_bisiesto%4==0 and ano_bisiesto%100!=0 ):
    print(f"El año {ano_bisiesto} es bisiesto")
else:
    print(f"El año {ano_bisiesto} no es bisiesto")

#Ejer 7 
num1=int(input("Ingrese el numero 1:"))
num2=int(input("Ingrese el numero 2:"))
num3=int(input("Ingrese el numero 3:"))

if (num1<num2) and (num1<3):
    print(f"{num1} es el numero menor")
elif (num2<num1) and (num2<3):
    print(f"{num2} es el numero menor")
else:
    print(f"{num3} es el numero menor")

# Ejer8
usuario=input("Ingrese el usuario:  ")
contrasena=input("Ingrese la contraseña:  ")
if usuario=="Gwenevere" and contrasena=="excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

# Ejer9
nombre=input("Ingrese su nombre : ")
sexo=input("Ingrese su sexo M/F : ").upper()
if ( sexo=="F" and nombre[0]<"M") or (sexo=="M" and nombre[0]>"N"):
    print("Corresponde al grupo A")
else:
      print("Corresponde al grupo B")
# Ejer 10
edad = int(input("Ingrese su edad:  "))
if edad<4 :
    print("Entra gratis ya que su edad es menor a 4")
elif edad>=4 and edad<19:
    print("Debe pagar $500")
else :
    print("Debe pagar $1000")

# Ejer 11

pizza=input("Desea una pizza vegetariana ? (SI/NO) : ").upper()

if pizza=="SI":
    print(" Ingredientes disponibles: \n pimiento \n tofu ")
    ingredientes=input(" Ingrediente elegido : ").lower()
else : 
    print("Ingredientes disponibles \n peperoni \n jamon \n salmon ")
    ingredientes=input(" Ingrediente elegido : ").lower()

print(f"la pizza elegida {pizza} es vegetariana y el ingrediente elegido es {ingredientes}")
# Ejer 13
ano_actual = int(input("ingrese el año actual: "))
ano_cualquiera= int(input("ingrese un año cualquiera: "))
suma=ano_actual-ano_cualquiera
resta=ano_cualquiera-ano_actual
if ano_actual > ano_cualquiera :
    print(f"han pasado {suma} desde el año {ano_actual}, hasta el año {ano_cualquiera}")
else:
    print(f"faltan {resta} para el año {ano_actual} hasta el año {ano_cualquiera}")
    
# Ejer13
numero1=int(input("Ingrese numero 1 "))
numero2=int(input("Ingrese numero 2 "))
if numero1<=0 or numero2<=0:
    print("Ingreso números negativos o nulos ")
elif numero2>numero1:
    aux=numero1
    numero1=numero2
    numero2=aux
if numero1%numero2==0 :
    print(" El numero mayor es múltiplo del menor")
else:
    print("El numero mayor no es múltiplo del menor")
# Ejer 14
a= int(input("ingrese el número a: "))
b= int(input("ingrese el número b: "))
print(f"{a}x+{b}=0")
x= -b / a
print(f"x=-{b}/{a}")
print("el resultado de su ecuacion es ",x)

# Ejer15

forma=input("Desea sacar el area de un triangulo o un circulo? ingrese 't' para triangulo y 'c' para circulo: ")
forma.lower
if(forma=="t"):
    base=int(input("ingrese la base del triangulo: "))
    altura=int(input("ingrese la altura del triangulo"))
    area= (base*altura)/2
    print("El area del triangulo es: ", area)
elif(forma=="c"):
    radio=int(input("ingrese el radio del circulo: "))
    area=(math.pi*(radio**2))
    print("el area del circulo es: ", area)
else:
    print("error, el tipo de operacion ingresada no corresponde a lo pedido")
# Ejer16
num_1=int(input("ingrese el primer numero: "))
num_2=int(input("ingrese el segundo numero: "))
operacion=input("Que operacion desea realizar? ingrese '1' para suma, '2' para resta, '3' para multiplicacion y '4' para division: ")
operacion.lower
if(operacion=="1"):
    suma=num_1+num_2
    print("la suma es: ", suma)
elif(operacion=="2"):
    resta=num_1-num_2
    print("la resta es: ", resta)
elif(operacion=="3"):
    multiplicacion=num_1*num_2
    print("la multiplicasion es: ", multiplicacion)
elif(operacion=="4"):
    if(num_1==0 or num_2==0):
        print("no se puede dividir por cero")
    else:
        division=num_1/num_2
        print("la division es: ", division)
else:
    print("la operacion ingresada no cerresponde a ninguna operacion de las pedidas")

# Ejer17
dia=input("Ingrese un dia de la semana: ").lower()
if (dia=="lunes"):
    print("inicio de semana")
elif (dia=="viernes"):
    print("ya casi es fin semana")
elif (dia=="sabado" or dia=="domingo"):
    print("fin de semana")
else:
    print("hoy es: ", dia)

#Ejercicio 18
sal_hora=float(input("Le pediremos por favor que ingrese su salario por hora: "))
mes_hora=float(input("Y sus horas trabajadas durante el mes: "))
hora_t_min=48
hora_extra=mes_hora-hora_t_min
if hora_extra>0 :
    print(f"Horas extras trabajadas: {hora_extra}")
else:
    print("No trabajo horas extras ")
    
sal_total=(hora_t_min*sal_hora)+(hora_extra*sal_hora*1.1)
print(f"Salario total: ${sal_total}")
# Ejer19
cantidad_lapiz=int(input("Ingrese la cantidad de lapices a comprar: "))
costo_lapiz=60

if cantidad_lapiz>=1000:
    sin_descuento=costo_lapiz*cantidad_lapiz
    descuento=(sin_descuento*7)/100
    costo_total=sin_descuento-descuento
    print(f"El monto total a pagar es de: ${costo_total}")
else:
    sin_descuento=costo_lapiz*cantidad_lapiz
    print(f"El monto total a pagar es de: ${sin_descuento}")

# Ejer20
print("Te pediremos que ingreses tus notas: ")
nota_1=int(input("Primer nota: "))
nota_2=int(input("Segunda nota: "))
nota_3=int(input("Tercer nota: "))
nota_4=int(input("Cuarta nota: "))
promedio=(nota_1+nota_2+nota_3+nota_4)/4
if promedio>=6:
    print(f"Aprobaste con: {promedio}")
else:
    print(F"Desaprobaste con: {promedio}")