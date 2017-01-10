# tic-tac-toe
TTT = {}

TTT["TL"] = ' ' 
TTT["TC"] = ' '
TTT["TR"] = ' '
TTT["ML"] = ' '
TTT["MC"] = ' '
TTT["MR"] = ' '
TTT["BL"] = ' '
TTT["BC"] = ' '
TTT["BR"] = ' '


computerScore = 0
playerScore = 0
player1Choice = ''
player2Choice = ''
global turn
turn = True 

def player1Turn(turn):
    while turn == True:
        player1Choice = input("")
    
        if(TTT[str(player1Choice)] == ' '):
            TTT[str(player1Choice)] = 'X'
            turn = False
        else:
            print("That space is taken")
        
    printBoard()

    player2Turn(turn)


def player2Turn(turn):
    while turn == False:
        player1Choice = input("")
        
        if(TTT[str(player1Choice)] == ' '):
            TTT[str(player1Choice)] = 'O'
            turn = True
        else:
            print("That space is taken")
            

    printBoard()

    player1Turn(turn)


def printBoard():

    print("    |    |   ")
    print(" %s  | %s  | %s " % (TTT["TL"], TTT["TC"], TTT["TR"]))
    print("----+----+----")
    print(" %s  | %s  | %s  " % (TTT["ML"], TTT["MC"], TTT["MR"]))
    print("----+----+----")
    print(" %s  | %s  | %s  " % (TTT["BL"], TTT["BC"], TTT["BR"]))
    print("    |    |   ")
    
while player1Choice != 'q':
    player1Turn(turn)
    #player2Turn(turn)    

#def winCondition():
    #break

    # need to make functions for win conditions and player 1 and 2 turns
