import requests


class Weather:

    @staticmethod
    def web_query(request_url):
        response = requests.get(url=request_url)
        return response.text
