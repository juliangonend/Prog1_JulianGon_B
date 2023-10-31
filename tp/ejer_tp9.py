
from Clases.Person import Person
from Clases.Account import Account
from Clases.Triangle import Triangle
from Clases.Agenda import *



# 1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# •	mostrar(): Muestra los datos de la persona
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
person_1 = Person()
person_1.self_name("Juan")
person_1.self_age(12)
person_1.self_dni(455343234)
person_1.show()
is_legal=person_1.is_legal()
if is_legal:
    print(f"{person_1.name} es mayor de edad")
else:
    print(f"{person_1.name} es mayor de edad")
print(person_1.get_name())


# 2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona)
# y cantidad (puede tener decimales).
# El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
# •	Un constructor, donde los datos pueden estar vacíos.
# •	Los setters y getters para cada uno de los atributos.
# El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# •	mostrar(): Muestra los datos de la cuenta.
# •	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# •	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
account_1= Account("Lopez Marcelo")
account_1.self_quantity(5000)
print(f"El dinero de la cuenta es {account_1.get_quantity()}")
account_1.deposit(5000)
account_1.show()
account_1.withdraw(12000)
account_1.show()
# 3.	Desarrollar un programa que cargue los datos de un triángulo.
# Implementar una clase con los métodos para inicializar los atributos, 
# imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es 
# (equilátero, isósceles o escaleno).
triangle_1= Triangle(13,13,20)
triangle_1.biggest_side()
print(f"El tipo de triangulo es {triangle_1.biggest_side}")


# 4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre
# , el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
# •	Añadir contacto
# •	Lista de contactos
# •	Buscar contacto
# •	Editar contacto
# •	Cerrar agenda
agenda=Agenda()
while True:
    print("Agenda")
    print("1) Añadir contacto")
    print("2) Mostrar lista de  contactos")
    print("3) Buscar contacto")
    print("4) Editar contacto")
    print("5)Cerrar contacto")
    opc=int(input("Ingrese la opcion que desea :"))
    if opc==1:
        new__name=input("Ingrese el nombre del contacto ").capitalize()
        new__tel=int(input("Ingrese del telefono del contacto "))
        new__mail=input("Ingrese del mail del contacto ")
        contact=Contact(new__name,new__mail,new__tel)
        agenda.add_contact_to_list(contact.name,contact.mail, contact.tel)
    if opc==2:
        agenda.list_contact()
    if opc==3:
        name_contact=input("Ingrese el nombre del contacto que desea buscar ").capitalize()
        agenda.search_contact(name_contact)
    if opc==4:
        edit_name=input("Ingrese el nombre del contacto que desea editar ").capitalize()
        edit_tel=input("Ingrese el nuevo numero de telefono ")
        edit_mail=input("Ingrese el nuevo mail ")
        agenda.edit_contact(edit_name, edit_mail,edit_tel)
    if opc==5:
        break
    

