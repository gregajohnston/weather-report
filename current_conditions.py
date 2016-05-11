import requests


class CurrentConditions:

    @staticmethod
    def web_query(request_url):
        response = requests.get(url=request_url)
        return response.text
