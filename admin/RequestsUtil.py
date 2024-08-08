import requests
from enum import Enum

class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"

class RequestsUtil:
    def __init__(self, base_url, default_headers=None):
        self.base_url = base_url
        self.default_headers = default_headers or {}

    def make_request(self, method, endpoint, data=None, params=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **(headers or {})}
        response = None

        try:
            if method == HttpMethod.GET:
                response = requests.get(url, params=params, headers=headers, data=data)
            elif method == HttpMethod.POST:
                response = requests.post(url, data=data, params=params, headers=headers)
            elif method == HttpMethod.PUT:
                response = requests.put(url, data=data, params=params, headers=headers)
            elif method == HttpMethod.DELETE:
                response = requests.delete(url, params=params, headers=headers, data=data)

            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            if response:
                print(f"Response Content: {response.text}")
            return None

        return response
