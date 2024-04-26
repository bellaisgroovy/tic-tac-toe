class Loader:
    def __init__(self, obj, reader):
        self.obj = obj
        self.reader = reader()

    def data_to_obj_list(self):
        return

    def get_data(self, input_data):
        return self.reader.get_data(input_data)
