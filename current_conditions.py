class CurrentConditions:

    @staticmethod
    def format_output(dictionary):
        print('\n' + ('-'*50))
        print("Current conditions: \n")
        print("Temperature of {} degrees F".format(
            dictionary['current_observation']['temp_f']))
        print("Precipitation of {} today".format(
            dictionary['current_observation']['precip_today_string']))
        print("Relative humidity of {}%".format(
            dictionary['current_observation']['relative_humidity']))
        print("Feels like {} degrees F".format(
            dictionary['current_observation']['feelslike_f']))
