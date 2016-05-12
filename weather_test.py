import unittest
import requests_mock

from web_requester import WebRequester
from weather import is_zip


class TestStringMethods(unittest.TestCase):

    def test_is_zip(self):
        self.assertTrue(is_zip('12345'))

    def test_is_not_zip_long(self):
        self.assertFalse(is_zip('012345'))

    def test_is_not_zip_alpha(self):
        self.assertFalse(is_zip('012c45'))

    def test_is_not_zip_numeric(self):
        self.assertFalse(is_zip(12345))

    def test_parse_json(self):
        json_file = '{"employees": [ \
            {"firstName": "John", "lastName": "Doe"}, \
            {"firstName": "Anna", "lastName": "Smith"} \
            ]}'
        self.assertTrue(WebRequester.parse_json(json_file), type(dict))

    @requests_mock.mock()
    def test_web_query(self, mock):
        mock.get('http://fake.com', text='data')
        self.assertEqual(
                WebRequester.web_query('http://fake.com'),
                'data')


if __name__ == '__main__':
    unittest.main()
