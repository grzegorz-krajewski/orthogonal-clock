import tkinter as tk
import math
import time

class ZegarOrtosOznaczony3_9:
    def __init__(self, root):
        self.root = root
        self.root.title("Zegarek Systemu 3-9 z Oznaczeniami i Trendem")
        self.root.geometry("500x620")
        self.root.resizable(False, False)
        
        self.canvas = tk.Canvas(self.root, width=500, height=500, bg='#0f172a', highlightthickness=0)
        self.canvas.pack()
        
        self.lbl_czas = tk.Label(self.root, text="", font=("Courier New", 14, "bold"), fg="#f8fafc", bg="#1e293b")
        self.lbl_czas.pack(fill="both", expand=True)
        
        self._last_ortos_val = 0.0
        self.aktualizuj_mechanizm()

    def aktualizuj_mechanizm(self):
        self.canvas.delete("all")
        
        czas_teraz = time.time()
        t = time.localtime(czas_teraz)
        h, m, s = t.tm_hour, t.tm_min, t.tm_sec
        ułamki_sekund = czas_teraz % 1
        
        kat_h = (h % 12 + m / 60 + (s + ułamki_sekund) / 3600) * 30
        kat_m = (m + (s + ułamki_sekund) / 60) * 6

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
                xt = 250 + 152 * math.sin(rad_rys)
                yt = 250 - 152 * math.cos(rad_rys)
                
                if ortos_val == 90:
                    etykieta = f"Cykl {(i // 30) % 12}"
                else:
                    etykieta = f"{int(ortos_val)} Ortos"
                    
                self.canvas.create_text(xt, yt, text=etykieta, fill="#94a3b8", font=("Helvetica", 7))

        self.canvas.create_polygon(250, 45, 243, 25, 257, 25, fill="#ef4444")
        self.canvas.create_text(250, 15, text="BIEŻĄCY CYKL", fill="#ef4444", font=("Helvetica", 8, "bold"))
        self.canvas.create_line(250, 45, 250, 70, fill="#ef4444", width=2, dash=(2,2))

        rad_m = math.radians(kat_m)
        x_m = 250 + 170 * math.sin(rad_m)
        y_m = 250 - 170 * math.cos(rad_m)
        self.canvas.create_line(250, 250, x_m, y_m, fill="#3b82f6", width=2, arrow=tk.LAST)
        
        self.canvas.create_oval(244, 244, 256, 256, fill="#e2e8f0", outline="#0f172a", width=2)

        kat_m_mod = kat_m % 180
        kat_h_mod = kat_h % 180
        rozny_kat = abs(kat_h_mod - kat_m_mod)
        if rozny_kat > 90:
            rozny_kat = 180 - rozny_kat
            
        ortos_pelny = abs(90 - rozny_kat)
        ortos = int(ortos_pelny)
        centi = int((ortos_pelny - ortos) * 100)

        # Wykrywanie trendu
        trend = "↓" if ortos_pelny < self._last_ortos_val else "↑"
        self._last_ortos_val = ortos_pelny

        sfera = "[+]" if not (3 <= h < 9) else "[-]"
        
        self.lbl_czas.config(
            text=f"{sfera} Cykl: {h%12} | Ortos: {ortos}° {trend} | Centi: {centi:02d}\n"
                 f"Odświeżanie: co 1 Centi (~109 ms)\n"
                 f"Tradycyjny podgląd: {h:02d}:{m:02d}:{s:02d}"
        )
        
        self.root.after(109, self.aktualizuj_mechanizm)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZegarOrtosOznaczony3_9(root)
    root.mainloop()
