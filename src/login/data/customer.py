class Customer:
    def __init__(self, customer_id, username, password):
        self.customer_id = customer_id
        self.username = username
        self.password = password

    def __eq__(self, other):
        id_equ = self.customer_id == other.customer_id
        user_equ = self.username == other.username
        pwd_equ = self.password == other.password
        return  id_equ and user_equ and pwd_equ
