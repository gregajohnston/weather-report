class CurrentHurricane:

    @staticmethod
    def format_output(dictionary):
        hurricane_list = dictionary['currenthurricane']
        print('\n' + ('-'*50))
        print("Current hurricanes: \n")
        for hurricane in hurricane_list:
            if hurricane['stormInfo']['stormName_Nice']:
                print(hurricane['stormInfo']['stormName_Nice'])
            else:
                print("No active \'canes.")
