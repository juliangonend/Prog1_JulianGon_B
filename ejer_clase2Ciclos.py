
# Ejercisio 1
# Declaramos el abecedario 
abecedario="abcdefghijklmnñopqrstuvwxyz"
i=0
# Le pedimos al usuario cuantos lugares quierer correr el código
corrimiento=int(input("Ingrese cuanto desea correr el codigo "))
# HACEMOS UN FOR PARA QUE SE REPITA 5 VECES
for i in range(5):
    #Ingresa la palabra que desea encriptar
    palabra=input("Ingrese la frase que desea encriptar ")
    #Declaramos palabra_encriptada en un string vacío para usarlo más adelante 
    palabra_encriptada=""
    #for para  recorrer la palabra
    for letra in palabra:
        #Si la letra esta en mayuscula la cambiamos a minuscula para que la reconozca el programa al verificar
        mayuscula=False
        if letra.isupper():
                letra=letra.lower()
                mayuscula=True
        #Si la letra esta en el abecedario la cambiamos
        if letra in abecedario:
            indice=abecedario.find(letra)
            indice=(indice+corrimiento)%27
            letra=abecedario[indice]
        #Si la letra estaba en mayuscula la volvemos a dejar en mayuscula luego de codificarla
        letra= letra.upper() if mayuscula==True else letra
        #Guardamos la letra cambiada
        palabra_encriptada+=letra
    #Imprimimos 
    print(palabra_encriptada) 
   
# Ejercisio 2
#Declaramos las variables que vamos a utilizar 
num=1
par=0
impar=0
resto=0
#mientras para repetirlo hasta que el usuario ingrese 0
while num!=0 :
    #Pedimos el numero
    num=int(input("Ingrese numeros y se le dira si es par o impar y si es == 0 termina la ejecusion : "))
    i=abs(num)
    #Mientras para descomponer el numero unidad por unidad mientras sea mayor a 0
    while i>0:
        if i>10:
            #Sacamos la unidad del numero
            resto=int(i%10)
            # lo guardamos sin la unidad 
            i=i/10
        else:
            resto=i
        #Si ya el numero es menor a 10 guardamos el numero 0 para terminar la ejecusion
            i=0
        #pasamos el numero de int a float para que no este con .
        resto=int(resto)
        #Verificamos si es par o impar
        if resto%2==0:

            par+=1
        else:
            impar+=1
#Imprimos cuantos pares y impares hubo
print(f"La cantidad de pares es {par} ")
print(f"La cantidad de impares es {impar} ")
        