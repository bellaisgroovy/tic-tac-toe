from src.login.data.customer import Customer
from src.login.data.loader.loader import Loader
from src.login.data.reader.reader import Reader


class StubLoader(Loader):
    def __init__(self,):
        super().__init__(None, Reader())

    def get_obj_list(self, path=None):
        customers = [
            Customer('7', 'spirofan77', 'dragond3zN00tz'),
            Customer('8', 'emmit', 'Kraggle'),
            Customer('9', 'eraserIHardly', 'kn0wH4r'),
        ]
        return customers
