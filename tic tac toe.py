board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "\033[1;34mX\033[0;0m"
winner = None
gameRunning = True



def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2]+ "                             1 | 2 | 3")
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5]+ "            Modèle : " "        4 | 5 | 6")
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8]+ "                             7 | 8 | 9")


def playerInput(board):
    while True:
        if currentPlayer == "\033[1;34mX\033[0;0m":
            inp = int(input(f"Entrez un numéro entre 1 et 9 \033[1;34m Joueur X \033[0;0m : "))
        else:
            inp = int(input(f"Entrez un numéro entre 1 et 9 \033[1;31m Joueur O \033[0;0m : "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "\033[1;34mX\033[0;0m":
                print(f"Erreur ! La case est déjà utilisée \033[1;34m Joueur X \033[0;0m ! ")
            else:
                print(f"Erreur ! La case est déjà utilisée \033[1;31m Joueur O \033[0;0m ! ")
            printBoard(board)


def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True
def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("                       ")
        print("                       ")
        print("                       ")
        print("          C'est une égalité")
        print("                       ")

        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print("                       ")
        print("                       ")
        print("                       ")
        print(f"          Le gagnant est : {winner} !")



def switchPlayer():
    global currentPlayer
    if currentPlayer == "\033[1;34mX\033[0;0m":
        currentPlayer = "\033[1;31mO\033[0;0m"
    else:
        currentPlayer = "\033[1;34mX\033[0;0m"



while gameRunning:
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()