import orthos_time
import orthos_cipher
import time

print("--- PROJEKT SYSTEMU 3-9: POKAZ MOŻLIWOŚCI ---")

# 1. Pobieramy aktualny czas w Twoim systemie z angielskiej biblioteki
sfera, cykl, ortos = orthos_time.get_3_9_time()
zegarek_str = orthos_time.format_time(sfera, cykl, ortos)

print(f"Bieżący czas Ortogonalny: {zegarek_str}")
print("-" * 45)

# 2. Szyfrujemy wiadomość dokładnie tym bieżącym ułamkiem czasu!
wiadomosc = "To jest scisle tajna wiadomosc zakodowana czasem!"
print(f"Oryginalna wiadomość: {wiadomosc}")

# Szyfrowanie
zaszyfrowana = orthos_cipher.encrypt(wiadomosc, sfera, cykl, ortos)
print(f"Zaszyfrowana (bajty): {zaszyfrowana.encode('utf-8')}")
print("-" * 45)

# 3. Symulujemy upływ czasu i próbę odszyfrowania
print("Czekamy 2 sekundy (czas płynie, Ortos się zmienia)...")
time.sleep(2)

# Pobieramy NOWY czas
nowa_sfera, nowy_cykl, nowy_ortos = orthos_time.get_3_9_time()
print(f"Nowy czas zegara: {orthos_time.format_time(nowa_sfera, nowy_cykl, nowy_ortos)}")

# Próba odszyfrowania nowym (złym) czasem
proba_zla = orthos_cipher.decrypt(zaszyfrowana, nowa_sfera, nowy_cykl, nowy_ortos)
print(f"Próba odszyfrowania nowym czasem: {proba_zla} (BŁĄD!)")

# Prawidłowe odszyfrowanie (używamy starych parametrów, które były kluczem)
proba_dobra = orthos_cipher.decrypt(zaszyfrowana, sfera, cykl, ortos)
print(f"Odszyfrowanie właściwym kluczem czasu: {proba_dobra} (SUKCES!)")
