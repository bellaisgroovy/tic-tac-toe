from src.login_menu import LoginMenu
from src.tic_tac_toe.game.tic_tac_toe.normal_tic_tac_toe import NormalTicTacToe
from src.login.customer_login import CustomerLogin
from src.login.data.loader.json_loader import JsonLoader
from src.login.data.customer import Customer
from src.login.data.reader.csv_reader import CsvReader
from os import path


class Index:
    def __init__(self):
        customers_path = path.join(path.pardir, 'customers.csv')
        loader = JsonLoader(Customer, CsvReader())
        login = CustomerLogin(loader, customers_path)
        game = NormalTicTacToe()
        self.menu = LoginMenu(game, login)

    def start(self):
        while True:
            action = self.get_action()
            self.execute_action(action)

    def get_action(self):
        options = self.get_options()
        action = input(options).lower()
        return action

    def execute_action(self, action):
        if action == 'play' or action == 'p':
            self.menu.play()
        elif (action == 'login' or action == 'l') and self.menu.get_current_user() is None:
            self.menu.login()
        elif (action == 'logout' or action == 'l') and self.menu.get_current_user() is not None:
            self.menu.logout()
        elif action == 'quit' or action == 'q':
            self.menu.quit()
        else:
            print('Please input a listed option')

    def get_options(self):
        if self.menu.get_current_user() is None:
            options = '''
Please input a listed option.

Play
Login
Quit
'''
        else:
            options = f'''
Player : {self.menu.get_current_user()}

Please input a listed option.

Play
Logout
Quit
'''
        return options

if __name__ == '__main__':
    index = Index()
    index.start()

# customers_path = path.join(path.pardir, 'customers.csv')
# loader = JsonLoader(Customer, CsvReader())
# login = CustomerLogin(loader, customers_path)
# game = NormalTicTacToe()
# menu = LoginMenu(game, login)
#
#
# print('Welcome to Tic-Tac-Toe')
# while True:
#     if menu.get_current_user() is None:
#         options = '''
# Please input a listed option.
#
# Play
# Login
# Quit
# '''
#     else:
#         options = f'''
# Player : {menu.get_current_user()}
#
# Please input a listed option.
#
# Play
# Logout
# Quit
# '''
#
#     action = input(options).lower()
#
#     if action == 'play' or action == 'p':
#         menu.play()
#     elif (action == 'login' or action == 'l') and menu.get_current_user() is None:
#         menu.login()
#     elif (action == 'logout' or action == 'l') and menu.get_current_user() is not None:
#         menu.logout()
#     elif action == 'quit' or action == 'q':
#         menu.quit()
#     else:
#         print('Please input a listed option')
