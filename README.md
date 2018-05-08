# bitcointrade python api

A Python wrapper for Bitcointrade API. Forked project from python-mercadobitcoin by Alan Fachini (alfakini@gmail.com)

## Installation

```bash
git clone https://github.com/Megarushing/bitcointrade-python-api.git
cd bitcointrade-python-api
python setup.py install
```

## Basic Usage

Below you can see the available Bitcointrade API methods you can use:

```python
import bitcointrade
btctrade = bitcointrade.PublicApi()

btctrade.list_orderbook()
```

And the private Trade API:

```python
from bitcointrade import PrivateApi

btctrade = PrivateApi(<API_ID>, <API_SECRET>)

btctrade.list_orderbook(currency="BTC")
btctrade.create_order(currency="BTC",amount="0.1",type="buy",subtype="market",unit_price="")
btctrade.balance()
btctrade.estimated_price(currency="BTC",amount="0.1","type"="buy")
btctrade.bitcoin_withdraw_fee()
btctrade.ethereum_withdraw_fee()
btctrade.bitcoin_create_withdraw(destination="1FSzwTdndhtbjGtRTKiu2vQHHrVAPUGSZG",fee="0.0001",type="fast",amount="0.1")

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
