from backend import save_price
from backend import get_prices
from backend import _initialize_prices_from_storage
from backend import _save_prices_to_storage
from backend import delete_price

_initialize_prices_from_storage()

def run():
    espec = input()
    delete_price(espec)
    prices = get_prices()
    print(prices)

if __name__ == '__main__':
    run()

_save_prices_to_storage