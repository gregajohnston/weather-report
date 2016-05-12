import re


class Weather:

    @staticmethod
    def is_zip(zip_code):
        return (type(zip_code) is str and
                re.match(r'^[0-9]{5}$', zip_code))

    def welcome_user():
        print('Welcome to the Weather Forecaster!')
        print('Please enter your zip code:')
        zip_code = input('>')
        if Weather.is_zip(zip_code):
            return zip_code

    def main():
        pass

    if __name__ == '__main__':
        main()
