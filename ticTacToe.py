def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################
    
#########################PRINTED THE BOARD ABOVE LIKE THE TEXTBOOK. SHOULD BE DONE###############################################################
def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    if (board['mid-L']==player) and (board['mid-M']==player) and (board['mid-R']==player):#ADDED MIDDLE ACROSS WINNING SCENARIO
        return True
    elif (board['top-L']==player) and (board['top-M']==player) and (board['top-R']==player):#ADDED TOP ACROSS WINNING SCENARIO
        return True
    elif (board['low-L']==player) and (board['low-M']==player) and (board['low-R']==player):#ADDED LOWER ACROSS WINNING SCENARIO
        return True
    elif (board['top-L']==player) and (board['mid-L']==player) and (board['low-L']==player):#ADDED LEFT VERTICAL WINNING SCENARIO
        return True
    elif (board['top-M']==player) and (board['mid-M']==player) and (board['low-M']==player):#ADDED MIDDLE VERTICAL WINNING SCENARIO
        return True
    elif (board['top-R']==player) and (board['mid-R']==player) and (board['low-R']==player):#ADDED RIGHT VERTICAL WINNING SCENARIO
        return True
    elif (board['top-L']==player) and (board['mid-M']==player) and (board['low-R']==player):#ADDED DIAGONAL WINNING SCENARIO #1
        return True
    elif (board['top-R']==player) and (board['mid-M']==player) and (board['low-L']==player):#ADDED DIAGONAL WINNING SCENARIO #2
        return True
    else:
        return False
        
    
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board          #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

    turn = startingPlayer
    for i in range(9):
        printBoard(board)#prints the empty board
        print('Turn for ' + turn + '. Move on which space?')#asking the player where they want to move
        move = input() #player inputs their move
        board[move] = turn#takes the players choice and inputs it onto the board
        if( checkWinner(board, 'X') ):#checking if the players moves return true
            print('X wins!')
            break
        elif ( checkWinner(board, 'O') ):#checking if the players moves return true
            print('O wins!')
            break
    
        if turn == 'X':#switching turns
            turn = 'O'
        else:
            turn = 'X'
        
    printBoard(board)
    
