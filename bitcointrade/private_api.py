from .errors import ArgumentError
from .utils import check_args

from .api import Base

class PrivateApi(Base):
    def __init__(self, token):
        Base.__init__(self)
        self.token = token
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "ApiToken "+self.token}

    # Bitcoin API type

    def bitcoin_withdraw_fee(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#cd0b440a-109b-80b3-9df6-8f3a0b10e32f
        Returns fee estimates for each confirmation speed category
        """
        return self.get_api("bitcoin","withdraw/fee", **params)

    def bitcoin_withdraw_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#2f4b6643-ae82-d9a3-8cb9-d025e92982fe
        Returns users withdrawals list
        Optional arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: pending/confirmed/canceled
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_date": str,
                                                "end_date": str,
                                                "status": ["pending","confirmed","canceled"],
                                                "page_size": int,
                                                "current_page": int})
        return self.get_api("bitcoin","withdraw", **params)

    def bitcoin_create_withdraw(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#0f218e0f-89a3-0b16-a670-6582ae858b1a
        Withdraws bitcoins to requested address
        Arguments:
        :param str destination: wallet address to process withdrawal
        :param float fee: amount to pay for transaction fees
        :param str fee_type: fast / regular / slow
        :param float amount: amount to send
        """
        check_args(params, {"destination": str,
                            "fee": float,
                            "fee_type":["fast","regular","slow"],
                            "amount": float})
        return self.post_api("bitcoin","withdraw", **params)

    def bitcoin_deposit_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#34810ae9-69e0-8c83-5c61-01d81162be10
        Returns users deposits list
        Optional arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: confirmation_pending / confirmed / canceled
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_date": str,
                                                "end_date": str,
                                                "status": ["confirmation_pending","confirmed","canceled"],
                                                "page_size": int,
                                                "current_page": int})
        return self.get_api("bitcoin","deposits", **params)

    # Market API type

    def orderbook_full(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#7aa82620-f7a2-7688-3081-bbb95afc3be3
        Returns buy orders, sell orders, and executed orders along with user codes
        Arguments:
        :param str currency: BTC/LTC/ETH/BCH
        """
        check_args(params, {"currency": ["BTC","LTC","BCH","ETH"]})
        return self.request_api_noaction("GET","market",**params)

    def summary(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#9a20d5e9-056b-7427-5f22-35f571f60411
        Returns market summary for a coin in the last 24 hours
        Arguments:
        :param str currency: BTC/LTC/ETH/BCH
        """
        check_args(params, {"currency": ["BTC", "LTC", "BCH", "ETH"]})
        return self.get_api("market","summary", **params)

    def create_order(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#caf0a4c9-8485-4b14-d162-2a38cc8440a9
        Creates an order
        Arguments:
        :param str currency: BTC/LTC/ETH/BCH
        :param float amount: amount of coins to buy/sell
        :param str type: buy/sell
        :param str subtype: market/limited
        :param float unit_price: how much to pay/earn (in BRL) per coin
        """
        check_args(params, { "currency": ["BTC","LTC","BCH","ETH"],
                             "amount": float,
                             "type":["buy","sell"],
                             "subtype":["market","limited"],
                             "unit_price": float })
        return self.post_api("market","create_order", **params)

    def get_user_orders(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#989dcc17-e4fa-1262-fa35-589d47dd6b43
        Get your users orders
        Optional arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: executed_completely / executed_partially / waiting / canceled
        :param str type: buy / sell
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        :param str currency: BTC/LTC/ETH/BCH
        """
        check_args(params, optional_parameters={"start_date": str,
                                                "end_date": str,
                                                "status": ["executed_completely","executed_partially","waiting","canceled"],
                                                "type": ["buy","sell"],
                                                "page_size": int,
                                                "current_page": int,
                                                "currency": ["BTC", "LTC", "BCH", "ETH"]})
        return self.get_api("market","user_orders/list", **params)

    def cancel_order(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#8d1745de-d21e-1478-9dfc-dd6f2a381cd1
        Cancel specified order
        Arguments:
        :param str id: order id
        """
        check_args(params, { "id": str })
        return self.request_api("DELETE","market","user_orders", **params)

    def estimated_price(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#c3fbdb41-fdd6-108c-753d-5efcfeff7a7e
        Calculates a price for market buying or selling specified amount
        Arguments:
        :param str currency: BTC/LTC/ETH/BCH
        :param float amount: amount of coins to buy/sell
        :param str type: buy/sell
        """
        check_args(params, {"currency": ["BTC","LTC","BCH","ETH"],
                            "amount": float,
                            "type": ["buy", "sell"]})
        return self.get_api("market","estimated_price", **params)

    #Wallets API type

    def balance(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#5ef0088b-40ef-4668-2ac4-59e0b94e91f7
        Returns available balances
        """
        return self.get_api("wallets","balance", **params)

    # Ethereum API type (why arent all coins parameters in a single endpoint? \_("/)_/)

    def ethereum_withdraw_fee(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#7c467985-794b-42a3-b356-1e6193a64322
        Returns fee estimates for each confirmation speed category
        """
        return self.get_api("ethereum","withdraw/fee", **params)

    def ethereum_withdraw_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#811ba44d-28dd-483f-ba2f-762974dca1d5
        Returns users withdrawals list
        Optional arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: pending/confirmed/canceled
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_date": str,
                                                "end_date": str,
                                                "status": ["pending","confirmed","canceled"],
                                                "page_size": int,
                                                "current_page": int})
        return self.get_api("ethereum","withdraw", **params)

    def ethereum_create_withdraw(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#74fa9c02-d356-4ea8-bf9a-27947c94b58a
        Withdraws ethereum to requested address
        Arguments:
        :param str destination: wallet address to process withdrawal
        :param float fee: amount to pay for transaction fees
        :param str fee_type: fast / regular / slow
        :param float amount: amount to send
        """
        check_args(params, {"destination": str,
                            "fee": float,
                            "fee_type":["fast","regular","slow"],
                            "amount": float})
        return self.post_api("ethereum","withdraw", **params)

    def ethereum_deposit_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#a91988b5-7fe2-4fed-82de-8c66116c2400
        Returns users deposits list
        Optional arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: confirmation_pending / confirmed / canceled
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_date": str,
                                                "end_date": str,
                                                "status": ["confirmation_pending","confirmed","canceled"],
                                                "page_size": int,
                                                "current_page": int})
        return self.get_api("ethereum","deposits", **params)

    # Litecoin API type

    def litecoin_withdraw_fee(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#e5890f51-4ae9-4c7a-bc87-de9d38f8aeaf
        Returns fee estimates for each confirmation speed category
        """
        return self.get_api("litecoin","withdraw/fee", **params)

    def litecoin_withdraw_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#23c9c7e3-2483-4c50-a7f5-5da33b65e815
        Returns users withdrawals list
        Optional arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: pending/confirmed/canceled
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_date": str,
                                                "end_date": str,
                                                "status": ["pending","confirmed","canceled"],
                                                "page_size": int,
                                                "current_page": int})
        return self.get_api("litecoin","withdraw", **params)

    def litecoin_create_withdraw(self, **params):
        """
        https://api.bitcointrade.com.br/v1/litecoin/withdraw
        Withdraws litecoin to requested address
        Arguments:
        :param str destination: wallet address to process withdrawal
        :param float fee: amount to pay for transaction fees
        :param str fee_type: fast / regular / slow
        :param float amount: amount to send
        """
        check_args(params, {"destination": str,
                            "fee": float,
                            "fee_type":["fast","regular","slow"],
                            "amount": float})
        return self.post_api("litecoin","withdraw", **params)

    def litecoin_deposit_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#24250a34-37e1-48cd-9961-bb66e1e1f186
        Returns users deposits list
        Optional arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: confirmation_pending / confirmed / canceled
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_date": str,
                                                "end_date": str,
                                                "status": ["confirmation_pending","confirmed","canceled"],
                                                "page_size": int,
                                                "current_page": int})
        return self.get_api("litecoin","deposits", **params)



