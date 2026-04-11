import tkinter as tk
import math
import time

class ZegarSystemu3_9:
    def __init__(self, root):
        self.root = root
        self.root.title("Zegar Systemu 3-9")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(self.root, width=500, height=450, bg='white')
        self.canvas.pack()
        
        self.label_info = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"))
        self.label_info.pack(pady=10)
        
        self._last_orthos = 0.0
        self.rysuj_podstawe()
        self.aktualizuj_czas()

    def rysuj_podstawe(self):
        self.canvas.create_oval(50, 25, 450, 425, outline="#d3d3d3", width=2)
        self.canvas.create_line(50, 225, 450, 225, fill="#e0e0e0", dash=(4, 2))
        self.canvas.create_line(250, 25, 250, 425, fill="#e0e0e0", dash=(4, 2))
        self.canvas.create_text(435, 225, text="3", font=("Helvetica", 16, "bold"), fill="gray")
        self.canvas.create_text(65, 225, text="9", font=("Helvetica", 16, "bold"), fill="gray")

    def aktualizuj_czas(self):
        self.canvas.delete("wskazowka")
        
        t = time.localtime()
        h, m, s = t.tm_hour, t.tm_min, t.tm_sec
        
        kat_h = (h % 12 + m / 60 + s / 3600) * 30
        kat_m = (m + s / 60) * 6
        
        # Wskazówka minutowa (Średnica)
        x_mA = 250 + 190 * math.sin(math.radians(kat_m))
        y_mA = 225 - 190 * math.cos(math.radians(kat_m))
        x_mB = 250 - 190 * math.sin(math.radians(kat_m))
        y_mB = 225 + 190 * math.cos(math.radians(kat_m))
        self.canvas.create_line(x_mA, y_mA, x_mB, y_mB, fill="#3b82f6", width=3, tags="wskazowka")
        
        # Wskazówka godzinowa
        x_h = 250 + 120 * math.sin(math.radians(kat_h))
        y_h = 225 - 120 * math.cos(math.radians(kat_h))
        self.canvas.create_line(250, 225, x_h, y_h, fill="#ef4444", width=5, tags="wskazowka")
        
        # Obliczanie Ortosa i Centi
        kat_m_mod = kat_m % 180
        kat_h_mod = kat_h % 180
        rozny_kat = abs(kat_h_mod - kat_m_mod)
        if rozny_kat > 90:
            rozny_kat = 180 - rozny_kat
            
        ortos_pelny = abs(90 - rozny_kat)
        ortos = int(ortos_pelny)
        centi = int((ortos_pelny - ortos) * 100)
        
        # Badanie trendu (Spadek / Wzrost)
        trend = "↓" if ortos_pelny < self._last_orthos else "↑"
        self._last_orthos = ortos_pelny
        
        sfera = "[+]" if not (3 <= h < 9) else "[-]"
        
        self.label_info.config(
            text=f"{sfera} Cykl: {h%12} | Ortos: {ortos}° {trend} | Centi: {centi:02d}"
        )
        
        self.root.after(109, self.aktualizuj_czas)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZegarSystemu3_9(root)
    root.mainloop()
