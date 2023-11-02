import random
def verify_num(num,bingo_card):
    change_num=False
    if num<1 or num>75:
        change_num=True
        print(f"El numero {num} tiene valores incorrectos ")
    else:
        for r in bingo_card:
            if num in r:
                print(f"El numero {num} ya esta en el carton ")
                change_num=True

    if change_num==False:
        return num
    else:
        print("numero incorrecto ingreselo nuevamente ")
        # num=int(input())
        num=random.randint(1,75)
        return verify_num(num,bingo_card)
    
def print_bingo_list(bingo_card):
    print("Carton")
    for row in bingo_card:

        print("-------------------")
        print(row)
    print("-------------------")
def return_bingo_ball(bingo_ball_list):
    
    bingo_ball=random.randint(1,75)
    if bingo_ball in bingo_ball_list :
        return return_bingo_ball(bingo_ball_list)
    else :
        print(f"Bola numero : {bingo_ball}")
        bingo_ball_list.append(bingo_ball)
        return bingo_ball

def verify_is_win(bingo_card):
    
    for row in bingo_card:
        if row[0]==row[1]==row[2]==row[3]==row[4]:
            print("Ganador por linea horizontal ")
            return True
    for column in range(5):
        if bingo_card[0][column]==bingo_card[1][column]==bingo_card[2][column]==bingo_card[3][column]==bingo_card[4][column]:

            print("Ganador por linea vertical ")
            return True
    if bingo_card[0][0]==bingo_card[1][1]==bingo_card[2][2]==bingo_card[3][3]==bingo_card[4][4]:
            print("Ganador por diagonal")
            return True
    elif bingo_card[0][4]==bingo_card[1][3]==bingo_card[2][2]==bingo_card[3][1]==bingo_card[4][0]:
            print("Ganador por diagonal inversa")
            return True

        
def play_bingo(bingo_card):
    bingo_ball_list=[]
    find_winner=False
    while True:

        if len(bingo_ball_list)==75:
            print("El jugador ha perdido")
            break
        else:
            bingo_ball=return_bingo_ball(bingo_ball_list)
        for row in range(5):
                for col in range(5):
                    if bingo_ball ==bingo_card[row][col]:
                        print(f"Tachando numero {bingo_ball}")
                        bingo_card[row][col]="X"
                        print_bingo_list(bingo_card)
        find_winner=verify_is_win(bingo_card)
        if find_winner==True:
            break
    