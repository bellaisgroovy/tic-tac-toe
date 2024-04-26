from src.login.data.loader.loader import Loader
from src.login.data.customer import Customer


class JsonLoader(Loader):
    def __init__(self, obj, reader):
        super().__init__(obj, reader)

    def data_to_obj_list(self, input_data):
        obj_list = []
        for record in self.get_data(input_data):
            instance = self.obj(**record)
            obj_list.append(instance)
        return obj_list

