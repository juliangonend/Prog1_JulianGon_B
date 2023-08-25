# Ejer 1 
base=float(input("Ingrese la base del rectangulo "))
altura=float(input("Ingrese la altura del rectangulo "))
perimetro=2*base + 2* altura
area = base *altura
print(f"El perimetro es : {perimetro}")
print(f"El area es : {area} ")

# Ejer 2 
cate1=float(input("Ingrese el cateto 1 : "))
cate2=float(input("Ingrese el cateto 2 : "))
hipotenusa= (cate1**2+cate2**2 )** (1/2)
print(f"La hipotenusa es : {hipotenusa}")


#Ejer3
num1= float(input("Ingrese un numero "))
num2= float(input("Ingrese otro numero "))
suma= num1+num2
resta = num1-num2
divi= num1/num2
multi= num1*num2
print(f" suma = {suma}")
print(f" resta = {resta}")
print(f" division = {divi}")
print(f" multiplicasion= {multi}")

#Ejer 4
farenheit= float(input("Ingrese la temperatura en grados farenheit: "))
cels=(farenheit-32)*5/9
print(f"Los grados en celsious son {cels}")

# Ejer5
# a
nombre=input("¿Cual es tu cancion favorita")
# b 
precio= int(input(" Precio : "))
total= precio + (precio * 0.1)
# c
edad = int ( input(" Edad : "))
print(f" tu edad es : {edad}")
# d 
edad2= int(input("Edad : "))
edad18=bool(edad2==18)
print(f" veamos  si tu edad es 18 : {edad18}")

# Ejer6
val1=float(input( " Ingrese el primer valor a promediar: "))
val2=float(input( " Ingrese el segundo valor a promediar: "))
val3=float(input( " Ingrese el tercero valor a promediar: "))

promedio= (val1+val2+val3)/3
print(f"El promedo de los numeros es : {promedio}")

# Ejer7
minutos= int(input("Ingrese la cantidad de minutos"))
horas= minutos/60

print(f" La cantidad de horas es : {horas}")

# Ejer8

sueldo= int(input ( "Ingrese su sueldo base: "))
ventas= int(input( "Ingrese cantidad de ventas : "))
dinero_extra= (sueldo*(10*ventas))/100
sueldo_final= sueldo + dinero_extra
print(f" Su sueldo final es de : {sueldo_final}")

# Ejer9
compra=int(input(" Ingrese el total de su compra "))
descuento= (compra*15)/100
compra_desceuento= compra-descuento
print(f"Su total con el descuento es de : {compra_desceuento}")

#Ejer10

parcial1= float(input("Ingrese la nota del primer parcial : "))
parcial2= float(input("Ingrese la nota del segundo parcial : "))
parcial3= float(input("Ingrese la nota del tercero parcial : "))
examen_final= float(input( "Ingrese la nota del examen final : "))

prom_parciales=(parcial1+parcial2+parcial3)/3
prom_parciales=prom_parciales*0.55
prom_examen= examen_final*0.30
prom_trabajo_final=  examen_final *0.15
nota_final= prom_parciales+ prom_parciales+ prom_examen
print(f" Su calificacion final de la materia es {int(nota_final)}")

# Ejer11
print("Vamos a tomar la distancia de dos números :")
num1=float(input("Ingrese el primer numero"))
num2=float(input("Ingrese el segundo numero"))

distancia=abs(num1-num2)
print(f"La distancia entre los dos numeros es de {distancia}")

# Ejer12
print("Vamos a calcular la raíz cuadrada y cubica del número que elijas ")
numero_r=float(input("Ingresa el número: "))
raiz_cubica_num=numero_r**(1/3)
raiz_cuadrada_num=numero_r**(1/2)
print(f"La raiz cuadrada de {numero_r} es de {raiz_cuadrada_num} y su raíz cúbica es de {raiz_cubica_num}")

# Ejer13
num= input("ingrese un número: ")
inverso= num[::-1]
print(f"el numero inverso es: {inverso}")

# Ejer14
a = int(input("ingrese el primer número: "))
b = int(input("ingrese el segundo número: "))
aux=a
a=b
b=aux
print(f"a: {a}")
print(f"b: {b}")
# Ejer15

print("Ingrese la hora, minutos y segundos de salida")
hora_salida= int(input(print("Ingrese la hora :")))
min_salida= int(input(print("Ingrese los minutos ")))
seg_salida= int(input(print("Ingrese los segundos ")))
seg_del_viaje= 5415
print("La hora de llegada va a ser:")
seg_horas= hora_salida*3600
seg_min= min_salida*60
seg_total= seg_salida+seg_horas+seg_min+seg_del_viaje
hora_tot= int(seg_total/3600)
seg_total-=(hora_tot*3600)
min_tot= int(seg_total/60)
seg_total-= (min_tot*60)
print(f"{hora_tot}:{min_tot}:{seg_total}")

# Ejer16

nombre =input( " Ingrese su nombre ")
primer_apellido =input( " Ingrese su primer_apellido ")
segundo_apellido =input( " Ingrese su segundo_apellido ")
inicales= (nombre[0]+primer_apellido[0]+segundo_apellido[0]).upper()
print (inicales )

#Ejer17

usuario =input( " Ingrese su nombre ")
print(f"Ahora estás en la matrix , [{usuario}]")

# Ejer18

cena = float(input("Ingrese el costo de la cena "))
servicio=cena%6.2
propina=cena%10
cena+=  propina + servicio 

# Ejer19

# dd/mm/aaaa

import datetime

dia=int(input("Ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
anio=int(input("Ingrese su anio de nacimiento: "))

# Ejer20

dia=int(input("Ingrese su dia de nacimiento: "))
mes=int(input("Ingrese su mes de nacimiento: "))
anio=int(input("Ingrese su año de nacimiento: "))
fecha=datetime.date(anio, mes, dia).strftime('%d/%m/%Y')
print(fecha)

#Ejer21

km_por_litro=int(input("cuantos kilometros puede recorrer su vehículo con 1 litro de combustible: "))
km_a_recorrer=int(input("cuantos kilometros van a recorrer?: "))
capacidad_del_tanque=int(input("de cuantos litros es su tanque?: "))
tanques=(km_a_recorrer/km_por_litro)/capacidad_del_tanque
print("necesitan ", tanques, " tanques de combustible")
