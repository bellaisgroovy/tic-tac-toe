from src.login.data.reader.reader import Reader
import csv


class CsvReader(Reader):
    def get_data(self, input_data):
        json_list = self.csv_to_json(input_data)
        return json_list

    @staticmethod
    def csv_to_json(path):
        json_list = []
        with open(path, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                json_list.append(row)
        return json_list
