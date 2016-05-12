class CurrentHurricane:

    @staticmethod
    def format_output(dictionary):
        hurricane_list = dictionary['currenthurricane']
        print('\n' + ('-'*50))
        print("Current hurricanes: \n")
        if hurricane_list == []:
            print("No active \'canes.")
        else:
            for hurricane in hurricane_list:
                print(hurricane['stormInfo']['stormName_Nice'])
