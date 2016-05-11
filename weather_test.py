import unittest
import requests_mock

from weather import Weather


class TestStringMethods(unittest.TestCase):

    @requests_mock.mock()
    def test_web_query(self, mock):
        mock.get('http://fake.com', text='data')
        self.assertEqual(Weather.web_query('http://fake.com'), 'data')


if __name__ == '__main__':
    unittest.main()
