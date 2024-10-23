import unittest
from unittest.mock import patch
from client_fetch_data_helpers import fetch_data

BASE_URL = 'http://127.0.0.1:5000'

class TestApiFunctions(unittest.TestCase):
    @patch('requests.get')
    def test_fetch_data_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"key": "value"}]

        response = fetch_data(f'{BASE_URL}/libraries', "No available libraries")
        self.assertEqual(response, [{"key": "value"}])

    @patch('requests.get')
    def test_fetch_data_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        response = fetch_data(f'{BASE_URL}/libraries', "No available libraries")
        self.assertEqual(response, "No available libraries")

if __name__ == '__main__':
    unittest.main()