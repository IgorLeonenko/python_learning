def print_board(board):
  for row in board:
    print(" | ".join(row))
    print("-" * 10)

def check_win(board):
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
      return True
    if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
      return True
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
      return True
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
      return True
  return False

def check_draw(board):
  for row in board:
    for cell in row:
      if cell == ' ':
        return False
  return True


def game():
  board = [[" " for _ in range(3)] for _ in range(3)]
  first_player = "X"

  while True:
    print_board(board)
    user_input = input(f"Player, enter your move in: column row \n")
    row, column = user_input.split()
    row = int(row)
    column = int(column)

    if board[row][column] == ' ':
      board[row][column] = first_player
      if check_win(board):
          print_board(board)
          print(f"{first_player} Wins!")
          break
      if check_draw(board):
          print_board(board)
          print("It's a Draw!")
          break
      first_player = 'O' if first_player == 'X' else 'X'
    else:
        print("Cell already occupied! Try again.")

game()