

print("====================tic tac toe game==============================")
board = ["1","2","3",
          "4","5","6",
          "7","8","9"]
def show_board():
  print()
  print(board[0],"|",board[1],"|",board[2])
  print("--+--+--")
  print(board[3],"|",board[4],"|",board[5])
  print("--+--+--")
  print(board[6],"|",board[7],"|",board[8])
  print()
def check_winner():
  if board[0] == board[1] == board[2]:
    return True
  if board[3] == board[4] == board[5]:
    return True
  if board[6] == board[7] == board[8]:
    return True
  if board[0] == board[3] == board[6]:
    return True
  if board[1] == board[4] == board[7]:
    return True
  if board[2] == board[5] == board[8]:
    return True
  if board[0] == board[4] == board[8]:
    return True
  if board[2] == board[4] == board[6]:
    return True
  return False

player = 'x'
for turn in range (9):
    show_board()
    print("player",player)

    while True:
        try:
            position = int(input("enter position (1-9):"))
            if 1 <= position <= 9 and board[position -1] != "x" and board[position -1] != "o":
                break
            else:
                print("position already taken or invalid input. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

    board[position -1] = player

    if check_winner():
        show_board()
        print("player",player,"wins")
        break

    if turn == 8:
        show_board()
        print("tie")
        break

    if player == "x":
        player = "o"
    else:
        player = "x"

