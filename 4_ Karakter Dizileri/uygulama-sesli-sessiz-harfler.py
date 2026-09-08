###
sesli_harfler = "aAeEıIiİoOöÖuUüÜ "
sessiz_harfler = "bBcCçÇdDfFgGğĞhHjJkKlLmMnNpPrRsSşŞtTvVyYzZ "
sesli = ""
sessiz = ""

kelime = input("Kelime Giriniz : ")
for harf in kelime: #kelime değişkenindeki her karakteri 'harf' değişkenine attık.
    if harf in sesli_harfler: #'harf' sesli_harfler değişkeninin içerisinde varsa...
        sesli += harf #'sesli' ye harf değişkenini ekle.
    else:
        sessiz += harf #yoksa 'sessiz' e ekle.
        
print("Kelime :", kelime)
print("Sesliler :", sesli)
print("Sessizler :", sessiz)