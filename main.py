from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

print(f"Welcome to {Fore.GREEN}TIC-TAC-TOE{Style.RESET_ALL} game!")

TL, TM, TR, ML, MM, MR, BL, BM, BR = "1", "2", "3", "4", "5", "6", "7", "8", "9"
turn = 1

def game():

  global TL, TM, TR, ML, MM, MR, BL, BM, BR, turn, board

  render_board()

  userInput = input(
      f"Turn player {'X' if turn == 1 else 'O'}. Please choose a location 1-9: "
  )

  if userInput == "1" and TL not in ['X', 'O']:
    TL = placeXO()
  elif userInput == "2" and TM not in ['X', 'O']:
    TM = placeXO()
  elif userInput == "3" and TR not in ['X', 'O']:
    TR = placeXO()
  elif userInput == "4" and ML not in ['X', 'O']:
    ML = placeXO()
  elif userInput == "5" and MM not in ['X', 'O']:
    MM = placeXO()
  elif userInput == "6" and MR not in ['X', 'O']:
    MR = placeXO()
  elif userInput == "7" and BL not in ['X', 'O']:
    BL = placeXO()
  elif userInput == "8" and BM not in ['X', 'O']:
    BM = placeXO()
  elif userInput == "9" and BR not in ['X', 'O']:
    BR = placeXO()
  else:
    print(Fore.RED + "Invalid move. Try again." + Style.RESET_ALL)
    game()

  turn = toggle(turn)

  if checkWin() == 'DRAW':
    render_board()
    print(
      Fore.MAGENTA + 'DRAW' + Style.RESET_ALL)
    print(f"Game Over. Thanks for playing! Type {Fore.GREEN + '0' + Style.RESET_ALL} to play again, or {Fore.RED + '1' + Style.RESET_ALL} to quit.")
    finishGame()
  elif checkWin():
    render_board()
    print(
        Fore.GREEN + f"Player {Fore.RED + 'X' + Style.RESET_ALL if turn == 2 else Fore.BLUE + 'O'  + Style.RESET_ALL} Wins!" + Style.RESET_ALL)
    print(f"Game Over. Thanks for playing! Type {Fore.GREEN + '0' + Style.RESET_ALL} to play again, or {Fore.RED + '1' + Style.RESET_ALL} to quit.")
    finishGame()

  game()


def closeGame():
  raise SystemExit


def finishGame():
  action = input("Please choose your action: ")
  if action == "0":
    return create_new_board()
  elif action == "1":
    print("Thanks for playing!")
    closeGame()
  else:
    print("Invalid action. Please try again.")


def create_new_board():
  global TL, TM, TR, ML, MM, MR, BL, BM, BR, turn
  TL, TM, TR, ML, MM, MR, BL, BM, BR = "1", "2", "3", "4", "5", "6", "7", "8", "9"
  turn = 1
  game()


def render_board():
  global TL, TM, TR, ML, MM, MR, BL, BM, BR

  gameBoard = f"""
  -------------
  = {TL} = {TM} = {TR} =
  -------------
  = {ML} = {MM} = {MR} =
  -------------
  = {BL} = {BM} = {BR} =
  -------------
  """
  print(gameBoard)


def placeXO():
  if turn == 1:
    return Fore.RED + "X" + Style.RESET_ALL
  elif turn == 2:
    return Fore.BLUE + "O" + Style.RESET_ALL


def checkWin():
  win_conditions = [
      (0, 1, 2),  # Top row
      (3, 4, 5),  # Middle row
      (6, 7, 8),  # Bottom row
      (0, 3, 6),  # Left column
      (1, 4, 7),  # Middle column
      (2, 5, 8),  # Right column
      (0, 4, 8),  # Top-left to bottom-right diagonal
(2, 4, 6)   # Top-right to bottom-left diagonal
  ]

  board = [TL, TM, TR, ML, MM, MR, BL, BM, BR]

  for condition in win_conditions:
    if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != ' ':
        return True

  if all(position in [Fore.RED + "X" + Style.RESET_ALL, Fore.BLUE + "O" + Style.RESET_ALL] for position in board):
    return 'DRAW'

  return False

def toggle(turn):
  turn = 2 if turn == 1 else 1
  return turn


game()