import unittest
import requests_mock

from current_conditions import CurrentConditions
from weather import Weather


class TestStringMethods(unittest.TestCase):

    def test_is_zip(self):
        self.assertTrue(Weather.is_zip('12345'))

    def test_is_not_zip_long(self):
        self.assertFalse(Weather.is_zip('012345'))

    def test_is_not_zip_alpha(self):
        self.assertFalse(Weather.is_zip('012c45'))

    def test_is_not_zip_numeric(self):
        self.assertFalse(Weather.is_zip(12345))

    @requests_mock.mock()
    def test_web_query(self, mock):
        mock.get('http://fake.com', text='data')
        self.assertEqual(
                CurrentConditions.web_query('http://fake.com'),
                'data')


if __name__ == '__main__':
    unittest.main()
