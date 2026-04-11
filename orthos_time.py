"""
Orthos Time Library - System 3-9
Copyright (c) 2026. All Rights Reserved.
"""
import math
import time

# Zmienna globalna do przechowywania poprzedniej wartości Ortosa (do badania trendu)
_last_orthos = 0.0

def get_3_9_time():
    """
    Gets the current system time and converts it to the 3-9 System units with trend.
    Returns a tuple: (sphere, cycle, orthos, centi, trend)
    """
    global _last_orthos
    
    t = time.localtime()
    h, m, s = t.tm_hour, t.tm_min, t.tm_sec
    
    sphere = "[-]" if 3 <= h < 9 else "[+]"
    cycle = h % 12
    
    angle_h = (h % 12 + m / 60 + s / 3600) * 30
    angle_m = (m + s / 60) * 6
    
    angle_m_mod = angle_m % 180
    angle_h_mod = angle_h % 180
    diff_angle = abs(angle_h_mod - angle_m_mod)
    if diff_angle > 90:
        diff_angle = 180 - diff_angle
        
    orthos_full = abs(90 - diff_angle)
    orthos = int(orthos_full)
    centi = int((orthos_full - orthos) * 100)
    
    # Wyznaczanie trendu (Spadek / Wzrost)
    if orthos_full < _last_orthos:
        trend = "↓" # Zbliżanie do zera
    else:
        trend = "↑" # Oddalanie od zera
        
    _last_orthos = orthos_full
    
    return sphere, cycle, orthos, centi, trend

def format_time(sphere: str, cycle: int, orthos: int, centi: int, trend: str) -> str:
    """Returns a readable string formatted in the 3-9 System."""
    return f"{sphere} Cycle: {cycle} | Orthos: {orthos}° {trend} | Centi: {centi:02d}"
