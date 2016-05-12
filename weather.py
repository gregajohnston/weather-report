import re
from web_requester import WebRequester
from current_conditions import CurrentConditions
from ten_day_forecast import TenDayForecast


__API_KEY = '0f0931639fcce419'
__CATEGORIES = 'conditions/forecast10day/astronomy'


def create_url(api_key, category, zip_code):
    return ('http://api.wunderground.com/api/' + api_key +
            '/' + category + '/q/' + zip_code + '.json')


def is_zip(zip_string):
    return (type(zip_string) is str and
            re.match(r'^[0-9]{5}$', zip_string))


def welcome_user():
    print('Welcome to the Weather Forecaster!')
    print('Please enter your zip code:')
    zip_code = ''
    while not zip_code:
        zip_code = input('>')
        if is_zip(zip_code):
            return zip_code
        else:
            print('\"{}\"'.format(zip_code), end="")
            print('is not a valid input. Please try again.')
            zip_code = ''


def main():
    __zip_code = welcome_user()
    weather_url = create_url(__API_KEY, __CATEGORIES, __zip_code)
    weather_dict = WebRequester.return_weather_info(weather_url)
    CurrentConditions.format_output(weather_dict)
    TenDayForecast.format_output(weather_dict)


if __name__ == '__main__':
    main()
