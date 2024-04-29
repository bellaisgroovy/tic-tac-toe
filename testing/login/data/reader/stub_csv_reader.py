from src.login.data.reader.csv_reader import CsvReader


class StubCsvReader(CsvReader):
    def get_data(self, input_data):
        fake_json = [
            {'customer_id': '0', 'username': 'weewoo', 'password': 'n333nawWW'},
            {'customer_id': '1', 'username': 'mr_strong', 'password': 'str0nk'},
            {'customer_id': '2', 'username': 'mames_nond', 'password': 'b0ndYul4ncE?'},
        ]
        return fake_json


class StubBadCsvReader(CsvReader):
    def get_data(self, input_data):
        fake_json = [
            {'customer_id': '0', 'username': 'weewoo'},
            {'customer_id': '1', 'username': 'mr_strong', 'password': 'str0nk'},
            {'customer_id': '2', 'username': 'mames_nond', 'password': 'b0ndYul4ncE?'},
        ]
        return fake_json


class StubEmptyCsvReader(CsvReader):
    def get_data(self, input_data):
        fake_json = []
        return fake_json
