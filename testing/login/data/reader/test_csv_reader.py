from unittest import TestCase
from src.login.data.reader.csv_reader import CsvReader
from src.login.data.customer import Customer


class TestCsvReader(TestCase):
    def test_csvToJson_1validRecord_matchingJson(self):
        reader = CsvReader()

        json_list = reader.csv_to_json(path='../test_data.csv')

        expected_json = [{'customer_id': '0', 'username': 'bellaisgroovy', 'password': 'basilplant'}]
        self.assertEqual(expected_json, json_list)

    def test_csvToJson_3validRecords_matchingJson(self):
        reader = CsvReader()

        json_list = reader.csv_to_json(path='../big_test_data.csv')

        expected_json = [
            {'customer_id': '0', 'username': 'weewoo', 'password': 'n333nawWW'},
            {'customer_id': '1', 'username': 'mr_strong', 'password': 'str0nk'},
            {'customer_id': '2', 'username': 'mames_nond', 'password': 'b0ndYul4ncE?'},
        ]
        self.assertEqual(expected_json, json_list)


