
# nombre usuario
while True:
    name=input("Ingrese su nombre ").capitalize()
    if name=="":
        print("No se puede ingresar un nombre vacio ")
    else:
        break
# menu opciones 
while True:  
    options_menu=int(input(f"Usuario {name} indique que juego desea jugar 1)Juego de numeros 2)juego de palabras "))
    if options_menu!=1 and  options_menu!=2:
        print(f"{name} ha ingresado datos incorrectos ")
    else:
        break
#Declaramos variables que vamo sa necesitar mas adelante y las inicializamos en 0
prime_num=0
bigger_even_num=0
amount_prime_num=0
a_amount=0
e_amount=0
i_amount=0
o_amount=0
u_amount=0
# Juego de numeros 

if options_menu == 1 :
    while True :
        while True:
            num=int(input(f"{name} ingrese numeros enteros positivos si ingresa 0 termina la ejecusion "))
            if num>=0:
                break
            else:
                print(f"{name} ingrese un numero entero positivo")
        if num==0:
            break
        elif num%2!=0:
            prime_num+=num
            amount_prime_num+=1
        else:
            if num> bigger_even_num:
                bigger_even_num=num
    average_prime_num=prime_num/amount_prime_num
    print(f"{name} el mayor numero par que ingresaste es {bigger_even_num}  ")
    print(f"{name} el promedio de numero impares es de  {average_prime_num} ")
#Juego de palabras

else:
    
    while True:
        phrase=input(f"{name} ingrese una frase y se mostrara la cantidad de vocales ")
        if phrase!=" ":
            break  
        else:
            print(f" {name} No puede ingresar una respuesta vacia ")
    for l in phrase:
        if l == "a":
            a_amount+=1
        elif l == "e":
            e_amount+=1
        elif l == "i":
            i_amount+=1
        elif l == "o":
             o_amount+=1
        elif l == "u":
            u_amount+=1
    print(f"{name} a ingresado la vocal a : {a_amount}")
    print(f"{name} a ingresado la vocal e : {e_amount}")
    print(f"{name} a ingresado la vocal i : {i_amount}")
    print(f"{name} a ingresado la vocal o : {o_amount}")
    print(f"{name} a ingresado la vocal u : {u_amount}")
