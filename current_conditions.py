import requests
import json


class CurrentConditions:

    @staticmethod
    def web_query(request_url):
        response = requests.get(url=request_url)
        return response.text

    @staticmethod
    def parse_json(string):
        return json.loads(string)

    @staticmethod
    def return_conditions(request_url):
        string = CurrentConditions.web_query(request_url)
        dictionary = CurrentConditions.parse_json(string)
        return dictionary

    @staticmethod
    def format_output(request_url):
        dictionary = CurrentConditions.return_conditions(request_url)
        print("\nCurrent conditions:")
        print("The temperature is ", end='')
        print("{} degrees.".format(
            dictionary['current_observation']['temp_f']))
        print("Today there has been ", end='')
        print("{} precipitation today.".format(
            dictionary['current_observation']['precip_today_string']))
        print("The relative humidity is ", end='')
        print("{}.".format(
            dictionary['current_observation']['relative_humidity']))

# response = json.loads(r.content.decode('utf-8'))
# print(json.dumps(response, sort_keys=True, indent=4, separators=(',',': ')))


# features = {'alerts':'alerts/',
#             'almanac':'almanac/',
#             'astronomy':'astronomy/',
#             'conditions':'conditions/',
#             'currenthurricane':'currenthurricane/',
#             'forecast':'forecast/',
#             'forecast10day':'forecast10day/',
#             'geolookup':'geolookup/',
#             'history':'history/',
#             'hourly':'hourly/',
#             'hourly10day':'hourly10day/',
#             'planner':'planner/',
#             'rawtide':'rawtide/',
#             'tide':'tide/',
#             'webcams':'webcams/',
#             'yesterday':'yesterday/',
#             }
