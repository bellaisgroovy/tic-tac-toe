from src.login.data.reader.reader import Reader
import csv


class CsvReader(Reader):
    def get_data(self, data, obj):
        json_list = self.csv_to_json(data)
        obj_list = self.json_to_objs(json_list, obj)
        return obj_list

    @staticmethod
    def csv_to_json(path):
        json_list = []
        with open(path, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                json_list.append(row)
        return json_list

    @staticmethod
    def json_to_objs(json_list, obj):
        obj_list = []
        for record in json_list:
            instance = obj(**record)
            obj_list.append(instance)
        return obj_list
