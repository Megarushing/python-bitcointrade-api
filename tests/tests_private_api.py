import tests
import unittest
import bitcointrade
from bitcointrade.errors import ApiError, ArgumentError

def assert_order_response(response):
    assert type(response) == dict
    assert "id" in response
    assert "unit_price" in response
    assert "code" in response
    assert "user_code" in response
    assert "amount" in response

def assert_complete_order_response(response):
    assert type(response) == dict
    assert "id" in response
    assert "code" in response
    assert "currency_code" in response
    assert "type" in response
    assert "subtype" in response
    assert "requested_amount" in response
    assert "executed_amount" in response
    assert "remaining_amount" in response
    assert "remaining_price" in response
    assert "unit_price" in response
    assert "total_price" in response
    assert "status" in response
    assert "update_date" in response
    assert "create_date" in response

def assert_fee_response(response):
    assert type(response) == list
    for r in response:
        assert "name" in r
        assert "amount" in r

def assert_withdraw_response(response):
    assert type(response) == dict
    assert "code" in response
    assert "origin_address" in response
    assert "destination_address" in response
    assert "amount" in response
    assert "miner_fee" in response
    assert "miner_fee_type" in response
    assert "tax_index" in response
    assert "tax_index_calculated" in response
    assert "tax_amount" in response
    assert "status" in response
    assert "create_date" in response
    assert "update_date" in response
    assert "transaction_id" in response
    assert "link" in response

def assert_withdraw_list_response(response):
    assert type(response) == dict
    assert "withdrawals" in response
    assert type(response["withdrawals"]) == list
    for r in response["withdrawals"]:
        assert_withdraw_response(r)

def assert_deposit_list_response(response):
    assert type(response) == dict
    assert "deposits" in response
    assert type(response["deposits"]) == list
    for r in response["deposits"]:
        assert "code" in r
        assert "hash" in r
        assert "amount" in r
        assert "status" in r
        assert "create_date" in r
        assert "confirmation_date" in r

class PrivateApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = bitcointrade.PrivateApi("42")

    @tests.vcr.use_cassette
    def test_bitcoin_withdraw_fee(self):
        response = self.api.bitcoin_withdraw_fee()
        assert_fee_response(response)

    @tests.vcr.use_cassette
    def test_bitcoin_withdraw_list(self):
        response = self.api.bitcoin_withdraw_list()
        assert_withdraw_list_response(response)

    @tests.vcr.use_cassette
    def test_bitcoin_create_withdraw(self):
        response = self.api.bitcoin_create_withdraw(
            destination="1FSzwTdndhtbjGtRTKiu2vQHHrVAPUGSZG",
            fee=0.0001,
            fee_type="slow",
            amount=0.1)
        assert_withdraw_response(response)

    @tests.vcr.use_cassette
    def test_bitcoin_deposit_list(self):
        response = self.api.bitcoin_deposit_list()
        assert_deposit_list_response(response)

    @tests.vcr.use_cassette
    def test_ethereum_withdraw_fee(self):
        response = self.api.ethereum_withdraw_fee()
        assert_fee_response(response)

    @tests.vcr.use_cassette
    def test_ethereum_withdraw_list(self):
        response = self.api.ethereum_withdraw_list()
        assert_withdraw_list_response(response)

    @tests.vcr.use_cassette
    def test_ethereum_create_withdraw(self):
        response = self.api.ethereum_create_withdraw(
            destination="0x27Db473751D76e2E9Af2b7A9b0199ef2c6Af838D",
            fee=0.0001,
            fee_type="slow",
            amount=0.1)
        assert_withdraw_response(response)

    @tests.vcr.use_cassette
    def test_ethereum_deposit_list(self):
        response = self.api.ethereum_deposit_list()
        assert_deposit_list_response(response)

    @tests.vcr.use_cassette
    def test_litecoin_withdraw_fee(self):
        response = self.api.litecoin_withdraw_fee()
        assert_fee_response(response)

    @tests.vcr.use_cassette
    def test_litecoin_withdraw_list(self):
        response = self.api.litecoin_withdraw_list()
        assert_withdraw_list_response(response)

    @tests.vcr.use_cassette
    def test_litecoin_create_withdraw(self):
        response = self.api.litecoin_create_withdraw(
            destination="LhWeEXcVHpHxonqbLooKPNMzbmMetdHJdC",
            fee=0.0001,
            fee_type="slow",
            amount=0.1)
        assert_withdraw_response(response)

    @tests.vcr.use_cassette
    def test_litecoin_deposit_list(self):
        response = self.api.litecoin_deposit_list()
        assert_deposit_list_response(response)

    @tests.vcr.use_cassette
    def test_orderbook_full(self):
        response = self.api.orderbook_full(currency="BTC")
        assert type(response) == dict
        assert "buying" in response
        assert type(response["buying"]) == list
        assert "selling" in response
        assert type(response["selling"]) == list
        for r in response["buying"]:
            assert_order_response(r)
        for r in response["selling"]:
            assert_order_response(r)

    @tests.vcr.use_cassette
    def test_summary(self):
        response = self.api.summary(currency="BTC")
        assert type(response) == list
        assert len(response) > 0
        assert "unit_price_24h" in response[0]
        assert "volume_24h" in response[0]
        assert "max_price" in response[0]
        assert "min_price" in response[0]
        assert "last_transaction_unit_price" in response[0]
        assert "currency" in response[0]

    @tests.vcr.use_cassette
    def test_create_order(self):
        response = self.api.create_order(
            currency="BTC",
            amount=0.1,
            type="sell",
            subtype="limited",
            unit_price=70000.0)
        assert_order_response(response)

    @tests.vcr.use_cassette
    def test_get_user_orders(self):
        response = self.api.get_user_orders(currency="BTC")
        assert type(response) == dict
        assert "orders" in response
        assert type(response["orders"]) == list
        for r in response["orders"]:
            assert_complete_order_response(r)

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
        assert type(response) == dict
        assert "price" in response

    @tests.vcr.use_cassette
    def test_balance(self):
        response = self.api.balance()
        assert type(response) == list
        for r in response:
            assert "available_amount" in r
            assert "locked_amount" in r
            assert "currency_code" in r

