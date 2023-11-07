
print ("Witaj w programie do obslugi ladowarki paczek.")
koniec_programu=False
ilosc_elementow=input("Podaj ilosc elemontow ktore chcesz zapakowac:")
suma_wyslanych_kilogramow=0
waga_paczki=0
ilosc_wyslanych_paczek=1
kilogramy_wyslane_w_paczce=0
suma_pustych_kilogramow=0
paczka_z_najwieksza_liczba_pustych_kilogamow=1
najwiecej_pustych_kilogramow_w_paczce=0

for element in range(int(ilosc_elementow)):
    waga_elementu=float(input("Podaj wage elementu: "))
    if waga_elementu>0 and waga_elementu <1 or waga_elementu>10:
        koniec_programu=True
        break
    elif waga_elementu==0:
        print("Maksymalna liczba elementow zostala osiagnieta.")
        break
    else:
        suma_wyslanych_kilogramow=suma_wyslanych_kilogramow+waga_elementu
        if (waga_paczki+waga_elementu <20):
            waga_paczki=waga_paczki+waga_elementu
            puste_kg_w_tej_paczce = 20 - waga_paczki
        else:
            kilogramy_wyslane_w_paczce=waga_elementu+kilogramy_wyslane_w_paczce

            suma_pustych_kilogramow = ilosc_wyslanych_paczek * 20 - suma_wyslanych_kilogramow
            puste_kg_w_tej_paczce = 20 - waga_paczki
            if puste_kg_w_tej_paczce>najwiecej_pustych_kilogramow_w_paczce:
                paczka_z_najwieksza_liczba_pustych_kilogamow=ilosc_wyslanych_paczek
                najwiecej_pustych_kilogramow_w_paczce=puste_kg_w_tej_paczce
            waga_paczki=waga_elementu
            ilosc_wyslanych_paczek = ilosc_wyslanych_paczek + 1
puste_kg_w_ostatniej_paczce=20-waga_paczki
suma_pustych_kilogramow=suma_pustych_kilogramow+20-waga_paczki
if puste_kg_w_ostatniej_paczce>najwiecej_pustych_kilogramow_w_paczce:
    paczka_z_najwieksza_liczba_pustych_kilogamow=ilosc_wyslanych_paczek
    najwiecej_pustych_kilogramow_w_paczce=puste_kg_w_ostatniej_paczce
if not koniec_programu:
    print("Podsumowanie :")
    print(f"Liczba wyslanych paczek to: {ilosc_wyslanych_paczek}")
    print(f"Liczba wyslanych kilogramow to: {suma_wyslanych_kilogramow}")

    print(f"Suma 'pustych' kilogramow to : {suma_pustych_kilogramow}")
    print(f"Paczka numer : {paczka_z_najwieksza_liczba_pustych_kilogamow} miala najwiecej 'pustych' kilogramow, jej wynik to {najwiecej_pustych_kilogramow_w_paczce} 'pustych' kilogramow")
else :
    print("Podana waga jest bledna. Element moze wazyc od 1 do 10kg.")



