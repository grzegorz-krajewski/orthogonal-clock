# Project: 3-9 System Clock (Orthogonal Chronometry)

## 💡 Concept Description
An original system of time organization and reading based on the geometry of classic clock hands. The project completely rejects the traditional division of an hour into 60 equal minutes in favor of reading the geometric tension between hands.

This branch introduces the **Single-Hand Mechanical Concept**, reducing visual noise and maximizing zen minimalism.

### Main Rules:
* **The dial** is physically attached to the hour hand and rotates with it.
* **The top indicator** (where 12:00 usually is) serves as the static reading point for minutes.
* **The base axis (horizon)** of the system is the 3:00 and 9:00 line. It divides the day into an upper sphere (day/peak) and a lower sphere (night/rest).

---

## ⏳ How to read time in the 3-9 System?

Time notation in this system consists of four elements, e.g., **`[+] Cycle: 3 | Orthos: 12 | Centi: 45`**

1. **Sphere `[+]` or `[-]`** - Determines whether the time is in the upper diurnal sphere or the lower sphere.
2. **Cycle** - The equivalent of a traditional hour (from 0 to 11). Indicated by the position of the single hand.
3. **Orthos** - The degree of deviation from perpendicularity. You read this value at the exact top (12 o'clock position) of the rotating dial.
   * `0°` means perfect perpendicularity (The Orthos Moment).
   * `90°` means the hand is pointing straight up or down.
4. **Centi** - The smallest unit of the system, representing 1/100th of an Orthos (taking the place of traditional seconds).

---

## 📁 Repository Contents
* `orthos_time.py` - Core time library (Obfuscated/Hidden source).
* `orthos_cipher.py` - Cryptographic library (Obfuscated/Hidden source).
* `przyklad_kompletny.py` - Complete execution file (Clear text, open for testing).
* `zegar_mechaniczny.py` - Visual Python mechanical simulator (Single-hand version).
* `mechanizm.txt` - Technical description of the dial.
* `skala.txt` - Mathematical proof with a list of 22 moments of perpendicularity.

## ⚖️ Copyright & License
Copyright (c) 2026. All Rights Reserved. The source code and mathematical concept are the private property of the author of this repository. Copying, distribution, and use without the author's consent are prohibited.
