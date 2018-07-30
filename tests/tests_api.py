import tests
import unittest
import bitcointrade

class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.api = bitcointrade.Api()

    @tests.vcr.use_cassette
    def test_ticker(self):
        response = self.api.ticker("BTC")
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
        assert 'asks' in response
        assert 'bids' in response
        assert len(response['asks']) > 0
        assert len(response['bids']) > 0

    @tests.vcr.use_cassette
    def test_trades(self):
        response = self.api.trades("BTC")
        assert 'pagination' in response
        assert 'trades' in response
        assert len(response['trades']) > 0
