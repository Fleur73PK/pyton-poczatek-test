# main.py

from pakiet.zamowienia import utworz_nowe_uporzadkowanie

print("Witamy w naszym sklepie!")
nazwa_produktu = input("Jaki towar chcesz kupić? ").strip().lower()
ilosc = int(input("Ile sztuk/kg produktu chcesz kupić? "))

wynik = utworz_nowe_uporzadkowanie(nazwa_produktu, ilosc)

if wynik is not None:
    cena_calk = wynik["cena_calk"]
    print(f"Łączny koszt wyniesie {cena_calk} zł.")
