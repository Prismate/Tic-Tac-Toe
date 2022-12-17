def get_empty_board():
    '''
    Should return a list with 3 sublists.
    Each sublist should contain 3 time the "." character
    '''
    board = [
      [".", ".", "."],
      [".", ".", "."],
      [".", ".", "."]
    ]
    return board

def return_board_as_string(board):
    """
    Should return the tic tac toe board in a format similar to
        1   2   3
      A   X | O | . 
        ---+---+---
      B   X | O | .
        --+---+---
      C   0 | X | . 
        --+---+---
    """
    A1 = board[0][0]
    A2 = board[0][1]
    A3 = board[0][2]
    B1 = board[1][0]
    B2 = board[1][1]
    B3 = board[1][2]
    C1 = board[2][0]
    C2 = board[2][1]
    C3 = board[2][2]
    
    return f"   1   2   3\nA  {A1} | {A2} | {A3}\n  ---+---+---\nB  {B1} | {B2} | {B3}\n  ---+---+---\nC  {C1} | {C2} | {C3}"

def display_board(board):
    print(return_board_as_string(board))

def is_board_full(board):
  '''
  should return True if there are no more empty place on the board,
  otherwise should return False
  '''
  for i in range(0, len(board)):
      for j in range(0, len(board[0])):
          if board[i][j] == '.': 
              return False
  return True

def check_left_diagonal(board, char):
    '''
    input: 
    - board [[][][]]
    - char of player (O or X)
    output:
    - True or False
    '''
    for row_index in range(0, len(board)):
        if board[row_index][row_index] != char:
            return False
    return True

def check_right_diagonal(board, char):
    '''
    input: 
    - board [[][][]]
    - char of player (O or X)
    output:
    - True or False
    '''
    for row_index in range(0, len(board)):
        if board[-row_index-1][row_index] != char:
            return False
    return True

def check_rows(board, char):
    '''
    input: 
    - board [[][][]]
    - char of player (O or X)
    output:
    - True or False
    '''
    for i in range(len(board)):
        counter = 0
        for j in range(len(board[0])):
            if board[i][j] == char:
                counter += 1 
        if counter == 3:
            return True
    return False

def check_columns(board, char):
    '''
    input: 
    - board [[][][]]
    - char of player (O or X)
    output:
    - True or False
    '''
    for col_index in range(0, len(board)):
        if board[0][col_index] == char and board[1][col_index] == char and board[2][col_index] == char:
            return True
    return False


def check_player(board, char):
    if (check_columns(board, char) or check_rows(board, char) or check_left_diagonal(board, char) or check_right_diagonal(board, char)):
        return True
    else:
        return False

def get_winning_player(board):
    """
    Should return the player that wins based on the tic tac toe rules.
    If no player has won, than "None" is returned.
    """
    player_x = 'X'
    player_o = 'O'
    if check_player(board, player_x) and check_player(board, player_o):
        return None
    elif check_player(board, player_x):
        return player_x
    elif check_player(board, player_o):
        return player_o
    else:
        return None

def choose_player(turn_number):
    if turn_number % 2 == 0:
        return 'O'
    else:
        return 'X'