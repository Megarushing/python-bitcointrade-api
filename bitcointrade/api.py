import requests
import json
from .utils import check_args
from .errors import ApiError
TIMEOUT = 30

class Base(object):
    """Base API Class"""

    def __init__(self):
        self.host = "api.bitcointrade.com.br"
        self.api_version = "v1"
        self.token = None
        self.headers = {"Content-Type": "application/json"}
        self.timeout = TIMEOUT

    def _check_response(self, response):
        try:
            r = response.json()
        except:
            response.raise_for_status()
        if not ("message" in r and "data" in r):
            raise ApiError("Invalid response: {}".format(r))
        if r["message"] != None:
            raise ApiError(r["message"])
        return r["data"]

    def request_api(self,method,api_type, action, **params):
        """
        Returns decoded json dict for requested action.
        :param str method: Http method used
        :param str api_type: The requested API action
        :param str action: The requested API action
        :param \*\*params: data sent to API.
        :return dict: decoded json received
        """
        filtered = {k: v for k, v in params.items() if v != None}
        url = "https://%s/%s/%s/%s" % (self.host,
                                       self.api_version,
                                       api_type,
                                       action)
        response = None
        if method.upper() == "GET":
            response = requests.get(url,params=filtered,timeout=self.timeout,headers=self.headers)
        else:
            response = requests.request(method,url,data=json.dumps(filtered),timeout=self.timeout,headers=self.headers)
        return self._check_response(response)

    def request_api_noaction(self,method,api_type, **params):
        """
        Returns decoded json dict for requested api type, does not take action as param.
        :param str method: Http method used
        :param str api_type: The requested API action
        :param \*\*params: data sent to API.
        :return dict: decoded json received
        """
        filtered = {k: v for k, v in params.items() if v != None}
        url = "https://%s/%s/%s" % (self.host,
                                       self.api_version,
                                       api_type)
        response = None
        if method.upper() == "GET":
            response = requests.get(url,params=filtered,timeout=self.timeout,headers=self.headers)
        else:
            response = requests.request(method,url,data=json.dumps(filtered),timeout=self.timeout,headers=self.headers)
        return self._check_response(response)

    def get_api(self, api_type, action, **params):
        """
        Returns decoded json dict for requested action.
        :param str api_type: The requested API action
        :param str action: The requested API action
        :param \*\*params: data sent to API encoded in url.
        :return dict: decoded json received
        """
        return self.request_api("GET", api_type, action, **params)

    def post_api(self, api_type, action, **params):
        """
        Returns decoded json dict for requested action.
        :param str api_type: The requested API action
        :param str action: The requested API action
        :param \*\*params: data sent to API in json form.
        :return dict: decoded json received
        """
        return self.request_api("POST", api_type, action, **params)

class Api(Base):
    """Coin market informations."""

    def get_api(self, api_type, coin, action, **params):
        """
        Returns decoded json dict for requested action.
        :param str api_type: The requested API action
        :param str action: The requested API action
        :param \*\*params: data sent to API encoded in url.
        :return dict: decoded json received
        """
        filtered = {k: v for k, v in params.items() if v != None}
        url = "https://%s/%s/%s/%s/%s" % (self.host,
                                       self.api_version,
                                       api_type,
                                       coin.upper(),
                                       action)

        response = requests.get(url,params=filtered,timeout=self.timeout,headers=self.headers)
        return self._check_response(response)

    def ticker(self,coin):
        """
        https://apidocs.bitcointrade.com.br/#8e6f6b73-b2f8-c03a-9d60-a0159f2c6ce0
        Returns a summary of last 24 hour trade period.
        """
        return self.get_api("public",coin,'ticker')

    def orderbook(self,coin):
        """
        https://apidocs.bitcointrade.com.br/#dc3695f5-6129-e35c-153d-c629aee8fd48
        Returns the orderbook for chosen coin.
        """
        return self.get_api("public",coin,'orders')

    def trades(self,coin,**params):
        """
        https://apidocs.bitcointrade.com.br/#9fe41816-3d20-e53e-9273-643c95279dc4
        Returns list of trades that happened during search period.
        Possible arguments:
        :param str start_time: (ISO-8601 optional)
        :param str end_time: (ISO-8601 optional)
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_time": str, "end_time": str,
                            "page_size": int, "current_page": int})
        return self.get_api("public",coin,'trades',**params)
