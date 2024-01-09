board = ["-","-","-",
         "-","-","-",
         "-","-","-",]
gamerun = True
game_winner = None
player = "X"

def pboard(board):
    print(board[0], "|",board[1],"|",board[2])
    print(board[3], "|",board[4],"|",board[5])
    print(board[6], "|",board[7],"|",board[8])

def move(player):
    location = int(input("enter your location 1-9: "))
    if location >= 1 and location <=9 and board[location-1] == "-":
        board[location-1] = player

def checkhor(board):
    global game_winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        game_winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        game_winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        game_winner = board[6]
        return True

def checkver(board):
    global game_winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        game_winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        game_winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        game_winner = board[2]
        return True
    
def checkdia(board):
    global game_winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        game_winner = board[0]
        return True
    elif board[6] == board[4] == board[2] and board[6] != "-":
        game_winner = board[6]
        return True
    
def checktie(board):
    global gamerun
    if "-" not in board:
        pboard(board)
        print("Tie!")
        gamerun = False

def checkgame():
    global gamerun
    if checkhor(board) or checkver(board) or checkdia(board):
        print("congrats winner " + game_winner)
        gamerun = False
        pboard(board)
    checktie(board)

def changeplayer():
    global player 
    if player == "X":
        player = "O"
    else:
        player = "X"

while gamerun:
    pboard(board)
    move(player)
    checkgame()
    changeplayer()


