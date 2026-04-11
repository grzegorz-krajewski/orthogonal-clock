import tkinter as tk
import math
import time

class ZegarOrtogonalny:
    def __init__(self, root):
        self.root = root
        self.root.title("Zegar Systemu 3-9")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        
        # Tworzenie płótna do rysowania
        self.canvas = tk.Canvas(self.root, width=500, height=450, bg='white')
        self.canvas.pack()
        
        # Etykieta do wyświetlania unikalnej wartości
        self.label_info = tk.Label(self.root, text="", font=("Helvetica", 14, "bold"))
        self.label_info.pack(pady=10)
        
        self.rysuj_podstawe()
        self.aktualizuj_czas()

    def rysuj_podstawe(self):
        # Rysowanie statycznej tarczy
        self.canvas.create_oval(50, 25, 450, 425, outline="#d3d3d3", width=2)
        # Oś horyzontalna (3-9)
        self.canvas.create_line(50, 225, 450, 225, fill="#e0e0e0", dash=(4, 2))
        # Oś pionowa
        self.canvas.create_line(250, 25, 250, 425, fill="#e0e0e0", dash=(4, 2))
        
        # Punkty bazowe 3 i 9
        self.canvas.create_text(435, 225, text="3", font=("Helvetica", 16, "bold"), fill="gray")
        self.canvas.create_text(65, 225, text="9", font=("Helvetica", 16, "bold"), fill="gray")

    def aktualizuj_czas(self):
        self.canvas.delete("wskazowka")
        
        # Pobieranie aktualnego czasu
        t = time.localtime()
        h, m, s = t.tm_hour, t.tm_min, t.tm_sec
        
        # Obliczanie kątów (w stopniach)
        kat_h = (h % 12 + m / 60 + s / 3600) * 30
        kat_m = (m + s / 60) * 6
        
        # 1. WSKAZÓWKA MINUTOWA JAKO ŚREDNICA
        # Punkt A (zgodny z minutą)
        x_mA = 250 + 190 * math.sin(math.radians(kat_m))
        y_mA = 225 - 190 * math.cos(math.radians(kat_m))
        # Punkt B (przeciwległy)
        x_mB = 250 - 190 * math.sin(math.radians(kat_m))
        y_mB = 225 + 190 * math.cos(math.radians(kat_m))
        
        self.canvas.create_line(x_mA, y_mA, x_mB, y_mB, fill="#3b82f6", width=3, tags="wskazowka")
        
        # 2. WSKAZÓWKA GODZINOWA (Krótszy promień)
        x_h = 250 + 120 * math.sin(math.radians(kat_h))
        y_h = 225 - 120 * math.cos(math.radians(kat_h))
        self.canvas.create_line(250, 225, x_h, y_h, fill="#ef4444", width=5, tags="wskazowka")
        
        # 3. OBLICZANIE UNIKALNEJ WARTOŚCI MINUTY (odchylenie od 90 stopni)
        kat_m_pelny = kat_m % 180
        kat_h_pelny = kat_h % 180
        rozny_kat = abs(kat_h_pelny - kat_m_pelny)
        
        if rozny_kat > 90:
            rozny_kat = 180 - rozny_kat
            
        wartosc_unikalna = abs(90 - rozny_kat)
        
        # Efekt tła przy prostopadłości
        if wartosc_unikalna < 2.0:
            self.canvas.config(bg="#ecfdf5") # Pastelowa zieleń w momencie zbieżności
        else:
            self.canvas.config(bg="white")
            
        # Aktualizacja napisów
        self.label_info.config(
            text=f"Tradycyjny: {h:02d}:{m:02d}:{s:02d}  |  Twoja wartość: {wartosc_unikalna:.2f}"
        )
        
        self.root.after(1000, self.aktualizuj_czas)

# Uruchomienie aplikacji
if __name__ == "__main__":
    root = tk.Tk()
    app = ZegarOrtogonalny(root)
    root.mainloop()
