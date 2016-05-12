import re
from current_conditions import CurrentConditions


ZIP_URL = ''
API_KEY = '0f0931639fcce419'
CONDITIONS_URL = ''


def create_url(zip_code):
    return ('http://api.wunderground.com/api/{}'.format(API_KEY) +
            '/conditions/q/{}.json'.format(zip_code))


def is_zip(zip_code):
    return (type(zip_code) is str and
            re.match(r'^[0-9]{5}$', zip_code))


def welcome_user():
    print('Welcome to the Weather Forecaster!')
    print('Please enter your zip code:')
    while not ZIP_URL:
        zip_code = input('>')
        if is_zip(zip_code):
            return zip_code
        else:
            print('\"{}\"'.format(zip_code), end="")
            print('is not a valid input. Please try again.')


def main():
    ZIP_URL = welcome_user()
    CONDITIONS_URL = create_url(ZIP_URL)
    current_result = CurrentConditions.return_conditions(CONDITIONS_URL)
    print(current_result)

if __name__ == '__main__':
    main()
