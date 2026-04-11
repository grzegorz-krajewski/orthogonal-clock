import tkinter as tk
import math
import time

class PrawdziwyZegarMechaniczny3_9:
    def __init__(self, root):
        self.root = root
        self.root.title("Mechanizm Systemu 3-9 (Ruchoma Tarcza)")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg='#0f172a', highlightthickness=0)
        self.canvas.pack()
        
        self.lbl_czas = tk.Label(self.root, text="", font=("Courier New", 14, "bold"), fg="#f8fafc", bg="#1e293b")
        self.lbl_czas.pack(fill="both", expand=True)
        
        self.aktualizuj_mechanizm()

    def aktualizuj_mechanizm(self):
        self.canvas.delete("all")
        
        t = time.localtime()
        h, m, s = t.tm_hour, t.tm_min, t.tm_sec
        
        # 1. OBLICZANIE KĄTÓW (Zgodnie z ruchem wskazówek)
        kat_h = (h % 12 + m / 60 + s / 3600) * 30
        kat_m = (m + s / 60) * 6

        # 2. RYSOWANIE RUCHOMEJ TARCZY (Obraca się razem z wskazówką godzinową!)
        self.canvas.create_oval(70, 70, 430, 430, outline="#334155", width=2)
        
        # Generujemy podziałkę tarczy Ortosów
        # 0 stopni Ortosa musi pokrywać się z linią prostopadłą do wskazówki godzinowej!
        for i in range(0, 360, 15):
            # Kąt rysowania kreski na tarczy uwzględnia przesunięcie o pozycję wskazówki godzinowej
            kat_rysowania = kat_h + i
            rad_rys = math.radians(kat_rysowania)
            
            # Obliczanie wartości Ortosa (0 na bokach od godziny, 90 na osi godziny)
            mod_i = i % 180
            ortos_val = abs(90 - mod_i) if mod_i <= 90 else abs(90 - (180 - mod_i))
            
            # Rysowanie kresek
            x1 = 250 + 170 * math.sin(rad_rys)
            y1 = 250 - 170 * math.cos(rad_rys)
            x2 = 250 + 180 * math.sin(rad_rys)
            y2 = 250 - 180 * math.cos(rad_rys)
            
            # Wyróżnienie głównych osi (0 i 90)
            color = "#60a5fa" if ortos_val == 0 else ("#f87171" if ortos_val == 90 else "#475569")
            self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)
            
            # Podpisywanie wartości Ortosów co 30 stopni
            if i % 30 == 0:
                xt = 250 + 155 * math.sin(rad_rys)
                yt = 250 - 155 * math.cos(rad_rys)
                self.canvas.create_text(xt, yt, text=f"{int(ortos_val)}°", fill="#94a3b8", font=("Helvetica", 9))

        # 3. WSKAZÓWKA GODZINOWA (Cykl)
        # Rysujemy ją jako bazę
        rad_h = math.radians(kat_h)
        x_h = 250 + 120 * math.sin(rad_h)
        y_h = 250 - 120 * math.cos(rad_h)
        self.canvas.create_line(250, 250, x_h, y_h, fill="#ef4444", width=5, arrow=tk.LAST)
        
        # 4. WSKAZÓWKA MINUTOWA (ŚREDNICA)
        # Porusza się całkowicie niezależnie i wskazuje wartość na obracającej się tarczy
        rad_m = math.radians(kat_m)
        x_mA = 250 + 180 * math.sin(rad_m)
        y_mA = 250 - 180 * math.cos(rad_m)
        x_mB = 250 - 180 * math.sin(rad_m)
        y_mB = 250 + 180 * math.cos(rad_m)
        self.canvas.create_line(x_mA, y_mA, x_mB, y_mB, fill="#3b82f6", width=2)
        
        # Groty linii minutowej
        self.canvas.create_oval(x_mA-4, y_mA-4, x_mA+4, y_mA+4, fill="#3b82f6", outline="")
        self.canvas.create_oval(x_mB-4, y_mB-4, x_mB+4, y_mB+4, fill="#3b82f6", outline="")
        
        # Środek zegara
        self.canvas.create_oval(244, 244, 256, 256, fill="#e2e8f0", outline="#0f172a", width=2)

        # 5. OBLICZANIE ORTOSA I CENTI DO WYŚWIETLACZA
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
            text=f"{sfera} Cykl: {h%12} | Ortos: {ortos}° | Centi: {centi:02d}\nTradycyjny: {h:02d}:{m:02d}:{s:02d}"
        )
        
        self.root.after(1000, self.aktualizuj_mechanizm)

if __name__ == "__main__":
    root = tk.Tk()
    app = PrawdziwyZegarMechaniczny3_9(root)
    root.mainloop()
