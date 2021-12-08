import time

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkForBlock(mark, mark2):
    if(board[1] == board[2] and board[1] == mark2 and board[3] == mark):
        return True
    elif(board[2] == board[3] and board[2] == mark2 and board[1] == mark):
        return True
    elif(board[1] == board[3] == mark2 and board[2] == mark):
        return True
    elif (board[4] == board[5] and board[4] == mark2 and board[6] == mark):
        return True
    elif (board[4] == board[6] and board[4] == mark2 and board[5] == mark):
        return True
    elif(board[5] == board[6] and board[5] == mark2 and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == mark2 and board[9] == mark):
        return True
    elif (board[7] == board[9] and board[7] == mark2 and board[8] == mark):
        return True
    elif (board[8] == board[9] and board[8] == mark2 and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == mark2 and board[7] == mark):
        return True
    elif (board[1] == board[7] and board[1] == mark2 and board[4] == mark):
        return True
    elif (board[4] == board[7] and board[4] == mark2 and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == mark2 and board[8] == mark):
        return True
    elif (board[2] == board[8] and board[2] == mark2 and board[5] == mark):
        return True
    elif (board[5] == board[8] and board[5] == mark2 and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == mark2 and board[9] == mark):
        return True
    elif (board[3] == board[9] and board[3] == mark2 and board[6] == mark):
        return True
    elif (board[6] == board[9] and board[6] == mark2 and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == mark2 and board[9] == mark):
        return True
    elif (board[1] == board[9] and board[1] == mark2 and board[5] == mark):
        return True
    elif (board[5] == board[9] and board[5] == mark2 and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == mark2 and board[3] == mark):
        return True
    elif (board[3] == board[7] and board[3] == mark2 and board[5] == mark):
        return True
    elif (board[3] == board[5] and board[3] == mark2 and board[7] == mark):
        return True

    else:
        return False
    



def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return

def compMove2():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = player
            score = minimax2(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(player, bestMove)
    return


def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def minimax(board, depth, isMaximizing):
    point = 0
    if (depth == 9):
        return 0
    elif (checkWhichMarkWon(bot)):
        return 10
    elif (checkWhichMarkWon(player)):
        return -10
    elif (checkForBlock(bot, player)):
        point += 5
    elif (checkDraw()):
        return 0
    else:
        point = 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False) + point
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True) + point
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

def minimax2(board, depth, isMaximizing):
    point = 0
    if (depth == 9):
        return 0
    elif (checkWhichMarkWon(player)):
        return 10
    elif (checkWhichMarkWon(bot)):
        return -10
    elif (checkForBlock(player, bot)):
        point += 5
    elif (checkDraw()):
        return 0
    
    
    
    else:
        point = 0

    if (isMaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, False) + point
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, True) + point
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


#global firstComputerMove
#firstComputerMove = True


while not checkForWin():
   compMove()
   compMove2()
   
    
    