import unittest
from unittest.mock import patch, mock_open, MagicMock
import sys
sys.path.append('./src')
#sys.path.append('c:/Users/a.kailas.patil/OneDrive - Accenture/Desktop/Loan_management_system/loan_management_system/src')
from customer import add_customer, get_next_customer_id, get_customer

class TestCustomerModule(unittest.TestCase):
    @patch('customer.csv.writer')
    @patch('customer.open', new_callable=mock_open, read_data="1,John Doe,30,50000,700\n")
    def test_add_customer(self, mock_file, mock_csv_writer):
        customer_id = add_customer("Jane Doe", 25, 60000, 750)
        self.assertIsInstance(customer_id, int)
        mock_csv_writer.return_value.writerow.assert_called_with([2, "Jane Doe", 25, 60000, 750])

    @patch('customer.os.path.exists')
    @patch('customer.open', new_callable=mock_open, read_data="1,John Doe,30,50000,700\n")
    def test_get_next_customer_id(self, mock_file, mock_exists):
        mock_exists.return_value = True
        self.assertEqual(get_next_customer_id(), 2)
        mock_exists.return_value = False
        self.assertEqual(get_next_customer_id(), 1)

    @patch('customer.open', new_callable=mock_open, read_data="id,name,age,income,credit_score\n1,John Doe,30,50000,700\n")
    def test_get_customer_exists(self, mock_file):
        expected = {'id': 1, 'name': 'John Doe', 'age': 30, 'income': 50000.0, 'credit_score': 700}
        self.assertEqual(get_customer(1), expected)

    @patch('customer.open', new_callable=mock_open, read_data="id,name,age,income,credit_score\n1,John Doe,30,50000,700\n")
    def test_get_customer_not_exists(self, mock_file):
        self.assertIsNone(get_customer(2))

if __name__ == '__main__':
    unittest.main()