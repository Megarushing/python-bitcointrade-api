[![PyPI](https://img.shields.io/pypi/v/bitcointrade.svg)](https://pypi.python.org/pypi/bitcointrade)

# bitcointrade python api

A Python wrapper for Bitcointrade API. Forked project from python-mercadobitcoin by Alan Fachini (alfakini@gmail.com)

## Installation

Directly from [PyPI](https://pypi.python.org/pypi/bitcointrade):

```bash
pip install bitcointrade
```

You can also install directly from the GitHub repository to have the newest features by running:

```bash
git clone https://github.com/Megarushing/python-bitcointrade-api.git
cd python-bitcointrade-api
python setup.py install
```

## Basic Usage

Below you can see the available Bitcointrade API methods you can use:

```python
import bitcointrade
btctrade = bitcointrade.Api()

btctrade.ticker("BRLBTC")
btctrade.orderbook("BRLBTC")
btctrade.trades("BRLBTC",
    start_time="2016-10-01T00:00:00-03:00",
    end_time="2018-10-10T23:59:59-03:00",
    page_size=100,
    current_page=1)
```

And the private Trade API:

```python
import bitcointrade
btctrade = bitcointrade.PrivateApi("<API_SECRET>")

btctrade.bitcoin_withdraw_fee()
btctrade.bitcoin_withdraw_list()
btctrade.bitcoin_create_withdraw(destination="1FSzwTdndhtbjGtRTKiu2vQHHrVAPUGSZG",
    fee_type="fast",
    amount=0.1)
btctrade.bitcoin_deposit_list()
btctrade.orderbook_full(currency="BTC")
btctrade.summary(currency="BTC")
btctrade.create_order(currency="BTC",
    amount=0.1,
    type="buy",
    subtype="market",
    unit_price=10000.0,
    request_price=10000.0*0.1)
btctrade.get_user_orders()
btctrade.cancel_order(id="<Order ID>")
btctrade.estimated_price(currency="BTC",
    amount=0.1,
    type="buy")
btctrade.balance()
btctrade.ethereum_withdraw_fee()
btctrade.ethereum_withdraw_list()
btctrade.ethereum_create_withdraw(destination="0x27Db473751D76e2E9Af2b7A9b0199ef2c6Af838D",
    fee_type="fast",
    amount=0.1)
btctrade.ethereum_deposit_list()
btctrade.litecoin_withdraw_fee()
btctrade.litecoin_withdraw_list()
btctrade.litecoin_create_withdraw(destination="LhWeEXcVHpHxonqbLooKPNMzbmMetdHJdC",
    fee_type="fast",
    amount=0.1)
btctrade.bitcoincash_deposit_list()
btctrade.bitcoincash_withdraw_fee()
btctrade.bitcoincash_withdraw_list()
btctrade.bitcoincash_create_withdraw(destination="1Dz46MhtvLH4Qd7RxXMxtMS8zZTBe5qiDj",
    fee_type="fast",
    amount=0.1)
btctrade.litecoin_deposit_list()

```
you may also use optional parameters when available:
```python
btctrade.get_user_orders(status="executed_completely",
    start_date="2017-01-01",
    end_date="2018-01-01",
    currency="BTC",
    type="buy",
    page_size=100,
    current_page=1)
    
    
btctrade.bitcoin_deposit_list(page_size=10,
    current_page=1,
    status="confirmed",
    start_date="2017-01-01",
    end_date="2018-01-01")
btctrade.bitcoin_withdraw_list(page_size=10,
    current_page=1,
    status="pending",
    start_date="2017-01-01",
    end_date="2018-01-25")

btctrade.ethereum_withdraw_list(page_size=10,
    current_page=1,
    status="pending",
    start_date="2017-01-01",
    end_date="2018-01-25")
btctrade.ethereum_deposit_list(page_size=10,
    current_page=1,
    status="confirmed",
    start_date="2017-01-01",
    end_date="2018-01-01")
    
    
btctrade.litecoin_withdraw_list(page_size=10,
    current_page=1,
    status="pending",
    start_date="2017-01-01",
    end_date="2018-01-25")
btctrade.litecoin_deposit_list(page_size=10,
    current_page=1,
    status="confirmed",
    start_date="2017-01-01",
    end_date="2018-01-01")
    
btctrade.bitcoincash_withdraw_list(page_size=10,
    current_page=1,
    status="pending",
    start_date="2017-01-01",
    end_date="2018-01-25")
btctrade.bitcoincash_deposit_list(page_size=10,
    current_page=1,
    status="confirmed",
    start_date="2017-01-01",
    end_date="2018-01-01")
```

Please notice that almost all calls dont have explicit parameters,
you can check the list of mandatory and optional parameters
via BitcoinTrade [documentation](https://apidocs.bitcointrade.com.br/#5ef0088b-40ef-4668-2ac4-59e0b94e91f7)
or by using python auto-documentation:
```python
help(btctrade.estimated_price)
```

## Development

Install development dependencies:

```bash
brew install libyaml
pip install -r requirements-development.txt
```

Run tests:

```bash
tox
```

## References

* [Bitcointrade public data API](https://apidocs.bitcointrade.com.br/#1ce5ce29-3e4d-8e97-3b43-185bb3862289)
* [Bitcointrade private trade API](https://apidocs.bitcointrade.com.br/#e1ba3dbf-6fef-238c-41da-92885c00290f)
