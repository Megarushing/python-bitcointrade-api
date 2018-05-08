import requests
import json

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

class PrivateApi(Base):
    def __init__(self, token=None):
        Base.__init__(self)
        self.token = token

    def list_orderbook(self, **kwargs):
        """https://api.bitcointrade.com.br/v1/market?currency=BTC"""
        check_args(kwargs, {"currency": ["BTC","LTC","BCH","ETH"]})
        return self.__check_response(self.__get_tapi("market","", kwargs ))

    def create_order(self, **kwargs):
        """https://api.bitcointrade.com.br/v1/market/create_order"""
        check_args(kwargs, { "currency": ["BTC","LTC","BCH","ETH"], "amount": str, "type":["buy","sell"],"subtype":["market","limited"], "unit_price": str })
        return self.__check_response(self.__post_tapi("market","/create_order", kwargs ))

    def balance(self, **kwargs):
        """https://api.bitcointrade.com.br/v1/wallets/balance"""
        return self.__check_response(self.__get_tapi("wallets","/balance", kwargs ))

    def estimated_price(self, **kwargs):
        """https://api.bitcointrade.com.br/v1/market/estimated_price?amount=583.23&currency=BTC&type=buy"""
        check_args(kwargs, {"currency": ["BTC","LTC","BCH","ETH"], "amount": str, "type": ["buy", "sell"]})
        return self.__check_response(self.__get_tapi("market","/estimated_price", kwargs ))

    def bitcoin_withdraw_fee(self, **kwargs):
        """https://api.bitcointrade.com.br/v1/bitcoin/withdraw/fee"""
        return self.__check_response(self.__get_tapi("bitcoin","/withdraw/fee", kwargs ))

    def ethereum_withdraw_fee(self, **kwargs):
        """https://api.bitcointrade.com.br/v1/ethereum/withdraw/fee"""
        return self.__check_response(self.__get_tapi("ethereum","/withdraw/fee", kwargs ))


    def bitcoin_create_withdraw(self, **kwargs):
        """https://api.bitcointrade.com.br/v1/bitcoin/withdraw"""
        check_args(kwargs, {"destination": str,"fee": str,"fee_type":["fast","regular","slow"], "amount": str })
        return self.__check_response(self.__post_tapi("bitcoin","/withdraw", kwargs ))

    def __check_response(self, response):
        if response["message"] != None:
            raise ApiError(response["message"])
        return response

    def __get_tapi(self, api_type, action, params={}):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "ApiToken "+self.token
        }

        response = requests.get("https://%s/%s/%s%s" % (self.host, self.api_version,api_type,action),params=params, headers=headers, timeout=30)
        return response.json()

    def __post_tapi(self, api_type, action, params={}):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "ApiToken "+self.token
        }

        response = requests.post("https://%s/%s/%s%s" % (self.host, self.api_version,api_type,action),data=json.dumps(params), headers=headers, timeout=30)
        return response.json()

