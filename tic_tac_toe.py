from board import display_board, get_empty_board, is_board_full, get_winning_player, choose_player, check_player
from coordinates import get_human_coordinates, get_random_ai_coordinates, get_unbeatable_ai_coordinates
from menu import get_menu_option, clear_screen



HUMAN_VS_HUMAN = 1
RANDOM_AI_VS_RANDOM_AI = 2
HUMAN_VS_RANDOM_AI = 3
HUMAN_VS_UNBEATABLE_AI = 4


def choose_player_coordinates(board, current_player, game_mode):
    if game_mode == 1:
        return get_human_coordinates(board, current_player)
    elif game_mode == 2:
        return get_random_ai_coordinates(board, current_player)
    elif game_mode == 3 and current_player == 'O':
        return get_human_coordinates(board, current_player)
    elif game_mode == 3 and current_player == 'X':
        return get_random_ai_coordinates(board, current_player)

def check_end(board):
    if check_player(board, 'O') or check_player(board, 'X') or is_board_full(board):
        clear_screen()
        print(f'{get_winning_player(board)} won the game.')
        display_board(board)
        return True

def main():
    game_mode = get_menu_option()
    board = get_empty_board()
    is_game_running = True
    turn = 0

    while is_game_running:
        clear_screen()
        display_board(board)

        current_player = choose_player(turn)
        x, y = choose_player_coordinates(board, current_player, game_mode)

        board[x][y] = current_player
        
        if check_end(board):
            break
        turn += 1


if __name__ == "__main__":
    main()