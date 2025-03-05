# pakiet/zamowienia.py

from pakiet.produkty import produkty, nowa_ilosc_produktu

zamowienia = []

def utworz_nowe_uporzadkowanie(nazwa_produktu, ilosc):
    """Tworzy nowe zamówienie, jeśli produkt jest dostępny."""
    if nazwa_produktu not in produkty:
        print(f"Błąd: Produkt '{nazwa_produktu}' nie istnieje.")
        return None

    cena = produkty[nazwa_produktu]["cena"]
    dostepna_ilosc = produkty[nazwa_produktu]["ilość"]

    if dostepna_ilosc < ilosc:
        print(f"Nie ma wystarczającej ilości '{nazwa_produktu}'. Dostępne: {dostepna_ilosc}")
        return None

    cena_calk = cena * ilosc
    nowe_uporzadkowanie = {
        "produkt": nazwa_produktu,
        "ilość": ilosc,
        "cena_calk": cena_calk
    }

    zamowienia.append(nowe_uporzadkowanie)
    nowa_ilosc_produktu(nazwa_produktu, ilosc)  # Aktualizacja magazynu

    return nowe_uporzadkowanie






