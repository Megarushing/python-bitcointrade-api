import tests
import unittest
import bitcointrade

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = bitcointrade.Api()

    @tests.vcr.use_cassette
    def test_ticker(self):
        response = self.api.ticker("BTC")
        assert type(response) == dict
        assert 'high' in response
        assert 'low' in response
        assert 'volume' in response
        assert 'trades_quantity' in response
        assert 'last' in response
        assert 'sell' in response
        assert 'buy' in response
        assert 'date' in response

    @tests.vcr.use_cassette
    def test_orderbook(self):
        response = self.api.orderbook("BTC")
        assert type(response) == dict
        assert "asks" in response
        assert type(response["asks"]) == list
        assert "bids" in response
        assert type(response["bids"]) == list
        for r in response["bids"]+response["asks"]:
            assert "unit_price" in r
            assert "code" in r
            assert "stop_limit_price" in r
            assert "amount" in r

    @tests.vcr.use_cassette
    def test_trades(self):
        response = self.api.trades("BTC")
        assert type(response) == dict
        assert "trades" in response
        assert type(response["trades"]) == list
        for r in response["trades"]:
            assert "type" in r
            assert "amount" in r
            assert "unit_price" in r
            assert "active_order_code" in r
            assert "passive_order_code" in r
            assert "date" in r
