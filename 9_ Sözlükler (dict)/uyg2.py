kisiler = {
    "Ahmet": {
        "Memleket": "İstanbul",
        "Meslek"  : "Öğretmen",
        "Yaş"     : 34
    },
    "Mehmet"   : {
        "Memleket": "Adana",
        "Meslek"  : "Mühendis",
        "Yaş"     : 40
    },
    "Seda"    : {
        "Memleket": "İskenderun",
        "Meslek"  : "Doktor",
        "Yaş"     : 30
    }
}
kisi = """
Hakkında ayrıntılı bilgi almak
istediğiniz kişinin adını giriniz : """
kisi = input(kisi)

if kisi in kisiler:
    ayrinti = input("Memleket/Meslek/Yaş? : ")
    if ayrinti in kisiler[kisi]:
        print(kisiler[kisi][ayrinti])
    else:
        print("Yanlış seçim!")
else:
    print("Böyle bir kişi kayıtlı değil!")