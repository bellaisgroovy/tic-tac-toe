from unittest import TestCase
from unittest.mock import patch

from src.login.customer_login import CustomerLogin
from testing.login.data.loader.stub_json_loader import StubLoader


class TestCustomerLogin(TestCase):
    loader = StubLoader()
    customers = loader.get_obj_list()

    def test_findUserOrNone_validInput_customer(self):
        customers = self.customers

        customer = CustomerLogin.find_user_or_none(customers, customers[0].username, customers[0].password)

        self.assertEqual(customers[0], customer)

    def test_findUserOrNone_invalidInput_none(self):
        customers = self.customers

        customer = CustomerLogin.find_user_or_none(customers, 'notarealuser', customers[0].password)

        expected = None
        self.assertEqual(expected, customer)

    @patch(
        'src.login.customer_login.CustomerLogin.get_username_password',
        return_value=(customers[1].username, customers[1].password))
    def test_login_validInput_customer(self, mock_user_pwd):
        login = CustomerLogin(self.loader)

        customer = login.login()

        expected_customer = self.customers[1]
        self.assertEqual(expected_customer, customer)
