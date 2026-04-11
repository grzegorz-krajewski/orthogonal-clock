import tkinter as tk
import math
import time

class ZegarekSystemu3_9:
    def __init__(self, root):
        self.root = root
        self.root.title("Zegarek Systemu 3-9")
        self.root.geometry("450x600")
        self.root.resizable(False, False)
        
        # Płótno zegara
        self.canvas = tk.Canvas(self.root, width=450, height=450, highlightthickness=0)
        self.canvas.pack()
        
        # Panel wyświetlacza nowej ery
        self.ramka_cyfrowa = tk.Frame(self.root, height=150)
        self.ramka_cyfrowa.pack(fill="both", expand=True)
        
        self.lbl_nowy_czas = tk.Label(self.ramka_cyfrowa, text="", font=("Courier New", 18, "bold"))
        self.lbl_nowy_czas.pack(pady=10)
        
        self.lbl_tradycyjny = tk.Label(self.ramka_cyfrowa, text="", font=("Helvetica", 10), fg="gray")
        self.lbl_tradycyjny.pack()
        
        self.aktualizuj_zegar()

    def aktualizuj_zegar(self):
        self.canvas.delete("wszystko")
        
        t = time.localtime()
        h, m, s = t.tm_hour, t.tm_min, t.tm_sec
        
        # Wyznaczanie sfery (Dzień/Noc) na podstawie osi 3-9
        if 3 <= h < 9:
            sfera = "[-]"
            bg_color = "#1e293b" # Ciemny (Noc)
            fg_color = "#f8fafc"
            line_color = "#475569"
        else:
            sfera = "[+]"
            bg_color = "#f8fafc" # Jasny (Dzień)
            fg_color = "#0f172a"
            line_color = "#cbd5e1"
            
        self.canvas.config(bg=bg_color)
        self.ramka_cyfrowa.config(bg=bg_color)
        self.lbl_nowy_czas.config(bg=bg_color, fg=fg_color)
        self.lbl_tradycyjny.config(bg=bg_color)
        
        # Rysowanie tarczy
        self.canvas.create_oval(25, 25, 425, 425, outline=line_color, width=2, tags="wszystko")
        # Oś horyzontalna (3-9)
        self.canvas.create_line(25, 225, 425, 225, fill=line_color, dash=(2, 4), tags="wszystko")
        
        # Obliczanie fizycznych pozycji wskazówek
        kat_h = (h % 12 + m / 60 + s / 3600) * 30
        kat_m = (m + s / 60) * 6
        
        # 1. Wskazówka godzinowa (Promień)
        x_h = 225 + 130 * math.sin(math.radians(kat_h))
        y_h = 225 - 130 * math.cos(math.radians(kat_h))
        self.canvas.create_line(225, 225, x_h, y_h, fill="#ef4444", width=4, tags="wszystko")
        
        # 2. Wskazówka minutowa (ŚREDNICA)
        x_mA = 225 + 185 * math.sin(math.radians(kat_m))
        y_mA = 225 - 185 * math.cos(math.radians(kat_m))
        x_mB = 225 - 185 * math.sin(math.radians(kat_m))
        y_mB = 225 + 185 * math.cos(math.radians(kat_m))
        self.canvas.create_line(x_mA, y_mA, x_mB, y_mB, fill="#3b82f6", width=2, tags="wszystko")
        
        # Obliczanie Ortosa (odchylenie od 90 stopni)
        kat_m_mod = kat_m % 180
        kat_h_mod = kat_h % 180
        rozny_kat = abs(kat_h_mod - kat_m_mod)
        if rozny_kat > 90:
            rozny_kat = 180 - rozny_kat
            
        ortos = abs(90 - rozny_kat)
        
        # Wykrywanie "Momentu Ortos" (Zielony punkt zbieżności)
        if ortos < 1.5:
            self.canvas.create_oval(215, 215, 235, 235, fill="#10b981", outline="", tags="wszystko")
            self.lbl_nowy_czas.config(fg="#10b981")
        else:
            self.canvas.create_oval(220, 220, 230, 230, fill="#ef4444", outline="", tags="wszystko")
            self.lbl_nowy_czas.config(fg=fg_color)

        # Wyświetlanie nowego formatu czasu
        self.lbl_nowy_czas.config(
            text=f"{sfera} Cykl: {h%12} | Ortos: {ortos:.2f}"
        )
        self.lbl_tradycyjny.config(
            text=f"Tradycyjny podgląd: {h:02d}:{m:02d}:{s:02d}"
        )
        
        self.root.after(1000, self.aktualizuj_zegar)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZegarekSystemu3_9(root)
    root.mainloop()
