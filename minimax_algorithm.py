import board as board_module


def list_all_available_coordinates(board):
    list_available_coordinates = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if item == '.':
                list_available_coordinates.append((row_index, item_index))
    return list_available_coordinates


def make_move(x_y_tuple, board, char):
    board[x_y_tuple[0]][x_y_tuple[1]] = char

    
def undo_move(x_y_tuple, board):
    board[x_y_tuple[0]][x_y_tuple[1]] = '.'

    
def is_board_full(board):
  for i in range(0, len(board)):
      for j in range(0, len(board[0])):
          if board[i][j] == '.': 
              return False
  return True


def minimax(maximazing, board, char):
    if board_module.check_player(board, char) or is_board_full(board):
        if board_module.get_winning_player(board) is None:
            return 0
        elif board_module.get_winning_player(board) == char:
            return 1
        else:
            return -1
    scores = []
    for move in list_all_available_coordinates(board):
        print(move, scores)
        make_move(move, board)
        print('first board:', board)
        scores.append(minimax(not maximazing, board, char))
        undo_move(move, board)
        print('second board: ', board)
    
    if maximazing:
        return max(scores)
    else:
        return min(scores)

    
def minimax2(is_maximizing, board, char):
    if board_module.check_player(board, char) or is_board_full(board) or board_module.check_player(board, 'O'):
        if board_module.get_winning_player(board) is None:
            print('end of tree')
            return 0
        elif board_module.get_winning_player(board) == char:
            score = 1
            print('player X won!', score, board)
            return score
        else:
            print('end of tree')
            return -1

    print('board: ', board)

    if is_maximizing:
        scores = []
        for move in list_all_available_coordinates(board):
            print(board, move, scores)
            make_move(move, board, 'X')
            scores.append(minimax2(is_maximizing=True, board=board, char=char))
            #undo_move(move, board)
        return max(scores)
    else:
        scores = []
        for move in list_all_available_coordinates(board):
            print(board, move, scores)
            make_move(move, board, 'O')
            scores.append(minimax2(is_maximizing=False, board=board, char='O'))
            #undo_move(move, board)
        return min(scores)


if __name__ == '__main__':
    print(minimax2(True, [['X', 'O', 'X'], ['.', 'X', '.'], ['.', '.', '.']], 'X'))
    #print(minimax(True, [['X', 'O', 'X'], ['.', 'X', '.'], ['.', '.', '.']], 'O'))
    
