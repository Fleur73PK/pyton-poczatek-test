# pakiet/produkty.py
"""Slownik ktory przechowuje informacje o produktach"""
produkty = {
    "chleb": {
        "ilość": 20,
        "cena": 4
    },
    "jablka": {
        "ilość": 15,
        "cena": 2
    }
}

def nowa_ilosc_produktu(nazwa_produktu, zamowiona_ilosc):
    """Zmniejsza ilość produktu w magazynie po zakupie."""
    if nazwa_produktu in produkty:
        produkty[nazwa_produktu]["ilość"] -= zamowiona_ilosc
