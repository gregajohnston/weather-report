class TenDayForecast:

    @staticmethod
    def format_output(dictionary):
        print('\n' + ('-'*50))
        print("Ten Day Forecast: ")
        print("{}".format(
            dictionary['forecast']['txt_forecast']['forecastday']))
