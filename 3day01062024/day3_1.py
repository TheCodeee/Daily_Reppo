# SNAKE WATER GUN GAME
import random

score_player = 0
score_comp = 0
Player = False
Comp = False

for i in range(3):
    comp = random.randint(1, 3)
    value = int(input("----Snake = 1---Water = 2----Gun = 3----\n\n------Enter value from 1 to 3-------\n"))

    if value == 1 and comp == 1:
        print("SNAKE V/S SNAKE \n ---->   DRAW   <----")
        Player = False
        Comp = False

    elif value == 1 and comp == 2:
        print("SNAKE V/S WATER \n ---->   PLAYER WIN   <----")
        Player = True
        Comp = False

    elif value == 3 and comp == 3:
        print("SNAKE V/S GUN \n ---->   COMP WINS   <----")
        Comp = True
        Player = False

    elif value == 2 and comp == 1:
        print("WATER V/S SNAKE \n ---->   COMP WINS   <----")
        Comp = True
        Player = False

    elif value == 2 and comp == 2:
        print("WATER V/S WATER \n ---->   DRAW   <----")
        Player = False
        Comp = False

    elif value == 2 and comp == 3:
        print("WATER V/S GUN \n ---->   PLAYER WINS   <----")
        Player = True
        Comp = False

    elif value == 3 and comp == 1:
        print("GUN V/S SNAKE \n ---->   PLAYER WINS   <----")
        Player = True
        Comp = False

    elif value == 3 and comp == 2:
        print("GUN V/S WATER \n ---->   COMP WIN   <----")
        Comp = True
        Player = False

    elif value == 3 and comp == 3:
        print("GUN V/S GUN \n ---->   DRAW   <----")
        Player = False
        Comp = False

    if Player:
        score_player += 10

    elif Comp:
        score_comp += 10

    else:
        pass

print("\n\n----Player Score---- = ", score_player, "\n----Comp Score---- = ", score_comp, "\n\n")
if score_comp > score_player:
    print("===============>   COMPUTER WINS   <================")

elif score_player > score_comp:
    print("=============>   PLAYER WINS   <==============")

else:
    print("=============>   DRAW    <===================")
