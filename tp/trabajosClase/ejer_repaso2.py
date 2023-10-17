import random
import sys

# # Ejer 1
# # . Realizar un programa que pida una frase o palabra y si la frase o palabra es de 4 caracteres de largo, el
# # programa le sumará un signo de exclamación al final, y si no es de 4 caracteres el programa le sumará un
# # signo de interrogación al final. El programa mostrará después la frase final.
# # frase=input("Ingrese una frase ")
# # if len(frase)==4:
# #     frase+="?"
# # else:
# #     frase+="!"
    
# # print(frase)
# # Ejer 2
# # 2. Crea un juego donde el programa elija una palabra al azar de una lista y el usuario tenga que adivinarla letra
# # por letra. Proporciona un número limitado de intentos y utiliza un bucle while para controlar el juego.

# aleatory_words=["casa","arbol","perro","banana","conejo","espada"]
# random_num=random.randint(0,len(aleatory_words))
# user_frase=""
# user_attempts=5

# for l in aleatory_words[random_num]:
#     while True:
#         print(f" Posee {user_attempts} intentos")
#         print(f"A ingresado correctamente {user_frase}")
#         user_letter=input(f"Ingrese la letra {len(user_frase)+1} que desea adivinar ")
        
#         if user_letter==l:
#             user_frase+=user_letter
#             break
        
#         else:
#             if user_attempts==0:
#                 print(f"Perdio la palabra a adivinar era {aleatory_words[random_num]}")
#                 sys.exit()
#             else:
#                 user_attempts-=1
#             print("Letra incorrecta ingresela nuevamente")
# print(f" Felicitaciones adivino la palabra {user_frase}")

# # Ejer 3 
# # 3. Escribe un programa que cuente cuántas palabras hay en una cadena de texto ingresada por el usuario.
# frase=input("Ingrese una cadena de texto y se devolveran cuantas palabras hay ")
# if len(frase)>0:
#     before=False
#     cont_words=1
#     for i in frase:
#         if i==" ":
#             if before:
#                 continue
#             else:
#                 cont_words+=1
#                 before=True
#         else:
#             if i!="":
#                 before=False
#     print(f" la cantidad de palabras de la frase {frase} es de {cont_words}")

# Ejer 4
# 4. Una empresa quiere pagar a sus empleados por la asistencia de lunes a viernes y un adicional por las
# horas trabajadas los domingos en tareas especiales.
# ✔ El empleado asistió todo el mes, además entre 3 y 5 horas los domingos, adiciona el 3 % del sueldo.
# ✔ Si asistió todo el mes y entre 6 y 10 horas los domingos, adiciona el 10 %.
# ✔ No asistió todo el mes y entre 3 y 10 horas los domingos, adiciona el 2 %.
while True:
    employee=input("Ingrese si/no si asistio todo el mes ").lower()
    if employee=="si" or employee=="no":
        break
salary_employee=int(input("Ingrese su sueldo  del mes "))
while True:
    hours_extra=int(input("Ingrese cuantas horas extra trabajo el domingo "))
    if hours_extra<=10:
        break
    else:
        print(" Puede cargar hasta 10 horas extra")
   
if employee=="si":
    if hours_extra>=3 and hours_extra<=5:
        additional_salary=salary_employee*0.03
        total_salary=additional_salary+salary_employee
        print(f"El salario de este empleado tiene un incremento del 3% y queda en un total de {total_salary}")
        
    if hours_extra>=6 and hours_extra<=10:
        additional_salary=salary_employee*0.10
        total_salary=additional_salary+salary_employee
        print(f"El salario de este empleado tiene un incremento del 10% y queda en un total de {total_salary}")
else:
       if hours_extra>=3 and hours_extra<=10:
        additional_salary=salary_employee*0.02
        total_salary=additional_salary+salary_employee
        print(f"El salario de este empleado tiene un incremento del 10% y queda en un total de {total_salary}")
    
# 5. Leer 2 números; si son iguales que los multiplique, si el primero es mayor que el segundo que los reste y si
# no que los sume.
num1=int(input("Ingrese un numero "))
num2=int(input("Ingrese otro numero "))
if num1==num2:
    operations=num1*num2
    print(f"El resultado de {num1} * {num2} = {operations}")    
elif num1>num2:
    operations=num1-num2
    print(f"El resultado de {num1} - {num2} = {operations}")
elif num1<num2:
    operations=num1+num2  
    print(f"El resultado de {num1} + {num2} = {operations}")  
# 6. El ANSES requiere clasificar a las personas que se jubilaran en el año de 2010. Existen tres tipos de
# jubilaciones: por edad, por antigüedad joven y por antigüedad adulta.
# - Las personas adscritas a la jubilación por edad deben tener 60 años o más y una antigüedad en su
# empleo de menos de 25 años.
# - Las personas adscritas a la jubilación por antigüedad joven deben tener menos de 60 años y una
# antigüedad en su empleo de 25 años o más.
# - Las personas adscritas a la jubilación por antigüedad adulta deben tener 60 años o más y una antigüedad
# en su empleo de 25 años o más.
# Determinar en qué tipo de jubilación, quedara adscrita una persona.
# 7. Calcular la utilidad que un trabajador recibe en el reparto anual de utilidades si este se le asigna como un
# porcentaje de su salario mensual que depende de su antigüedad en la empresa de acuerdo con la siguiente
# tabla:
# Tiempo Utilidad
# Menos de 1 año 5 % del salario
# 1 año o más y menos de 2 años 7% del salario
# 2 años o más y menos de 5 años 10% del salario
# 5 años o más y menos de 10 años 15% del salario
# 10 años o más 20% del salario