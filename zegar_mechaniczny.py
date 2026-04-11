import tkinter as tk
import math
import time

class ZegarMechaniczny3_9:
    def __init__(self, root):
        self.root = root
        self.root.title("Mechanizm Systemu 3-9")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg='#1e293b', highlightthickness=0)
        self.canvas.pack()
        
        self.lbl_czas = tk.Label(self.root, text="", font=("Courier New", 16, "bold"), fg="#f8fafc", bg="#0f172a")
        self.lbl_czas.pack(fill="both", expand=True)
        
        self.aktualizuj_mechanizm()

    def aktualizuj_mechanizm(self):
        self.canvas.delete("all")
        
        t = time.localtime()
        h, m, s = t.tm_hour, t.tm_min, t.tm_sec
        
        # 1. RYSOWANIE NOWEJ TARCZY MINUTOWEJ
        # Zewnętrzny okrąg
        self.canvas.create_oval(50, 50, 450, 450, outline="#475569", width=2)
        
        # Generowanie skali Ortosów na obwodzie (co 15 stopni)
        for kat_deg in range(0, 360, 15):
            kat_rad = math.radians(kat_deg)
            
            # Obliczanie wartości Ortosa dla danego kąta na tarczy
            mod_kat = kat_deg % 180
            ortos_val = abs(90 - mod_kat) if mod_kat <= 90 else abs(90 - (180 - mod_kat))
            
            # Rysowanie kresek na tarczy
            x1 = 250 + 190 * math.sin(kat_rad)
            y1 = 250 - 190 * math.cos(kat_rad)
            x2 = 250 + 200 * math.sin(kat_rad)
            y2 = 250 - 200 * math.cos(kat_rad)
            self.canvas.create_line(x1, y1, x2, y2, fill="#64748b", width=2)
            
            # Podpisywanie tarczy wartościami Ortosów (co 30 stopni)
            if kat_deg % 30 == 0:
                xt = 250 + 170 * math.sin(kat_rad)
                yt = 250 - 170 * math.cos(kat_rad)
                self.canvas.create_text(xt, yt, text=f"{int(ortos_val)}°", fill="#94a3b8", font=("Helvetica", 10))

        # Osie główne
        self.canvas.create_line(50, 250, 450, 250, fill="#334155", dash=(4, 4)) # Oś 0 (3-9)
        self.canvas.create_line(250, 50, 250, 450, fill="#334155", dash=(4, 4)) # Oś 90 (12-6)

        # Obliczanie kątów wskazówek
        kat_h = (h % 12 + m / 60 + s / 3600) * 30
        kat_m = (m + s / 60) * 6

        # 2. WSKAZÓWKA MINUTOWA (ŚREDNICA)
        # Przechodzi przez całą tarczę, oba końce wskazują tę samą wartość Ortosa na skali
        x_mA = 250 + 200 * math.sin(math.radians(kat_m))
        y_mA = 250 - 200 * math.cos(math.radians(kat_m))
        x_mB = 250 - 200 * math.sin(math.radians(kat_m))
        y_mB = 250 + 200 * math.cos(math.radians(kat_m))
        self.canvas.create_line(x_mA, y_mA, x_mB, y_mB, fill="#3b82f6", width=2)
        
        # Groty na obu końcach linii minutowej
        self.canvas.create_oval(x_mA-4, y_mA-4, x_mA+4, y_mA+4, fill="#3b82f6", outline="")
        self.canvas.create_oval(x_mB-4, y_mB-4, x_mB+4, y_mB+4, fill="#3b82f6", outline="")

        # 3. WSKAZÓWKA GODZINOWA (Normalna)
        x_h = 250 + 120 * math.sin(math.radians(kat_h))
        y_h = 250 - 120 * math.cos(math.radians(kat_h))
        self.canvas.create_line(250, 250, x_h, y_h, fill="#ef4444", width=5, arrow=tk.LAST)
        
        # Środek zegara
        self.canvas.create_oval(243, 243, 257, 257, fill="#e2e8f0", outline="#0f172a", width=2)

        # Obliczanie aktualnego Ortosa dla wyświetlacza
        kat_m_mod = kat_m % 180
        kat_h_mod = kat_h % 180
        rozny_kat = abs(kat_h_mod - kat_m_mod)
        if rozny_kat > 90:
            rozny_kat = 180 - rozny_kat
        ortos = abs(90 - rozny_kat)

        sfera = "[+]" if not (3 <= h < 9) else "[-]"
        
        self.lbl_czas.config(
            text=f"{sfera} Cykl: {h%12} | Bieżący Ortos: {ortos:.2f}°"
        )
        
        self.root.after(1000, self.aktualizuj_mechanizm)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZegarMechaniczny3_9(root)
    root.mainloop()
