from src.login.data.loader.json_loader import JsonLoader
from src.login.data.customer import Customer
from testing.login.data.reader.stub_csv_reader import StubCsvReader, StubBadCsvReader, StubEmptyCsvReader
from src.login.data.reader.csv_reader import CsvReader
from unittest import TestCase


class TestJsonLoader(TestCase):
    def test_dataToObjList_stubReader_matchingObjList(self):
        loader = JsonLoader(obj=Customer, reader=StubCsvReader())
        path = 'arbitrary string'

        obj_list = loader.get_obj_list(path)

        json_list = StubCsvReader().get_data(None)
        expected_obj_list = [
            Customer(
                json_list[0]['customer_id'],
                json_list[0]['username'],
                json_list[0]['password'],
            ),
            Customer(
                json_list[1]['customer_id'],
                json_list[1]['username'],
                json_list[1]['password'],
            ),
            Customer(
                json_list[2]['customer_id'],
                json_list[2]['username'],
                json_list[2]['password'],
            ),
        ]
        self.assertEqual(expected_obj_list, obj_list)

    def test_dataToObjList_stubReaderBadData_skipsBadData(self):
        loader = JsonLoader(obj=Customer, reader=StubBadCsvReader())
        path = 'arbitrary string'

        obj_list = loader.get_obj_list(path)

        json_list = StubCsvReader().get_data(None)
        expected_obj_list = [
            Customer(
                json_list[1]['customer_id'],
                json_list[1]['username'],
                json_list[1]['password'],
            ),
            Customer(
                json_list[2]['customer_id'],
                json_list[2]['username'],
                json_list[2]['password'],
            ),
        ]
        self.assertEqual(expected_obj_list, obj_list)

    def test_dataToObjList_emptyData_emptyList(self):
        loader = JsonLoader(obj=Customer, reader=StubEmptyCsvReader())
        path = 'arbitrary string'

        obj_list = loader.get_obj_list(path)

        expected_obj_list = []
        self.assertEqual(expected_obj_list, obj_list)

    def test_dataToObjList_csvReader_matchingObjList(self):
        loader = JsonLoader(obj=Customer, reader=CsvReader())
        path = '../big_test_data.csv'

        obj_list = loader.get_obj_list(path)
        json_list = StubCsvReader().get_data(-1)
        expected_obj_list = [
            Customer(
                json_list[0]['customer_id'],
                json_list[0]['username'],
                json_list[0]['password'],
            ),
            Customer(
                json_list[1]['customer_id'],
                json_list[1]['username'],
                json_list[1]['password'],
            ),
            Customer(
                json_list[2]['customer_id'],
                json_list[2]['username'],
                json_list[2]['password'],
            ),
        ]
        self.assertEqual(expected_obj_list, obj_list)
