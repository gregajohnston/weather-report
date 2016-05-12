class TenDayForecast:

    @staticmethod
    def format_output(dictionary):
        print('\n' + ('-'*50))
        print("Ten Day Forecast: \n")
        ten_list = dictionary['forecast']['txt_forecast']['forecastday']
        for item in ten_list:
            print('{}: '.format(item['title']), end='')
            print(item['fcttext'])
