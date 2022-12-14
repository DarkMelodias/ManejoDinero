from tkinter import *
from view import *

from backend import _initialize_prices_from_storage
from backend import _save_prices_to_storage

_initialize_prices_from_storage()

def run():
    root = Tk()
    root.wm_title('Manejo de Dinero')
    app = Interfaz(root)
    app.mainloop()

if __name__ == '__main__':
    run()

_save_prices_to_storage()