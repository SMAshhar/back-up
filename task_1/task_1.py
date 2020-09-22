user = input("Choose X or O : ")

if user.upper() == "X":
    AI = "O"
else:
    AI = "x"

top1 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
top2 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
top3 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
mid1 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
mid2 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
mid3 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
bot1 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
bot2 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]
bot3 = [" ", " ", " ", " ", " ", " ", "|", " ", " ", " ", " ", "|", " ", " ", " ", " "]

def board():
    for i in top1:
        print(i, end = "")
    print("")
    for i in top2:
        print(i, end = "")
    print("")
    for i in top3:
        print(i, end = "")
    print("")
    print('------------------')
    for i in mid1:
        print(i, end = "")
    print("")
    for i in mid2:
        print(i, end = "")
    print("")
    for i in mid3:
        print(i, end = "")
    print("")
    print('------------------')
    for i in bot1:
        print(i, end = "")
    print("")
    for i in bot2:
        print(i, end = "")
    print("")
    for i in bot3:
        print(i, end = "")  

    print("\n##############################################")

cpu = False
plr = False

global win 
win = False
global loose
loose = False


def win_loose():

# Cpu win condition
    global loose
    if 1 in cpu_choice and 2 in cpu_choice and 3 in cpu_choice:
        loose = True
    elif 4 in cpu_choice and 5 in cpu_choice and 6 in cpu_choice:
        loose = True
    elif 7 in cpu_choice and 8 in cpu_choice and 9 in cpu_choice:
        loose = True
    elif 7 in cpu_choice and 4 in cpu_choice and 1 in cpu_choice:
        loose = True
    elif 8 in cpu_choice and 5 in cpu_choice and 2 in cpu_choice:
        loose = True
    elif 3 in cpu_choice and 6 in cpu_choice and 9 in cpu_choice:
        loose = True
    elif 7 in cpu_choice and 5 in cpu_choice and 3 in cpu_choice:
        loose = True
    elif 9 in cpu_choice and 5 in cpu_choice and 1 in cpu_choice:
        loose = True

# Player win condition
    global win
    if 1 in plr_choice and 2 in plr_choice and 3 in plr_choice:
        win = True
    elif 4 in plr_choice and 5 in plr_choice and 6 in plr_choice:
        win = True
    elif 7 in plr_choice and 8 in plr_choice and 9 in plr_choice:
        win = True
    elif 7 in plr_choice and 4 in plr_choice and 1 in plr_choice:
        win = True
    elif 8 in plr_choice and 5 in plr_choice and 2 in plr_choice:
        win = True
    elif 3 in plr_choice and 6 in plr_choice and 9 in plr_choice:
        win = True
    elif 7 in plr_choice and 5 in plr_choice and 3 in plr_choice:
        win = True
    elif 9 in plr_choice and 5 in plr_choice and 1 in plr_choice:
        win = True



import random

def firstturn():
    y = random.randint(0, 1)
    if y == 1:
        global cpu
        cpu = True
    else:
        global plr
        plr = True

firstturn()
board()


turns = [1, 2, 3, 4, 5, 6, 7, 8, 9]

cpu_choice = []
plr_choice = []

while win == False and loose == False and len(turns) > 0:
    if cpu == True:
        dice = random.randrange(len(turns))
        com_turn = int(turns[dice])
        if com_turn in [7, 8, 9] and com_turn in turns:
            if com_turn == 7:
                top2[2] = AI
            elif com_turn == 8:
                top2[9] = AI
            elif com_turn == 9:
                top2[13] = AI
            cpu_choice.append(com_turn)
            turns.remove(com_turn)
            board()
            cpu = False
            plr = True
        elif com_turn in [4, 5, 6] and com_turn in turns:
            if com_turn == 4:
                mid2[2] = AI
            elif com_turn == 5:
                mid2[9] = AI
            elif com_turn == 6:
                mid2[13] = AI
            cpu_choice.append(com_turn)
            turns.remove(com_turn)
            board()
            cpu = False
            plr = True
        elif com_turn in [1, 2, 3] and com_turn in turns:
            if com_turn == 1:
                bot2[2] = AI
            elif com_turn == 2:
                bot2[9] = AI
            elif com_turn == 3:
                bot2[13] = AI
            cpu_choice.append(com_turn)
            turns.remove(com_turn)
            board()
            cpu = False
            plr = True
        win_loose()
        print(win, loose)

    elif plr == True:
        plr_turn = int(input("Enter Your choice : "))
        if plr_turn in [7, 8, 9] and plr_turn in turns:
            if plr_turn == 7:
                top2[2] = user
            elif plr_turn == 8:
                top2[9] = user
            elif plr_turn == 9:
                top2[13] = user
            plr_choice.append(plr_turn)
            turns.remove(plr_turn)
            plr == False
            cpu = True
        elif plr_turn in [4, 5, 6] and plr_turn in turns:
            if plr_turn == 4:
                mid2[2] = user
            elif plr_turn == 5:
                mid2[9] = user
            elif plr_turn == 6:
                mid2[13] = user  
            plr_choice.append(plr_turn)          
            turns.remove(plr_turn)
            plr == False
            cpu = True
        elif plr_turn in [1, 2, 3] and plr_turn in turns:
            if plr_turn == 1:
                bot2[2] = user
            elif plr_turn == 2:
                bot2[9] = user
            elif plr_turn == 3:
                bot2[13] = user
            plr_choice.append(plr_turn)
            turns.remove(plr_turn)
            plr == False
            cpu = True
        else:
            print("Wrong choice")
        win_loose()
        print(win, loose)
        
        board()

    win_loose()
  
board()
if win == True:
    print("===============")
    print(" Y O U  W I N")
    print("===============")
elif loose == True:
    print("===============")
    print(" C P U  W I N")
    print("===============")   
else:
    print("===============")
    print("  D  R  A  W  ")
    print("===============")  

print("Your choices = ", plr_choice)
print("Computer's Choices = ", cpu_choice)