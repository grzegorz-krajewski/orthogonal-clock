import tkinter as tk
import math
import time

class PrawdziwyZegarOrtogonalny3_9:
    def __init__(self, root):
        self.root = root
        self.root.title("Zegarek Jednowskazówkowy Systemu 3-9")
        self.root.geometry("500x620")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg='#0f172a', highlightthickness=0)
        self.canvas.pack()
        
        self.lbl_czas = tk.Label(self.root, text="", font=("Courier New", 14, "bold"), fg="#f8fafc", bg="#1e293b")
        self.lbl_czas.pack(fill="both", expand=True)
        
        self.aktualizuj_mechanizm()

    def aktualizuj_mechanizm(self):
        self.canvas.delete("all")
        
        # Pobieranie czasu systemowego z dokładnością do ułamków sekund
        czas_teraz = time.time()
        t = time.localtime(czas_teraz)
        h, m, s = t.tm_hour, t.tm_min, t.tm_sec
        # Dodajemy ułamki sekund do obliczeń płynnego ruchu
        ułamki_sekund = czas_teraz % 1
        
        # 1. OBLICZANIE KĄTÓW (Z ułamkiem sekundy dla super-płynności)
        sekundy_plynne = s + ułamki_sekund
        kat_h = (h % 12 + m / 60 + sekundy_plynne / 3600) * 30
        kat_m = (m + sekundy_plynne / 60) * 6

        # 2. RYSOWANIE RUCHOMEJ TARCZY
        self.canvas.create_oval(70, 70, 430, 430, outline="#334155", width=2)
        
        for i in range(0, 360, 15):
            kat_rysowania = kat_h + i
            rad_rys = math.radians(kat_rysowania)
            
            mod_i = i % 180
            ortos_val = abs(90 - mod_i) if mod_i <= 90 else abs(90 - (180 - mod_i))
            
            x1 = 250 + 170 * math.sin(rad_rys)
            y1 = 250 - 170 * math.cos(rad_rys)
            x2 = 250 + 180 * math.sin(rad_rys)
            y2 = 250 - 180 * math.cos(rad_rys)
            
            color = "#60a5fa" if ortos_val == 0 else ("#f87171" if ortos_val == 90 else "#475569")
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
            
            if i % 30 == 0:
                xt = 250 + 155 * math.sin(rad_rys)
                yt = 250 - 155 * math.cos(rad_rys)
                self.canvas.create_text(xt, yt, text=f"{int(ortos_val)}°", fill="#94a3b8", font=("Helvetica", 9))

        # 3. JEDYNA WSKAZÓWKA GODZINOWA (Cykl)
        rad_h = math.radians(kat_h)
        x_h = 250 + 120 * math.sin(rad_h)
        y_h = 250 - 120 * math.cos(rad_h)
        self.canvas.create_line(250, 250, x_h, y_h, fill="#ef4444", width=5, arrow=tk.LAST)
        
        # 4. STATYCZNY ZNACZNIK ODCZYTU ORTOSA (Na samej górze tarczy - 12:00)
        self.canvas.create_polygon(250, 40, 245, 25, 255, 25, fill="#10b981")
        self.canvas.create_text(250, 15, text="PUNKT ODCZYTU ORTOSA", fill="#10b981", font=("Helvetica", 8, "bold"))
        self.canvas.create_line(250, 40, 250, 70, fill="#10b981", width=2, dash=(2,2))

        # Środek zegara
        self.canvas.create_oval(244, 244, 256, 256, fill="#e2e8f0", outline="#0f172a", width=2)

        # 5. OBLICZANIE WARTOŚCI DO WYŚWIETLACZA
        kat_m_mod = kat_m % 180
        kat_h_mod = kat_h % 180
        rozny_kat = abs(kat_h_mod - kat_m_mod)
        if rozny_kat > 90:
            rozny_kat = 180 - rozny_kat
            
        ortos_pelny = abs(90 - rozny_kat)
        ortos = int(ortos_pelny)
        centi = int((ortos_pelny - ortos) * 100)

        sfera = "[+]" if not (3 <= h < 9) else "[-]"
        
        self.lbl_czas.config(
            text=f"{sfera} Cykl: {h%12} | Ortos: {ortos}° | Centi: {centi:02d}\n"
                 f"Tyknięcie zegara: co 1 Centi (~109 ms)\n"
                 f"Tradycyjny podgląd: {h:02d}:{m:02d}:{s:02d}"
        )
        
        # KLUCZOWA ZMIANA: Odświeżanie co 109 milisekund, a nie co 1000!
        self.root.after(109, self.aktualizuj_mechanizm)

if __name__ == "__main__":
    root = tk.Tk()
    app = PrawdziwyZegarOrtogonalny3_9(root)
    root.mainloop()
