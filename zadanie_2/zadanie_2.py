#napisanie programu generuj<acego spersonalizowaną kartkę urodzinową.
#jako dane uzytkownika pobieram  Imię odbiorcy, rok urodzenia odbiorcy, spersonalizowana wiadomosc i imie nadawcy
#jako wyjscie powinnismy dostac imie odbiorcy,  wiadomosc z informacja o wieku odbiorcy i spersonalizowana wiadomoscia oraz imie nadawcy.
print("Witan w naszym programie. \n Stworz spersonalizowane zyczenia urodzinowe")
imie_odbiorcy =input("Podaj imie odbiorcy: ")
rok_urodzenia=int(input("Podaj rok urodzenia odbiorcy: "))
obecny_rok=2023
wiek_odbiorcy= obecny_rok-rok_urodzenia
spersonalizowana_wiadomosc=input("Podaj tresc zyczen urodzinowych: ")
imie_nadawcy=input("Podaj swoje imie: ")
print(f"{imie_odbiorcy}, wszystkiego najlepszego z okazji {wiek_odbiorcy} urodzin! \n {spersonalizowana_wiadomosc} \n {imie_nadawcy}")
