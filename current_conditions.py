class CurrentConditions:

    @staticmethod
    def format_output(dictionary):
        print('\n' + ('-'*50))
        print("Current conditions: ")
        print("{} degrees F".format(
            dictionary['current_observation']['temp_f']))
        print("{} precipitation today".format(
            dictionary['current_observation']['precip_today_string']))
        print("{} % rel humidity".format(
            dictionary['current_observation']['relative_humidity']))
