class Alerts:

    @staticmethod
    def format_output(dictionary):
        alert_list = dictionary['alerts']
        print('\n' + ('-'*50))
        print("Alerts: \n")
        if alert_list == []:
            print('No active weather alerts.')
        else:
            for item in alert_list:
                print('{} '.format(item['description']), end='')
                print('until {}'.format(item['expires']))
