import unittest
import requests_mock

from current_conditions import CurrentConditions


class TestStringMethods(unittest.TestCase):

    @requests_mock.mock()
    def test_web_query(self, mock):
        mock.get('http://fake.com', text='data')
        self.assertEqual(
                CurrentConditions.web_query('http://fake.com'),
                'data')


if __name__ == '__main__':
    unittest.main()
