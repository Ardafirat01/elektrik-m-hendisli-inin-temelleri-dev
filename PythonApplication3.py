# İki Dirençli Seri ve Paralel Direnç Hesaplayıcı
# Yazan: ChatGPT (GPT-5)

def seri_direnc(R1, R2):
    """Seri bağlı iki direncin eşdeğer direnci"""
    return R1 + R2

def paralel_direnc(R1, R2):
    """Paralel bağlı iki direncin eşdeğer direnci"""
    if R1 == 0 or R2 == 0:
        return 0  # kısa devre durumu
    return 1 / ((1 / R1) + (1 / R2))

def main():
    print("🔌 İki Dirençli Seri ve Paralel Hesaplayıcı 🔋")
    print("Dirençleri ohm (Ω) cinsinden girin.\n")

    try:
        R1 = float(input("R1 (Ω): "))
        R2 = float(input("R2 (Ω): "))

        if R1 <= 0 or R2 <= 0:
            print("⚠️ Direnç değerleri pozitif olmalıdır!")
            return

        Rs = seri_direnc(R1, R2)
        Rp = paralel_direnc(R1, R2)

        print("\n📊 Hesap Sonuçları:")
        print(f"Seri bağlı eşdeğer direnç: {Rs:.2f} Ω")
        print(f"Paralel bağlı eşdeğer direnç: {Rp:.2f} Ω")

    except ValueError:
        print("⚠️ Lütfen geçerli sayısal bir değer girin!")

if __name__ == "__main__":
    main()

