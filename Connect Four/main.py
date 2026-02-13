board = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
game = True
player = 'X'
choice = 0
tie = False
def printBoard():
  print('-' * 35)
  for i in range(6):
    for j in range(7):
      print("|", board[i][j], "|", end='')
      if (j % 7 == 6):
        print()
        print('-' * 35)
while (game):
  printBoard()
  while (choice <= 0 or choice > 7):
    try:
      choice = int(input("Enter a column to put your chip (1-7) (Player " + player + "): "))
    except:
      print("Enter a valid number")
  if (board[0][choice - 1] != ' '):
    print("\nRow is full. Try again.\n")
    choice = 0
    continue
  for i in range(5, -1, -1):
    if (board[i][choice - 1] == ' '):
      board[i][choice - 1] = player
      break
  for i in range(6):
    for j in range(4):
      if (board[i][j] == player and board[i][j + 1] == player
          and board[i][j + 2] == player and board[i][j + 3] == player):
        game = False
  for i in range(3):
    for j in range(7):
      if (board[i][j] == player and board[i + 1][j] == player
          and board[i + 2][j] == player and board[i + 3][j] == player):
        game = False
  for i in range(5, 2, -1):
    for j in range(4):
      if (board[i][j] == player and board[i - 1][j + 1] == player
          and board[i - 2][j + 2] == player and board[i - 3][j + 3] == player):
        game = False
  for i in range(3):
    for j in range(4):
      if (board[i][j] == player and board[i + 1][j + 1] == player
          and board[i + 2][j + 2] == player and board[i + 3][j + 3] == player):
        game = False
  blankCount = 0
  for i in range(6):
    for j in range(7):
      if(board[i][j] == ' '):  blankCount+=1
  if(blankCount == 0):
    game = False;
    tie = True;
  if (game == False): break 
  if (player == 'X'): player = 'O'
  else: player = "X"
  choice = 0
printBoard()
if(tie == False):
  print("Player " + player + " Wins.")
else:
  print("Tie game.")
