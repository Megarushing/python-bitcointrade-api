import requests
import json
from .utils import check_args

from .api import Base
from .errors import ApiError

class PrivateApi(Base):
    def __init__(self, token):
        Base.__init__(self)
        self.token = token
        self.headers = {"Content-Type": "application/json",
                        "Authorization": "ApiToken "+self.token}

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
        Possible arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: pending/confirmed/canceled
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_date": str, "end_date": str,
                            "status": ["pending","confirmed","canceled"], "page_size": int, "current_page": int})
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
        check_args(params, {"destination": str,"fee": str,"fee_type":["fast","regular","slow"], "amount": float})
        return self.post_api("bitcoin","withdraw", **params)

    def bitcoin_deposit_list(self, **params):
        """
        https://apidocs.bitcointrade.com.br/#34810ae9-69e0-8c83-5c61-01d81162be10
        Returns users deposits list
        Possible arguments:
        :param str start_date: (ISO-8601 optional)
        :param str end_date: (ISO-8601 optional)
        :param str status: confirmation_pending / confirmed / canceled
        :param int page_size: (1-1000 optional)
        :param int current_page: (numeric optional)
        """
        check_args(params, optional_parameters={"start_date": str, "end_date": str,
                            "status": ["confirmation_pending","confirmed","canceled"], "page_size": int, "current_page": int})
        return self.get_api("bitcoin","deposits", **params)

