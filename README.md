# Project: 3-9 System Clock (Orthogonal Chronometry)

## 💡 Concept Description
An original system of time organization and reading based on the geometry of classic clock hands. The project completely rejects the traditional division of an hour into 60 equal minutes in favor of reading the geometric tension between hands.

This branch introduces the **Single-Hand/No-Hand Mechanical Concept**, reducing visual noise and maximizing zen minimalism by using a rotating dial.

### Main Rules:
* **The dial** is physically attached to the hour hand and rotates with it.
* **The top indicator** (where 12:00 usually is) serves as the static reading point for the current **Cycle**.
* **The blue Orthos hand** sweeps the rotating dial to show the current deviation from perpendicularity.
* **The base axis (horizon)** of the system is the 3:00 and 9:00 line. It divides the day into an upper sphere (day/peak) and a lower sphere (night/rest).

---

## ⏳ How to read time in the 3-9 System?

Full time notation in this system consists of four elements, e.g., **`[+] Cycle: 7 | Ortos: 45° ↓ | Centi: 12`**

1. **Sphere `[+]` or `[-]`** - Determines whether the time is in the upper diurnal sphere or the lower sphere.
2. **Cycle** - The equivalent of a traditional hour (from 0 to 11). Read directly at the exact top (12 o'clock position) of the rotating dial.
3. **Ortos** - The degree of deviation from perpendicularity. Indicated by the position of the blue hand on the rotating dial (from `0°` to `90°`).
4. **Trend `↓` or `↑`** - Indicates whether the time is flowing towards harmony (Orthos is decreasing to `0°` -> `↓` Down) or moving away from it (Orthos is increasing to `90°` -> `↑` Up).
5. **Centi** - The smallest unit of the system, representing 1/100th of an Orthos. The clock updates precisely every 1 Centi (~109 ms).

### ⏱️ Short Cyberpunk Notation (Quick Read)
For communication and cryptographic purposes, you can use a compressed data string without spaces:
**Format:** `[Sphere][Cycle] [Orthos][Trend]`
* **Example:** `+7 45U` -> Upper Sphere [+], Cycle 7, 45 Orthos, Trend increasing (Up).
* **Example:** `-2 10D` -> Lower Sphere [-], Cycle 2, 10 Orthos, Trend decreasing (Down).

---

## 📁 Repository Contents
* `orthos_time.py` - Core time library (Calculates spheres, cycles, orthos, and trend).
* `orthos_cipher.py` - Cryptographic library (Dynamic cipher shifting based on the current Orthos trend).
* `przyklad_kompletny.py` - Complete execution file (Clear text, open for testing).
* `zegar_mechaniczny.py` - Visual Python mechanical simulator (With rotating dial and trend arrows).
* `mechanizm.txt` - Technical description of the dial and wave time effect.
* `epoki.txt` - Macro-scale time breakdown for solar years and cosmic epochs.
* `skala.txt` - Mathematical proof with a list of 22 moments of perpendicularity.

## ⚖️ Copyright & License
Copyright (c) 2026. All Rights Reserved. The source code and mathematical concept are the private property of the author of this repository. Copying, distribution, and use without the author's consent are prohibited.
