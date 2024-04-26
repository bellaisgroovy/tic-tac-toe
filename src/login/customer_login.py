from src.login.login import Login
from os import getcwd, path


class CustomerLogin(Login):
    def __init__(self, loader):
        super().__init__(loader)

    def login(self):
        customers = self.get_obj_list(path.join(getcwd(), 'customers.csv'))

        user = None
        while user is None:
            username, password = self.get_username_password()
            user = self.find_user_or_none(customers, username, password)
            if user is None:
                print('no user with those details')

        return user

    @staticmethod
    def get_username_password():
        username = input('username : ')
        password = input('password : ')
        return username, password

    @staticmethod
    def find_user_or_none(customers, username, password):
        for customer in customers:
            if customer.username == username and customer.password == password:
                return customer
        return None
