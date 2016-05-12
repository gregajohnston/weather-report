import re
from web_requester import WebRequester
from current_conditions import CurrentConditions
from ten_day_forecast import TenDayForecast
from astronomy import Astronomy
from alerts import Alerts
from current_hurricane import CurrentHurricane


__API_KEY = '0f0931639fcce419'
__CATEGORIES = ('conditions/forecast10day/astronomy/' +
                'alerts/currenthurricane')
class_list = [CurrentConditions, TenDayForecast, Astronomy,
              Alerts, CurrentHurricane]


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
    for item in class_list:
        item.format_output(weather_dict)
        # CurrentConditions.format_output(weather_dict)
        # TenDayForecast.format_output(weather_dict)
        # Astronomy.format_output(weather_dict)
        # Alerts.format_output(weather_dict)
    print('\n')

if __name__ == '__main__':
    main()
