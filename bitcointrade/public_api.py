import requests

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from .api import Base
from .errors import ApiError, ArgumentError


def check_values(value, arg, arg_value):
    if type(value) == type:
        if type(arg_value) != value:
            raise ArgumentError(u"Type of argument {} is invalid. It should be {}".format(arg, value))
    elif arg_value not in value:
        raise ArgumentError(u"Value of argument {} is invalid. It should be one of {}".format(arg, value))


def check_args(kwargs, required_parameters, optional_parameters={}):
    args = kwargs.keys()
    required_args = required_parameters.keys()
    optional_args = optional_parameters.keys()

    missing_args = list(set(required_args) - set(args))
    if len(missing_args) > 0:
        raise ArgumentError(u"Parameter {} is required".format(missing_args))

    for arg_name, arg_value in kwargs.items():
        if arg_name in optional_args:
            optional_value = optional_parameters[arg_name]
            check_values(optional_value, arg_name, arg_value)
        elif arg_name in required_args:
            required_value = required_parameters[arg_name]
            check_values(required_value, arg_name, arg_value)


class PublicApi(Base):
    def __init__(self, token=None):
        Base.__init__(self)
        self.token = token
        self.type = "market"

    def list_orderbook(self, **kwargs):
        """https://api.bitcointrade.com.br/v1/market?currency=BTC"""

        check_args(kwargs, {"currency": ["BTC","LTC","BCH","ETH"]})
        return self.__check_response(self.__post_papi("", kwargs ))

    def __check_response(self, response):
        print response
        if response["status_code"] == 100:
            return response["response_data"]
        else:
            raise ApiError(response["error_message"], response["status_code"])

    def __post_papi(self, action, params={}):
        headers = {
            "Content-Type": "application/json",
        }

        response = requests.get("https://%s/%s/%s%s" % (self.host, self.api_version,self.type,action),data=params, headers=headers, timeout=30)
        return response.json()

