import requests

class Base(object):
    """Base API Class"""

    def __init__(self):
        self.host = "api.bitcointrade.com.br"
        self.api_version = "v1"

    def get_api(self, api_type, action):
        """Returns api json for requested action.

        param action: The requested API action
        """
        response = requests.get("https://%s/%s/%s/%s" % (self.host, self.api_version,api_type,action),timeout=30)
        return response.json()

class Api(Base):
    """Bitcoin and Litcoin market informations."""

    def ticker(self,coin):
        """Returns informations about Bitcoin market."""
        return self.get_api("public",coin.upper()+'/ticker')

    def orderbook(self,coin):
        """Returns the Bitcoin's orderbook."""
        return self.get_api("public",coin.upper()+'/orders')

    def trades(self,coin):
        """Returns the operation list for the Bitcoin market."""
        return self.get_api("public",coin.upper()+'/trades')

