import tests
import unittest
import bitcointrade
from bitcointrade.errors import ApiError, ArgumentError

def assert_order_response(response):
    assert "order" in response
    assert "status" in response["order"]
    assert "created_timestamp" in response["order"]
    assert "updated_timestamp" in response["order"]
    assert "coin_pair" in response["order"]
    assert "has_fills" in response["order"]
    assert "quantity" in response["order"]
    assert "executed_quantity" in response["order"]
    assert "order_id" in response["order"]
    assert "operations" in response["order"]
    assert "order_type" in response["order"]
    assert "executed_price_avg" in response["order"]
    assert "fee" in response["order"]
    assert "limit_price" in response["order"]

class PrivateApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = bitcointrade.PrivateApi("42")

    @tests.vcr.use_cassette
    def test_bitcoin_withdraw_fee(self):
        response = self.api.bitcoin_withdraw_fee()
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_bitcoin_withdraw_list(self):
        response = self.api.bitcoin_withdraw_list()
        assert "messages" in response

    # @tests.vcr.use_cassette
    # def test_bitcoin_create_withdraw(self):
    #     response = self.api.bitcoin_create_withdraw(
    #         destination="1FSzwTdndhtbjGtRTKiu2vQHHrVAPUGSZG",
    #         fee=0.0001,
    #         type="fast",
    #         amount=0.1)
    #     assert "messages" in response

    @tests.vcr.use_cassette
    def test_bitcoin_deposit_list(self):
        response = self.api.bitcoin_deposit_list()
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_ethereum_withdraw_fee(self):
        response = self.api.ethereum_withdraw_fee()
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_ethereum_withdraw_list(self):
        response = self.api.ethereum_withdraw_list()
        assert "messages" in response

    # @tests.vcr.use_cassette
    # def test_ethereum_create_withdraw(self):
    #     response = self.api.ethereum_create_withdraw(
    #         destination="1FSzwTdndhtbjGtRTKiu2vQHHrVAPUGSZG",
    #         fee=0.0001,
    #         type="fast",
    #         amount=0.1)
    #     assert "messages" in response

    @tests.vcr.use_cassette
    def test_ethereum_deposit_list(self):
        response = self.api.ethereum_deposit_list()
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_litecoin_withdraw_fee(self):
        response = self.api.litecoin_withdraw_fee()
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_litecoin_withdraw_list(self):
        response = self.api.litecoin_withdraw_list()
        assert "messages" in response

    # @tests.vcr.use_cassette
    # def test_litecoin_create_withdraw(self):
    #     response = self.api.litecoin_create_withdraw(
    #         destination="1FSzwTdndhtbjGtRTKiu2vQHHrVAPUGSZG",
    #         fee=0.0001,
    #         type="fast",
    #         amount=0.1)
    #     assert "messages" in response

    @tests.vcr.use_cassette
    def test_litecoin_deposit_list(self):
        response = self.api.litecoin_deposit_list()
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_orderbook_full(self):
        response = self.api.orderbook_full(currency="BTC")
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_summary(self):
        response = self.api.summary(currency="BTC")
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_create_order(self):
        response = self.api.create_order(
            currency="BTC",
            amount=0.1,
            type="sell",
            subtype="limited",
            unit_price=70000.0)
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_get_user_orders(self):
        response = self.api.get_user_orders(currency="BTC")
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_cancel_order(self):
        response = self.api.cancel_order(id="XXXXXXXXXXXXXXXXXXXXXXXXXX")
        assert response == None

    @tests.vcr.use_cassette
    def test_estimated_price(self):
        response = self.api.estimated_price(
            currency="BTC",
            amount=0.1,
            type="buy")
        assert "messages" in response

    @tests.vcr.use_cassette
    def test_balance(self):
        response = self.api.balance()
        assert "messages" in response

