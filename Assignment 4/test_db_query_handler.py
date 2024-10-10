import unittest
from unittest.mock import patch
from db_error_handling import get_all_libraries

class TestGetAllLibraries(unittest.TestCase):

    @patch('db_error_handling.execute_query')
    @patch('db_error_handling._get_headers')
    def test_get_all_libraries_success(self, mock_get_headers, mock_execute_query):
        mock_get_headers.return_value = ['id', 'location', 'address', 'phone_number', 'website', 'email']

        mock_execute_query.return_value = [
            (1, 'Stratford-upon-Avon', 'Shakespeare Ave, Stratford-upon-Avon, CV37 6GP', '01789 293 485',
              'www.stratfordlibrary.co.uk', 'info@stratfordlibrary.co.uk'),
            (2, 'Warwick', 'Market Place, Warwick, CV34 4SA', '01926 492 212', 'www.warwicklibrary.co.uk',
             'info@warwicklibrary.co.uk'),
            (3, 'Leamington Spa', 'The Parade, Leamington Spa, CV32 4AT', '01926 742 700',
             'www.leamingtonlibrary.co.uk', 'info@leamingtonlibrary.co.uk'),
            (4, 'Henley-in-Arden', 'High Street, Henley-in-Arden, B95 5BX', '01564 792 355', 'www.henleylibrary.co.uk',
             'info@henleylibrary.co.uk')
        ]

        expected_result = [
            {'id': 1, 'location': "Stratford-upon-Avon", 'address': "Shakespeare Ave, Stratford-upon-Avon, CV37 6GP", 'phone_number': "01789 293 485", 'website': "www.stratfordlibrary.co.uk", 'email': "info@stratfordlibrary.co.uk"},
            {'id': 2, 'location': "Warwick", 'address': "Market Place, Warwick, CV34 4SA", 'phone_number': "01926 492 212", 'website': "www.warwicklibrary.co.uk", 'email': "info@warwicklibrary.co.uk"},
            {'id': 3, 'location': "Leamington Spa", 'address': "The Parade, Leamington Spa, CV32 4AT", 'phone_number': "01926 742 700", 'website': "www.leamingtonlibrary.co.uk", 'email': "info@leamingtonlibrary.co.uk"},
            {'id': 4, 'location': "Henley-in-Arden", 'address': "High Street, Henley-in-Arden, B95 5BX", 'phone_number': "01564 792 355", 'website': "www.henleylibrary.co.uk", 'email': "info@henleylibrary.co.uk"}
        ]

        result = get_all_libraries()

        self.assertEqual(result, expected_result)

    @patch('db_error_handling.execute_query')
    def test_get_all_libraries_no_data_failure(self, mock_execute_query):
        mock_execute_query.return_value = []

        with self.assertRaises(Exception) as context:
            get_all_libraries()

        self.assertEqual(str(context.exception), "No libraries information found")

    @patch('db_error_handling.execute_query')
    def test_get_all_libraries_query_failure(self, mock_execute_query):
        mock_execute_query.side_effect = Exception("Database connection error")

        with self.assertRaises(Exception) as context:
            get_all_libraries()

        self.assertEqual(str(context.exception), "Database connection error")

if __name__ == '__main__':
    unittest.main()