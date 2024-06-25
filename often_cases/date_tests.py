import unittest

from often_cases.get_datetime import get_current_date
from unittest.mock import patch
from datetime import datetime


class TestGetCurrentDate(unittest.TestCase):

    @patch('often_cases.get_datetime.datetime')
    def test_get_date(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2024, 5, 20)

        self.assertEqual(get_current_date(), '2024-05-20')


if __name__ == '__main__':
    unittest.main()
