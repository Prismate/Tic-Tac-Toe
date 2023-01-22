import os


POSSIBLE_OPTIONS = [1, 2, 3, 4]


def clear_screen():
    os.system('clear')

    
def get_user_input():
    try:
        user_input = int(input('Please enter a number from 1 to 4: '))
        return user_input
    except:
        return None

    
def print_menu():
    print('1. Human vs Human\n2. Random AI vs Random AI\n3. Human vs Random AI\n4. Human vs Unbeatable AI')

    
def get_menu_option():
    while True:
        print_menu()
        user_input = get_user_input()
        if user_input is not None and user_input in POSSIBLE_OPTIONS:
          return user_input
        else:
          print('\nYou choose wrong option, please choose again.\n')


if __name__ == "__main__":
    # run this file to test you have implemented correctly the function
    option = get_menu_option()
    print("If the user selected 1, it should print 1")
    print(option) 
