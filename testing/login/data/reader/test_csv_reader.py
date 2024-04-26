from unittest import TestCase
from src.login.data.reader.csv_reader import CsvReader
from src.login.data.customer import Customer


class MyTestCase(TestCase):
    def test_csvToJson_1validRecord_matchingJson(self):
        reader = CsvReader()

        json_list = reader.csv_to_json(path='test_data.csv')

        expected_json = [{'customer_id': '0', 'username': 'bellaisgroovy', 'password': 'basilplant'}]
        self.assertEqual(expected_json, json_list)

    def test_jsonToObjs_1validJson_matchingObj(self):
        reader = CsvReader()
        json_list = [{'customer_id': '0', 'username': 'bellaisgroovy', 'password': 'basilplant'}]
        obj = Customer

        obj_list = reader.json_to_objs(json_list, obj)

        expected_obj_list = [Customer(
            json_list[0]['customer_id'],
            json_list[0]['username'],
            json_list[0]['password'],
        )]

        self.assertEqual(expected_obj_list, obj_list)
