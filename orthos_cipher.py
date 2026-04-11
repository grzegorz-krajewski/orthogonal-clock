"""
Orthos Cipher Library - System 3-9
Copyright (c) 2026. All Rights Reserved.
"""

def _generate_key(sphere: str, cycle: int, orthos: int, centi: int, trend: str) -> int:
    """Helper function generating shift vector based on the 3-9 scale and trend."""
    vector = int((cycle * 100) + (orthos * 10) + centi)
    
    # Trend modyfikuje klucz (np. podwaja go przy spadku)
    if trend == "↓":
        vector += 500
        
    return -vector if sphere == "[-]" else vector

def encrypt(text: str, sphere: str, cycle: int, orthos: int, centi: int, trend: str) -> str:
    """Encrypts input text based on the 3-9 System time and trend."""
    vector = _generate_key(sphere, cycle, orthos, centi, trend)
    return "".join(chr((ord(char) + vector) % 1114112) for char in text)

def decrypt(cipher_text: str, sphere: str, cycle: int, orthos: int, centi: int, trend: str) -> str:
    """Decrypts text encrypted with the 3-9 System based on the provided key."""
    vector = _generate_key(sphere, cycle, orthos, centi, trend)
    return "".join(chr((ord(char) - vector) % 1114112) for char in cipher_text)
