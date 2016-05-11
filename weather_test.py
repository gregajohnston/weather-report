import unittest
import requests_mock

from weather import web_query


class TestStringMethods(unittest.TestCase):

    @requests_mock.mock()
    def test_web_query(self, mock):
        mock.get('http://test.com', text='data')
        self.assertEqual(web_query('http://test.com'), 'data')


if __name__ == '__main__':
    unittest.main()
