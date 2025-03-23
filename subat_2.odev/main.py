def tek_cift():
    sayi = int(input("Bir sayı girin: "))
    
    if sayi % 2 == 0:
        print(f"{sayi} çift bir sayıdır.")
    else:
        print(f"{sayi} tek bir sayıdır.")

def not_sistemi():
    not_puan = int(input("Notunuzu girin (0-100 arası): "))
    
    if 90 <= not_puan <= 100:
        print("Harf Notu: A")
    elif 80 <= not_puan < 90:
        print("Harf Notu: B")
    elif 70 <= not_puan < 80:
        print("Harf Notu: C")
    elif 60 <= not_puan < 70:
        print("Harf Notu: D")
    elif 0 <= not_puan < 60:
        print("Harf Notu: F")
    else:
        print("Geçersiz not girdiniz!")

def yas_grubu():
    yas = int(input("Yaşınızı girin: "))
    
    if 0 <= yas <= 12:
        print("Yaş Grubu: Çocuk")
    elif 13 <= yas <= 19:
        print("Yaş Grubu: Genç")
    elif 20 <= yas <= 59:
        print("Yaş Grubu: Yetişkin")
    elif yas >= 60:
        print("Yaş Grubu: Yaşlı")
    else:
        print("Geçersiz yaş girdiniz!")

# Ana program
while True:
    print("\nSeçenekler:")
    print("1. Sayının Tek mi Çift mi Olduğunu Bul")
    print("2. Not Sistemi")
    print("3. Yaş Grubu")
    print("4. Çıkış")
    
    secim = input("Bir seçenek girin: ")

    if secim == "1":
        tek_cift()

    elif secim == "2":
        not_sistemi()

    elif secim == "3":
        yas_grubu()

    elif secim == "4":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")

