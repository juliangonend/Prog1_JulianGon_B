# Ejer 1
x=0
while x<=30:
    x+=1
    if x== 4 or x==6 or x==10 :
        print(f"The loop skip the value {x} for x")
    elif x==15: 
        print(f"The execution of the loop was broken when x was {x}")
        break
    else:
        print(f"{x}")
   
# Ejer 1.2
line_secuence="a"

while line_secuence!="":
    line_secuence=input("Ingrese una frase : ").upper()
    print(line_secuence)
    
# Ejer 2
operations = "a"
deposit=0
retire=0
acount=0
while operations!="":
    operations=input("Ingrese D si desea depositar o R si desea retirar luego ingrese el monto  ").upper()
    if operations=="":
        break
    elif operations[0]=="R":
            retire=int(operations[1:])
            print(retire)
            if (acount-retire)<0:
                print(" No puede retirar saldo negativo ")
            else:
                acount-=retire
    elif operations[0]=="D":
        deposit=int(operations[1:])
        print(deposit)
        acount+=deposit
print (f"Cuenta bancaria : {acount}")


# Ejer3

num=1 
pair=False
amount_prime_num=0
while num!=0:
    num=int(input("Ingrese un numero mayor que 1 si elige 0 termina la ejecusion "))
    pair=False
    if num>1:
        for i in range(2,num):
         if num%i== 0 : 
            pair=True;
            break
        amount_prime_num= amount_prime_num+1 if pair==False else amount_prime_num
    
print(f"La cantidad de numero primos son {amount_prime_num}")
# Ejer 4 

start_year=int(input("Ingrese un donde desea empezar la ejecusion año"))
finish_year=int(input("Ingrese el año donde desea finalizar la ejecusion "))
leap_year=0
for year in range(start_year,finish_year+1):
    if (year%4==0 and year%100!=0 and year%10==0) or (year%400==0):
        leap_year+=1
        print(f" El año {year} es bisiesto y multiplo de 10")

# Ejer 5 

for i in range(1,21):
    if i%2!=0 :
        continue
    print(f"El numero {i} es par ")

# Ejer 6 

numbers6=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
number=0
choose=int(input("Ingrese un numero del 10 al 25: "))

for i in numbers6:
    
    if choose==20:
        number=numbers6.index(choose)
        print("Encontraste el numero! ")
        break
    else:
        print("No es el numero que se esta buscando")
        choose=int(input("Ingrese otro numero: "))


# Ejer7
options=1
while True:
    options=int(input("Ingrese 1) 2) 3) 0)para salir "))
    if options==1:
        print("Ü")
    elif options==2:
        print("Ñ")
    elif options==3:
        print("E")
    elif options==0:
        break
    else:
        print(options)