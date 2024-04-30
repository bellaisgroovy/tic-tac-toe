from src.login.data.loader.loader import Loader


class JsonLoader(Loader):
    def __init__(self, obj, reader):
        super().__init__(obj, reader)

    def get_obj_list(self, path):
        obj_list = []
        for record in self.get_data(path):
            try:
                instance = self.obj(**record)  # creates instance with records data
                obj_list.append(instance)
            except TypeError:
                print('There is bad login data in customers.csv')
        return obj_list
