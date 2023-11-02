from func_preparcial import *

# Crea un juego de Bingo donde el usuario pueda ingresar los números para generar su propio cartón de bingo. A
# continuación, se detalla cómo se debe implementar el juego:
# 1. Solicita al usuario que ingrese 25 números únicos, uno a la vez, 
# para completar su cartón de bingo. Los
# números deben estar en el rango de 1 a 75.


# 2. Valida que los números ingresados sean únicos y estén dentro del rango permitido. Si el usuario ingresa un
# número duplicado o fuera del rango, debe mostrar un mensaje de error y solicitar otro número.
bingo_card=[[None for i in range(5)]for _ in range(5)]
amount_num=1

for row in range(5):
    for col in range(5):
        num=random.randint(1,75)
        # num=int(input(f"Ingrese el numero  en la posicion {amount_num} : "))
        num=verify_num(num,bingo_card)
        bingo_card[row][col]=num
        amount_num+=1

# 3. Después de que el usuario haya completado su cartón, inicia el juego de Bingo.
print("Iniciando Bingo")
print_bingo_list(bingo_card)
play_bingo(bingo_card)
# 4. Extrae bolas de bingo al azar y verifica si los números extraídos están en el cartón del usuario.
# 5. Continúa extrayendo bolas de bingo hasta que el jugador complete una línea horizontal, vertical o diagonal
# en su cartón.
# 6. Muestra mensajes informativos al usuario a medida que se extraen bolas y cuando gana.
# 7. Pregunta al usuario si desea jugar de nuevo al finalizar el juego.
