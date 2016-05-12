class Alerts:

    @staticmethod
    def format_output(dictionary):
        alert_list = dictionary['alerts']
        print('\n' + ('-'*50))
        print("Alerts: \n")
        for item in alert_list:
            print('{} '.format(item['description']), end='')
            print('until {}'.format(item['expires']))
