import time

print("--- PROJEKT SYSTEMU 3-9: POKAZ MOŻLIWOŚCI ---")

# 1. Pobieramy aktualny czas z nowym trendem
sfera, cykl, ortos, centi, trend = orthos_time.get_3_9_time()
zegarek_str = orthos_time.format_time(sfera, cykl, ortos, centi, trend)

print(f"Bieżący czas Ortogonalny: {zegarek_str}")
print("-" * 45)

# 2. Szyfrujemy wiadomość
wiadomosc = "To jest scisle tajna wiadomosc zakodowana czasem!"
print(f"Oryginalna wiadomość: {wiadomosc}")

zaszyfrowana = orthos_cipher.encrypt(wiadomosc, sfera, cykl, ortos, centi, trend)
print(f"Zaszyfrowana (bajty): {zaszyfrowana.encode('utf-8')}")
print("-" * 45)

# 3. Symulujemy upływ czasu (pół sekundy)
time.sleep(0.5)

# Pobieramy NOWY czas
nowa_sfera, nowy_cykl, nowy_ortos, nowy_centi, nowy_trend = orthos_time.get_3_9_time()
print(f"Nowy czas zegara: {orthos_time.format_time(nowa_sfera, nowy_cykl, nowy_ortos, nowy_centi, nowy_trend)}")

# Próba odszyfrowania nowym (złym) czasem
proba_zla = orthos_cipher.decrypt(zaszyfrowana, nowa_sfera, nowy_cykl, nowy_ortos, nowy_centi, nowy_trend)
print(f"Próba odszyfrowania nowym czasem: {proba_zla} (BŁĄD!)")

# Prawidłowe odszyfrowanie
proba_dobra = orthos_cipher.decrypt(zaszyfrowana, sfera, cykl, ortos, centi, trend)
print(f"Odszyfrowanie właściwym kluczem czasu: {proba_dobra} (SUKCES!)")
