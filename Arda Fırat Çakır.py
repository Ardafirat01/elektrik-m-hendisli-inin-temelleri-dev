import numpy as np

"""
BASIT DEVRE ANALİZİ
"""

print("KIRCHHOFF DEVRE ANALİZİ - MATRİS YÖNTEMİ")
print("=" * 40)
print("\nDevre: 12V kaynağı, R1=2Ω, R2=4Ω")

# Adım 1: İletkenlik matrisi
G = 1/2 + 1/4  # G = 1/R1 + 1/R2

# Adım 2: Akım vektörü
I = 12/2  # Kaynaktan gelen akım

# Adım 3: Düğüm gerilimini bul
V1 = I / G

print(f"\nDüğüm Gerilimi: V1 = {V1:.2f} V")

# Adım 4: Dal akımları
I1 = (12 - V1) / 2
I2 = V1 / 4

print(f"\nAkımlar:")
print(f"  I1 = {I1:.2f} A")
print(f"  I2 = {I2:.2f} A")

# Adım 5: Güçler
P1 = I1**2 * 2
P2 = I2**2 * 4

print(f"\nGüçler:")
print(f"  P1 = {P1:.2f} W")
print(f"  P2 = {P2:.2f} W")
print(f"  Toplam = {P1+P2:.2f} W")

print("=" * 40)