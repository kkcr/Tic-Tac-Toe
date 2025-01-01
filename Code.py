def p_board(board):
print("-------------")
for i in range(3):
print("|", end=" ")
for j in range(3):
print(board[i][j], end=" ")
print("|", end=" ")
print("\n------------")
print("\n")

#Checks for the sequence of 3
def c_winner(board):
#check rows for sequence

for i in range(3):
if board[i][0] == board[i][1] == board[i][2] != " ":
return board[i][0]
#check columns for sequence
for j in range(3):
if board[0][j] == board[1][j] == board[2][j] != " ":
return board[0][j]
#check diagonals for sequence
if board[0][0] == board[1][1] == board[2][2] != " ":
return board[0][0]
if board[0][2] == board[1][1] == board[2][0] != " ":
return board[0][2]
return None

#Checks weater the board is filled with moves or not
def is_board_full(board):
for i in range(3):
for j in range(3):
if board[i][j] == " ":
return False
return True

def start():
board = [[" ", " ", " "],
[" ", " ", " "],
[" ", " ", " "]]

c_player = "1"
while True:
p_board(board)
print("Player", c_player)
row = int(input("Enter the row (1-3): "))
col = int(input("Enter the column (1-3): "))
row-=1
col-=1
print("\n")
if(row>2 or col>2):
print("invalid move. Try again.\n")
continue
else:
if board[row][col] == " ":
if c_player=="1":
board[row][col] = "X"
else:
board[row][col] = "O"

else:
print("Invalid move. Try again.\n")
continue

winner = c_winner(board)
if winner:
p_board(board)
print("Player", c_player, "wins!")
break
if is_board_full(board):
p_board(board)
print("It's a tie!")
break

c_player = "2" if c_player == "1" else "1"

start()
