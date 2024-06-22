import array as arr
import random as r

def starting_1():
    print()
    print("************************************************************************************")
    print("Welcome to Snake and Ladder Game")
    print("Type any alphabet and press enter to roll the dice")
    print("The first person out of two to reach 100 is the winner.")
    print("Use the ladders to your advantage and beware of the snakes in your path.")
    print("All the best :)")
    for i in range(2):
        print()
    print("Game starts")
    print("The Board is displayed :)")
    print()
    print("********************************************************************************")
    print()

def starting_2():
    print()
    print("******************************************************************************************")
    print("Snakes are represented by negative numbers and ladders by positive numbers")
    print("******************************************************************************************")
    print("The two players are reprented by 'P1' and 'P2'")
    print("******************************************************************************************")
    print()
    snakesandladder()

def default():
    count=0
    box = [91,92,93,94,95,96,97,98,99,100,90,89,88,87,86,85,84,83,82,81,71,72,73,74,75,76,77,78,79,80,70,69,68,67,66,65,64,63,62,61,51,52,53,54,55,56,57,58,59,60,50,49,48,47,46,45,44,43,42,41,31,32,33,34,35,36,37,38,39,40,30,29,28,27,26,25,24,23,22,21,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2,1]
    for i in range(10):
        for j in range(10):
            if(box[count]<9):
                print(" ",end="")
            print(box[count],end=" ")
            count=count+1
        print()

def snakesandladder():
    snake = [0,0,-20,0,-20,0,0,-19,0,0,0,0,0,-51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-16,0,-43,0,0,0,0,-20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-11,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ladder = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,0,0,0,0,0,0,0,19,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,56,0,0,0,0,0,0,21,0,0,0,0,0,0,0,0,0,0,0,22,0,0,0,0,10,0,0,0]
    count = 0
    for i in range(10):
        for j in range(10):
            if(snake[count]==0 and ladder[count]==0):
                print("000",end=" ")
            if(snake[count]!=0):
                print(snake[count],end=" ")
            if(ladder[count]!=0):
                print("+",end="")
                print(ladder[count],end=" ")
            count = count + 1
        print()

def dice_roll():
    value = r.randint(1,6)
    return value


def findindex(player_value):
    board = [91,92,93,94,95,96,97,98,99,100,90,89,88,87,86,85,84,83,82,81,71,72,73,74,75,76,77,78,79,80,70,69,68,67,66,65,64,63,62,61,51,52,53,54,55,56,57,58,59,60,50,49,48,47,46,45,44,43,42,41,31,32,33,34,35,36,37,38,39,40,30,29,28,27,26,25,24,23,22,21,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2,1]
    count = 0
    index = 0
    for i in range(10):
        for j in range(10):
            if(player_value==board[count]):
                index = count
                return index
            count = count + 1

def checksnakeandladder(player_value):
    index = findindex(player_value)
    snake = [0,0,-20,0,-20,0,0,-19,0,0,0,0,0,-51,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-16,0,-43,0,0,0,0,-20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-11,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ladder = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,19,0,0,0,0,0,0,0,19,0,0,0,0,0,0,0,0,0,0,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,56,0,0,0,0,0,0,21,0,0,0,0,0,0,0,0,0,0,0,22,0,0,0,0,10,0,0,0]
    if(snake[index]!=0):
        player_value = player_value + snake[index]
        print("Bitten by snake")
    elif(ladder[index]!=0):
        player_value = player_value + ladder[index]
        print("Ladder found")
    return player_value

def printtheboard(player1,player2):
    box = [91,92,93,94,95,96,97,98,99,100,90,89,88,87,86,85,84,83,82,81,71,72,73,74,75,76,77,78,79,80,70,69,68,67,66,65,64,63,62,61,51,52,53,54,55,56,57,58,59,60,50,49,48,47,46,45,44,43,42,41,31,32,33,34,35,36,37,38,39,40,30,29,28,27,26,25,24,23,22,21,11,12,13,14,15,16,17,18,19,20,10,9,8,7,6,5,4,3,2,1]    
    count = 0
    status = False
    for i in range(10):
        for j in range(10):
            status = False
            if(player1==box[count]):
                print("P1",end=" ")
                status = True
            if(player2==box[count]):
                print("P2",end=" ")
                status = True
            if(status==True):
                count = count + 1
                continue
            if(box[count]<9):
                print(" ",end="")
            print(box[count],end=" ")
            count = count+1
        print()
    print()
    print("************************************************************************")
    print()

def main():
    starting_1()
    default()
    starting_2()
    player1 = 1
    player2 = 1
    print()
    print()
    printtheboard(player1,player2)
    shift = 0
    while(True):
        input_user = input()
        roll = dice_roll()
        if(shift%2==0):
            player1 = player1 + roll
            if(player1==100):
                print("************************************************************************")
                print("Player 1 gets : ",end="")
                print(roll)
                print("************************************************************************")
                print()
                print("***************Player 1 Wins**********************")
                print("*****************Game over************************")
                break
            if(player1>100):
                player1 = player1 - roll
            print("************************************************************************")
            print("Player 1 gets : ",end="")
            print(roll)
            if(player1==player2):
                player2 = 1
            else:
                player1 = checksnakeandladder(player1)
            print("************************************************************************")
            print()
            if(roll==6):
                printtheboard(player1,player2)
                continue
            shift = shift + 1
        else:
            player2 = player2 + roll
            if(player2==100):
                print("************************************************************************")
                print("Player 2 gets : ",end="")
                print(roll)
                print("************************************************************************")
                print()
                print("***************Player 2 Wins**********************")
                print("*****************Game over************************")
                break
            if(player2>100):
                player2 = player2 - roll
            print("************************************************************************")
            print("Player 2 gets : ",end="")
            print(roll)
            if(player1==player2):
                player1 = 1
            else:
                player2 = checksnakeandladder(player2)
            print("************************************************************************")
            print()
            if(roll==6):
                printtheboard(player1,player2)
                continue
            shift = shift + 1
        printtheboard(player1,player2)
   
main()
