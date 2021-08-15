from urllib.parse import urlencode
from urllib.request import urlopen, Request
import json


class APIClient(object):
    def __init__(self, api_key):
        self.url = "https://commentanalyzer.googleapis.com/v1alpha1/{endpoint}"
        self.api_key = api_key

    def request(self, data, endpoint):
        formatted_url = self.url.format(endpoint=endpoint) + "?" + urlencode({'key': self.api_key})
        headers = {"Content-Type": "application/json"}
        data_str = json.dumps(data).encode("utf-8")
        request = Request(formatted_url, data=bytes(data_str), headers=headers, method="POST")
        response = urlopen(request)
        json_response = response.read().decode('utf-8')
        return json.loads(json_response)
