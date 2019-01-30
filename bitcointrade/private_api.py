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
        https://apidocs.bitcointrade.com.br/#76927020-dcd0-4fcd-824b-68fad1eef8d9
        Returns fee estimates for each confirmation speed category
        """
        return self.get_api("bitcoin","withdraw/fee", **params)

    def bitcoin_withdraw_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#65ddd60e-03ae-4c9c-9b35-c86c3f8a045f
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
        https://apidocs.bitcointrade.com.br/#36fa6277-5721-49dd-8b63-c24a8033469c
        Withdraws bitcoins to requested address
        Arguments:
        :param str destination: wallet address to process withdrawal
        :param str fee_type: fast / regular / slow
        :param float amount: amount to send
        """
        check_args(params, {"destination": str,
                            "fee_type":["fast","regular","slow"],
                            "amount": float})
        return self.post_api("bitcoin","withdraw", **params)

    def bitcoin_deposit_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#8a25aee8-c6ce-4c82-9a73-00061f3a40aa
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

    def bitcoin_sync_transaction(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#56df5135-fb53-4dab-8466-332e58807400
        BitcoinTrade is the first, pioneer exchange, to make a "gambiarra" official
        through it's API, this method syncronizes a bitcoin transaction
        based on its hash, this has to be done in case BitcoinTrade does not
        notice the deposit incoming to your wallet, in which case the deposit
        will only appear in your balance after using this method.
        Arguments:
        :param str hash: transaction hash to syncronize
        """
        check_args(params, {"hash": str})
        return self.post_api("bitcoin","sync_transaction", **params)

    # Market API type

    def orderbook_full(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#6cb6844d-1253-4b92-b259-abcf9237e19a
        Returns buy orders, sell orders, and executed orders along with user codes
        Arguments:
        :param str pair: BRLBTC/BRLLTC/BRLETH/BRLBCH
        """
        check_args(params, {"pair": ["BRLBTC","BRLLTC","BRLETH","BRLBCH"]})
        return self.request_api_noaction("GET","market",**params)

    def summary(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#33519517-e04c-414c-9aeb-cc7177dd5c4a
        Returns market summary for a coin in the last 24 hours
        Arguments:
        :param str pair: BRLBTC / BRLETH / BRLLTC / BRLBCH
        """
        check_args(params, {"pair": ["BRLBTC", "BRLLTC", "BRLBCH", "BRLETH"]})
        return self.get_api("market","summary", **params)

    def create_order(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#9ed16ef6-c2bd-459d-b0a6-9d7a56e944f3
        Creates an order
        Arguments:
        :param str pair: BRLBTC / BRLETH / BRLLTC / BRLBCH
        :param float amount: amount of coins to buy/sell
        :param str type: buy/sell
        :param str subtype: limited / market / stopLimit
        :param float unit_price: how much to pay/earn (in BRL) per coin
        :param float request_price: total order value, in limited orders this is ignored
        """
        check_args(params, { "pair": ["BRLBTC","BRLLTC","BRLBCH","BRLETH"],
                             "amount": float,
                             "type":["buy","sell"],
                             "subtype":["market","limited","stopLimit"],
                             "unit_price": float,
                             "request_price": float})

        return self.post_api("market","create_order", **params)

    def get_user_orders(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#91edc155-a911-46bc-a6e8-dd1f77b23c59
        Get your users orders
        Optional arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: executed_completely / executed_partially / waiting / canceled
        :param str type: buy / sell
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        :param str pair: BRLBTC / BRLETH / BRLLTC / BRLBCH
        """
        check_args(params, optional_parameters={"start_date": str,
                                                "end_date": str,
                                                "status": ["executed_completely","executed_partially","waiting","canceled"],
                                                "type": ["buy","sell"],
                                                "page_size": int,
                                                "current_page": int,
                                                "pair": ["BRLBTC", "BRLLTC", "BRLBCH", "BRLETH"]})
        return self.get_api("market","user_orders/list", **params)

    def cancel_order(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#4a20e870-18b1-4a3d-ad72-a14ecf449f74
        Cancel specified order
        Arguments:
        :param str id: order id
        """
        check_args(params, { "id": str })
        return self.request_api("DELETE","market","user_orders", **params)

    def estimated_price(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#62e55ae0-0c79-413e-9a87-6fb1b87072fa
        Calculates a price for market buying or selling specified amount
        Arguments:
        :param str pair: BRLBTC / BRLETH / BRLLTC / BRLBCH
        :param float amount: amount of coins to buy/sell
        :param str type: buy/sell
        """
        check_args(params, {"pair": ["BRLBTC", "BRLLTC", "BRLBCH", "BRLETH"],
                            "amount": float,
                            "type": ["buy", "sell"]})
        return self.get_api("market","estimated_price", **params)

    #Wallets API type

    def balance(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#3a8473a4-f536-4836-a5e2-db6f3bc4023f
        Returns available balances
        """
        return self.get_api("wallets","balance", **params)

    # Ethereum API type (why arent coins expressed as parameters in a single endpoint? no idea \_("/)_/)

    def ethereum_withdraw_fee(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#c6dd2a46-9e7c-454f-8ecd-b0d04cd844dc
        Returns fee estimates for each confirmation speed category
        """
        return self.get_api("ethereum","withdraw/fee", **params)

    def ethereum_withdraw_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#30f6745b-02da-480c-95ad-d18cc150d21b
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
        https://apidocs.bitcointrade.com.br/#a632d54c-34af-4b49-8d98-5c0824a2e3fc
        Withdraws ethereum to requested address
        Arguments:
        :param str destination: wallet address to process withdrawal
        :param float fee: amount to pay for transaction fees
        :param str fee_type: fast / regular / slow
        :param float amount: amount to send
        """
        check_args(params, {"destination": str,
                            "fee_type":["fast","regular","slow"],
                            "amount": float})
        return self.post_api("ethereum","withdraw", **params)

    def ethereum_deposit_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#9241164c-b898-4866-be86-56f0b48a90dd
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

    def ethereum_sync_transaction(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#18af112e-d135-4143-91a5-990215179685
        BitcoinTrade is the first, pioneer exchange, to make a "gambiarra" official
        through it's API, this method syncronizes an ethereum transaction
        based on its hash, this has to be done in case BitcoinTrade does not
        notice the deposit incoming to your wallet, in which case the deposit
        will only appear in your balance after using this method.
        Arguments:
        :param str hash: transaction hash to syncronize
        """
        check_args(params, {"hash": str})
        return self.post_api("ethereum","sync_transaction", **params)

    # Litecoin API type

    def litecoin_withdraw_fee(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#f8a4eed1-5ba5-4002-95f4-845414d466ae
        Returns fee estimates for each confirmation speed category
        """
        return self.get_api("litecoin","withdraw/fee", **params)

    def litecoin_withdraw_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#30f6745b-02da-480c-95ad-d18cc150d21b
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
        https://apidocs.bitcointrade.com.br/#f9418a69-afb1-4ebe-8c65-9dd85efd1012
        Withdraws litecoin to requested address
        Arguments:
        :param str destination: wallet address to process withdrawal
        :param str fee_type: fast / regular / slow
        :param float amount: amount to send
        """
        check_args(params, {"destination": str,
                            "fee_type":["fast","regular","slow"],
                            "amount": float})
        return self.post_api("litecoin","withdraw", **params)

    def litecoin_deposit_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#10a073a1-01ab-4d80-baa1-231f3c9aa2c1
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

    def litecoin_sync_transaction(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#254ef8fe-edf4-4a84-848e-38ec016bc683
        BitcoinTrade is the first, pioneer exchange, to make a "gambiarra" official
        through it's API, this method syncronizes a litecoin transaction
        based on its hash, this has to be done in case BitcoinTrade does not
        notice the deposit incoming to your wallet, in which case the deposit
        will only appear in your balance after using this method.
        Arguments:
        :param str hash: transaction hash to syncronize
        """
        check_args(params, {"hash": str})
        return self.post_api("litecoin","sync_transaction", **params)

    # Bitcoin Cash API type

    def bitcoincash_withdraw_fee(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#ed5a2265-17ed-4da1-89b5-7d3e824c3519
        Returns fee estimates for each confirmation speed category
        """
        return self.get_api("bitcoincash","withdraw/fee", **params)

    def bitcoincash_withdraw_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#d109d015-1933-4a5b-a591-b734856a46f9
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
        return self.get_api("bitcoincash","withdraw", **params)

    def bitcoincash_create_withdraw(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#aeebec0f-cb86-49b7-ab71-c522525e1550
        Withdraws litecoin to requested address
        Arguments:
        :param str destination: wallet address to process withdrawal
        :param str fee_type: fast / regular / slow
        :param float amount: amount to send
        """
        check_args(params, {"destination": str,
                            "fee_type":["fast","regular","slow"],
                            "amount": float})
        return self.post_api("bitcoincash","withdraw", **params)

    def bitcoincash_deposit_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#338f3f8e-4cb3-4cdb-96e1-c27aa43f3afe
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
        return self.get_api("bitcoincash","deposits", **params)

    def bitcoincash_sync_transaction(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#9e069b38-db8b-44af-ba87-5b2e3309d9f8
        BitcoinTrade is the first, pioneer exchange, to make a "gambiarra" official
        through it's API, this method syncronizes a litecoin transaction
        based on its hash, this has to be done in case BitcoinTrade does not
        notice the deposit incoming to your wallet, in which case the deposit
        will only appear in your balance after using this method.
        Arguments:
        :param str hash: transaction hash to syncronize
        """
        check_args(params, {"hash": str})
        return self.post_api("bitcoincash","sync_transaction", **params)

