import requests


def web_query(request_url):
    response = requests.get(url=request_url)
    return response.text


# # client.py
# import requests
#
# class MyAPIClient(object):
#     """A simple API client for querying corgi data"""
#
#     base_url = 'http://api.corgidata.com'
#     version = 'v1'
#
#     def _make_uri(self, resource):
#         """
#         Construct the URL for a resource based on the API class's parameters
#         """
#         return '/'.join([self.base_uri, self.version, resource])
#
#     def _get(self, url):
#         """Make a GET request to an endpoint defined by 'url'"""
#
#         response = requests.get(url=url)
#         return response.json()
#
#     def get_breed_info(self, breed):
#         """Return information about a specific breed of corgi"""
#         resource = '/'.join(['breeds', breed])
#         url = self._make_url(resource=resource)
#         response = self._get(url=url)
#         return response
