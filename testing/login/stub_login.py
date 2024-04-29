from src.login.login import Login
from src.login.data.customer import Customer


class StubLogin(Login):
    def __init__(self):
        return

    def login(self):
        return Customer(customer_id=0, username='bella123', password='secret')
