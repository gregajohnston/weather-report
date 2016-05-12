class CurrentConditions:

    @staticmethod
    def format_output(dictionary):
        sunrise = dictionary['moon_phase']['sunrise']
        sunset = dictionary['moon_phase']['sunset']
        sunset['hour'] = int(sunset['hour']) - 12
        sunset['hour'] = str(sunset['hour'])
        print('\n' + ('-'*50))
        print("Astronomy: \n")
        print("Sunrise at {}:{} am".format(
            sunrise['hour'], sunrise['minute']))
        print("Sunset at {}:{} pm".format(
            sunset['hour'], sunrise['minute']))
