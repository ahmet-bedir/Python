#Kontrol mekanizması bulunmamaktadır...
print("""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")
giris = input("İşleminiz : ")

hesap = eval(giris)
print("Sonuç :", hesap)


#Burada ise, veri eval() fonksiyonuna ulaşmadan önce kontrolden geçiriliyor. Eğer veri ancak kontrol aşamasından geçerse eval() fonksiyona ulaşabilecek ve oradan da çıktı olarak verilebilecektir.
izinli_karakterler = "0123456789+-/*= "

print("""
Basit bir hesap makinesi uygulaması.

İşleçler:

    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme

Yapmak istediğiniz işlemi yazıp ENTER
tuşuna basın. (Örneğin 23 ve 46 sayılarını
çarpmak için 23 * 46 yazdıktan sonra
ENTER tuşuna basın.)
""")

while True:
    veri = input("İşleminiz (Çıkış 'q') : ")
    if veri == "q":
        print("Çıkılıyor...")
        break

    for s in veri:
        if s not in izinli_karakterler:
            print("Yanlış İşlem!")
            quit()

    hesap = eval(veri)

    print("Sonuç :", hesap)