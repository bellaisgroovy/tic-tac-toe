class Loader:
    def __init__(self, obj, reader):
        self.obj = obj  # not instantiated to create many objects of this type
        self.reader = reader

    def get_obj_list(self, path):
        return

    def get_data(self, input_data):
        return self.reader.get_data(input_data)
