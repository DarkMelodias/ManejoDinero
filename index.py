from tkinter import *
from view import *

def run():
    root = Tk()
    root.wm_title('Manejo de Dinero')
    app = Interfaz(root)
    app.mainloop()

if __name__ == '__main__':
    run()