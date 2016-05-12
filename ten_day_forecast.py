class TenDayForecast:

    @staticmethod
    def format_output(dictionary):
        print('\n' + ('-'*50))
        print("Ten Day Forecast: \n")
        ten_list = dictionary['forecast']['txt_forecast']['forecastday']
        count = 0
        for item in ten_list:
            len_formatter = (20 - len(item['title'])) * ' '
            print('{}:{}'.format(item['title'], len_formatter), end='')
            print(item['fcttext'])
            count += 1
