import requests
import json


class WebRequester:

    @staticmethod
    def web_query(request_url):
        response = requests.get(url=request_url)
        return response.text

    @staticmethod
    def parse_json(string):
        return json.loads(string)

    @staticmethod
    def return_weather_info(request_url):
        string = WebRequester.web_query(request_url)
        dictionary = WebRequester.parse_json(string)
        return dictionary
