from backend import save_price
from backend import get_prices
from backend import _initialize_prices_from_storage
from backend import _save_prices_to_storage

_initialize_prices_from_storage()

def run():
    prices = get_prices()
    print(prices[0]['especificacion'])

if __name__ == '__main__':
    run()

_save_prices_to_storage