# tic-tac-toe 2 player game

#defined two hash tables titled TTT (tic-tac-tow) and WC (win condition)
TTT = {}
WC = {}

#TTT will be the tic-tac-toe board intialized to blank space
TTT['1'] = ' ' 
TTT['2'] = ' '
TTT['3'] = ' '
TTT['4'] = ' '
TTT['5'] = ' '
TTT['6'] = ' '
TTT['7'] = ' '
TTT['8'] = ' '
TTT['9'] = ' '

#WC will have key values X and O and be intialized to blank space as well
WC['X'] = ' '
WC['O'] = ' '

#since players use 1-9 to pick board spaces their choices are intialized to 0                                               
player1Choice = 0
player2Choice = 0

#global won variable initialized to false
global won
won = False

#global tie variable initialized to false
global tie
tie = False

#global turn counter
global turn
turn = 0

#player1 (X player) function
def player1Turn():
    global turn
    while True:
        player1Choice = input("")
        
        if(TTT[player1Choice] == ' '):
            TTT[player1Choice] = 'X'
            turn += 1
            break
        elif(TTT[player1Choice] == 'X' or 'O'):
            print("That space is taken")
        else:
            print("Not a valid input")

            
    WC['X'] = TTT['1'] + TTT['2'] + TTT['3'],\
              TTT['4'] + TTT['5'] + TTT['6'],\
              TTT['7'] + TTT['8'] + TTT['9'],\
              TTT['1'] + TTT['4'] + TTT['7'],\
              TTT['2'] + TTT['5'] + TTT['8'],\
              TTT['3'] + TTT['6'] + TTT['9'],\
              TTT['3'] + TTT['5'] + TTT['7'],\
              TTT['1'] + TTT['5'] + TTT['9']

#player2 (O player) function
def player2Turn():
    global turn
    while True:
        player1Choice = input("")
        
        if(TTT[player1Choice] == ' '):
            TTT[player1Choice] = 'O'
            turn += 1
            break
        elif(TTT[player1Choice] == 'X' or 'O'):
            print("That space is taken")
        else:
            print("Not a valid input")

    WC['O'] = TTT['1'] + TTT['2'] + TTT['3'],\
              TTT['4'] + TTT['5'] + TTT['6'],\
              TTT['7'] + TTT['8'] + TTT['9'],\
              TTT['1'] + TTT['4'] + TTT['7'],\
              TTT['2'] + TTT['5'] + TTT['8'],\
              TTT['3'] + TTT['6'] + TTT['9'],\
              TTT['3'] + TTT['5'] + TTT['7'],\
              TTT['1'] + TTT['5'] + TTT['9']
            
#function that prints the current board along with the valid 1-9 inputs
def printBoard():

    print("1 = top left")
    print("2 = top center")
    print("3 = top right")
    print("4 = middle left")
    print("5 = middle center")
    print("6 = middle right")
    print("7 = bottom left")
    print("8 = bottom center")
    print("9 = bottom right\n")

    print("    |    |   ")
    print(" %s  | %s  | %s " % (TTT['1'], TTT['2'], TTT['3']))
    print("----+----+----")
    print(" %s  | %s  | %s  " % (TTT['4'], TTT['5'], TTT['6']))
    print("----+----+----")
    print(" %s  | %s  | %s  " % (TTT['7'], TTT['8'], TTT['9']))
    print("    |    |   ")

#win condition that checks if either player won and then changes global variable won to True
def winCondition():
    global won
    global tie
    global turn
    
    if ("XXX" in WC['X']):
        print("\n-------------------X wins!--------------------\n")
        won = True
    elif("OOO" in WC['O']):
        print("\n-------------------O wins!--------------------\n")
        won = True
    else:
        print("\nno winner yet\n")
    if (won == False and turn == 9):
        print("\n-------------------Tie!--------------------\n")
        tie = True
        


#main program will loop until either one player wins or a tie occurs then ends the program  
while True:
    printBoard()
    player1Turn()
    winCondition()
    if(won == True or tie == True):
        printBoard()
        break
    printBoard()
    player2Turn()
    winCondition()
    if(won == True or tie == True):
        printBoard()
        break
   
