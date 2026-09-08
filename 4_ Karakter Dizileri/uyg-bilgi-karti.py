
print("╔══════════════════════════╗")
print("║    Kişisel Bilgi Kartı   ║")
print("╚══════════════════════════╝")
print()

isim = input("👤 Adınız: ")
yas = int(input("🎂 Yaşınız: "))
meslek = input("💼 Mesleğiniz: ")
hobi = input("🎮 Hobiniz: ")

dogum_yili = 2026 - yas

print()
print("━" * 30)
print(f"  İsim    : {isim}")
print(f"  Yaş     : {yas}")
print(f"  Doğum   : {dogum_yili} ~")
print(f"  Meslek  : {meslek}")
print(f"  Hobi    : {hobi}")
print("━" * 30)
print(f"  {isim}, Python öğreniyor! 🐍")
