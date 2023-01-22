import board as board_module
import random


CORRECT_INPUT_OPTION = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3', 'quit']


def check_available_coordinate(board, x_y_tuple):
    if x_y_tuple in list_all_available_coordinates(board):
        return True
    return False


def list_all_available_coordinates(board):
    list_available_coordinates = []
    for row_index, row in enumerate(board):
        for item_index, item in enumerate(row):
            if item == '.':
                list_available_coordinates.append((row_index, item_index))
    return list_available_coordinates


def get_input_from_human():
    return input('Please choose place on board. ')


def validate_user_input(user_input):
    if user_input.lower() in CORRECT_INPUT_OPTION:
        return True
    else:
        return False

    
def quit_game():
    exit()

    
def user_input_to_coordinates(user_input):
    user_input = user_input.lower()
    list_woords = ['a', 'b', 'c']
    list_rows = [0, 1, 2]
    user_row = None

    zip_object = zip(list_woords, list_rows)
    for item in zip_object:
        if item[0] == user_input[0]:
            user_row = item[1]
    return (user_row, int(user_input[1])-1)


def warning_message_outside_board():
    print('You choose wrong place on the board')

    
def warning_msg_already_taken():
    print('This position was already taken')

    
def get_human_coordinates(board, current_player):
    while True:
        human_input = get_input_from_human()
        if validate_user_input(human_input):
            tuple_user_input = user_input_to_coordinates(human_input)
            print(tuple_user_input, list_all_available_coordinates(board))
            if check_available_coordinate(board, tuple_user_input):
                return tuple_user_input
            else:
                warning_msg_already_taken()
        else:
            warning_message_outside_board()

            
def get_random_ai_coordinates(board, current_player):
    if board_module.is_board_full(board):
        return None 
    return random.choice(list_all_available_coordinates(board))
    

if __name__ == "__main__":
  board_1 = [
    ["X", "X", "."],
    ["X", ".", "."],
    ["X", "X", "."],
  ]
  print("It should print the coordinates selected by the human player")
  coordinates = get_human_coordinates(board_1, "X")
  print(coordinates)

  board_2 = [
    ["O", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))
  print("The printed coordinate should be only (0,2) or (1,2)")
  print(get_random_ai_coordinates(board_2))

  board_3 = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "X"],
  ]
  print("The printed coordinate should be None")
  print(get_random_ai_coordinates(board_3))

  board_4 = [
    [".", "O", "."],
    ["X", "O", "."],
    ["X", "X", "O"],
  ]
  print("The printed coordinate should always be (0, 0)")
  print(get_unbeatable_ai_coordinates(board_4, "X")) 

  board_5 = [
    ["X", "O", "."],
    ["X", ".", "."],
    ["O", "O", "X"],
  ]
  print("The printed coordinate should always be (1, 1)")
  print(get_unbeatable_ai_coordinates(board_5, "O")) 

  board_6 = [
    ["O", "O", "."],
    ["O", "X", "."],
    [".", "X", "."],
  ]
  print("The printed coordinate should either (0, 2) or (2, 0)")
  print(get_unbeatable_ai_coordinates(board_6)) 
