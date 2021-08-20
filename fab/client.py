import json
import requests
from requests.adapters import HTTPAdapter

class Client(object):
    """
    The client for communicating with the API client.
    """
    def __init__(self, url=None, header=None):
        self.url = url if url is not None else "https://api.fabdb.net"
        self.header = header if header is not None else {"Accept": "application/json"}
        self.session = requests.Session()

    def __set_default_header(self):
        self.session.headers.update({"Accept": "application/json"})
    
    def _request(self, method: str, base_url: str, path: str, data=None, header=None):
        if path is not None and base_url is not None:
            url = "call format function here"
        elif path is not None and base_url is None:
            url = "call format function here with self.url"
        elif path is None:
            raise ValueError("The argument `path` cannot be None.")
        
        if data is not None:
            data = json.dumps(data)
        
        if header is not None:
            if not isinstance(header, dict):
                header = json.loads(header)
            self.session.headers.update(header)
        else:
            self.__set_default_header()
        
        response = self.session.request(method=method, url=url, data=data, headers=self.session.headers)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise(e)
        except requests.exceptions.RequestException as e:
            raise(e)
        except requests.exceptions.ConnectionError as e:
            raise(e)
        except requests.exceptions.Timeout as e:
            raise(e)
        
        if response.text != "":
            try:
                _response = response.json()
                while "next" in response.links.keys():
                    response = self.session.request(method=method, url=response.links["next"]["url"], data=data, headers=self.session.headers)
                    _response.extend(response.json())
                return _response
            except json.decoder.JSONDecodeError:
                return response.text
        else:
            return response.status_code


    def get(self, base_url: str = "", path: str = "", data=None, header=None):
        return self._request(method="GET", base_url=base_url, path=path, data=data, header=header)
    
    def post(self, base_url: str = "", path: str = "", data=None, header=None):
        return self._request(method="POST", base_url=base_url, path=path, data=data, header=header)
    
    def delete(self, base_url: str = "", path: str = "", data=None, header=None):
        return self._request(method="DELETE", base_url=base_url, path=path, data=data, header=header)
    
    def patch(self, base_url: str = "", path: str = "", data=None, header=None):
        return self._request(method="PATCH", base_url=base_url, path=path, data=data, header=header)
    
    def put(self, base_url: str = "", path: str = "", data=None, header=None):
        return self._request(method="PUT", base_url=base_url, path=path, data=data, header=header)

