#Ingresando fecha
fecha=input( " Ingrese el dia de la semana , DD/MM ")
#separamos dia de la semana , DD,MM en diferentes variables
dia_sem=fecha[0:fecha.find(",")]
dia_mes=int(fecha[fecha.find(",")+1:fecha.find("/")])
mes=int(fecha[fecha.find("/")+1:])

#Transformamos a minusculas el dia de la semana 
dia_sem= dia_sem.lower()
#Validamos el dia de la semana
if dia_sem != "lunes" and dia_sem!="martes"  and dia_sem!="miercoles"  and dia_sem!="jueves" :
    dia_sem=input(" Ingreso incorrecto , Ingrese nuevamente el dia de la semana que corresponda: ")
    if  dia_sem != "lunes" and dia_sem!="martes"  and dia_sem!="miercoles"  and dia_sem!="jueves" :
        print("dia incorrecto")
else:
    if dia_sem=="lunes":
        nivel="basico"
        print(f"Nivel {nivel}")
        #Se pregunta si se tomo examen y luego se pasa a minuscula por si el usuario lo ingreso en mayuscula
        tomo_examen=input("Escriba si o no si tomo examen : " ).lower()
        if tomo_examen=="si":
            notas_examen=int(input("Ingrese cuantas personas rindieron "))
            aprobados=int(input("Ingrese cuantas personas aprobaron el examen: "))
            prom_aprobados= float(aprobados/notas_examen)
            print(f"En el nivel {nivel} se realizo una evalucion para {notas_examen} y aprobaron un promedio de {prom_aprobados} %")
        
    elif dia_sem=="martes":
        nivel="medio"
        print(f"Nivel {nivel}")
        #Se pregunta si se tomo examen y luego se pasa a minuscula por si el usuario lo ingreso en mayuscula
        tomo_examen=input("Escriba si o no si tomo examen : " ).lower()
        if tomo_examen=="si":
            notas_examen=int(input("Ingrese cuantas personas rindieron "))
            aprobados=int(input("Ingrese cuantas personas aprobados el examen: "))
            prom_aprobados= float(aprobados/notas_examen)
            print(f"En el nivel {nivel} se realizo una evalucion para {notas_examen} y aprobaron un promedio de {prom_aprobados} %")
        
    elif dia_sem=="miercoles":
        nivel="avanzado"
        print(f"Nivel {nivel}")
        #Se pregunta si se tomo examen y luego se pasa a minuscula por si el usuario lo ingreso en mayuscula
        tomo_examen=input("Escriba si o no si tomo examen : " ).lower()
        if tomo_examen=="si":
            notas_examen=int(input("Ingrese cuantas personas rindieron "))
            aprobados=int(input("Ingrese cuantas personas aprobados el examen: "))
            prom_aprobados= float(aprobados/notas_examen)
            print(f"En el nivel {nivel} se realizo una evalucion para {notas_examen} y aprobaron un promedio de {prom_aprobados} %")
        
    elif dia_sem=="jueves":
        nivel= "practica"
        print(f"Nivel {nivel}")
        #Sacando la lista de asistencia del cursado
        lista_curso=int(input("Ingrese cuantas personas Hay en el cursado "))
        asistencia=int(input("Ingrese cuantas personas asistieron: "))
        prom_asistencia= float(lista_curso/asistencia)
    #Imprimimos segun el promedio de asistencia
        if prom_asistencia>=50 :
            print(f" En el nivel de {nivel} asistio la mayoria")
        else:
            print(f"En el nivel de {nivel} no asistion la mayoria de la clase")
    elif dia_sem=="viernes":
        nivel="viajeros"
        print(f"Nivel {nivel}")
    #si es el primer dia del mes 1 o 7 imprime nuevo ciclo 
        if dia_mes==1 and (mes == 1 or mes == 7):
            print("Ingresa un nuevo ciclo")
            cant_alumnos=int(input("Ingrese la cantidad de alumnos del nuevo ciclo"))
            arancel_alumn=int(input("Ingrees el arancel por alumno"))
            arancel_total= cant_alumnos* arancel_alumn
            print(f"el Ingreso total del curso de {nivel} es de {arancel_total}")
    #Si el usuario ingeso un dia incorrecto y al volverle a preguntar lo vuelve a ingresar se imprime dia incorrecto
