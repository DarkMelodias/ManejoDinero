import csv
import os

PRICES_TABLE = ".prices.csv"
PRICES_SCHEME = ['especificacion','valor','cobro']
prices = []

def _initialize_prices_from_storage():
    with open(PRICES_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=PRICES_SCHEME)

        for row in reader:
            prices.append(row)

def _save_prices_to_storage():
    tmp_table_name = '{}.tmp'.format(PRICES_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=PRICES_SCHEME)
        writer.writerows(prices)

        os.remove(PRICES_TABLE)
    os.rename(tmp_table_name, PRICES_TABLE)

def save_price(especificacion,valor,cobro):
    price = {
        'especificacion': especificacion,
        'valor': valor,
        'cobro': cobro
    }
    prices.append(price)

def delete_price(especificacion):
    global prices
    for element in prices:
        if element['especificacion'].lower() == especificacion.lower():
            prices.remove(element)
            return True
    return False
    


def get_prices():
    return prices
