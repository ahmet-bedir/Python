# "a" : (Append) Ekleme. Dosya konumda yoksa oluşturur. Varsa dosyaya ekleme yapar.
# "r" : (Read) Okuma. Dosya konumda yoksa hata verir.
# "w" : (Write) Yazma modu. 
#    ** Dosyayı konumda oluşturur. 
#    ** Dosya mevcut ise dosyayı siler ve yeniden oluşturur. 
# "r+": Hem okuma hem yazma modunda açılır. Dosya konumda yoksa hata verir.

#Dosyaların Sonunda Değişiklik Yapmak
with open("markalar.txt","a") as file:
    file.write("6-Bmw\n")


#Dosyaların Başında Değişiklik Yapmak
with open("markalar.txt","r+", encoding="utf-8") as file:
     markalar = file.read()
     print(markalar)
     
     input("Dosyaya ekleme yapmak için bir tuşa basınız.")
     
     markalar = "1-Toyota\n" + markalar
     file.seek(0)
     file.write(markalar)
     
     print(markalar)


#Dosyaların Ortasında Değişiklik Yapmak
with open("markalar.txt","r+",encoding="utf-8") as file:
    markalar = file.readlines()
    markalar.insert(2, "3-Renault\n")
    file.seek(0)
    file.writelines(markalar) #writelines() metodu ile bir dosyaya yalnızca liste veri tipinde veriler yazılabilir.
    
    """
    veya...
    for marka in markalar:
        file.write(marka) #write() metodu ile bir dosyaya yalnızca karakter dizileri yazılabilir.
    """


with open("markalar.txt", "r", encoding="utf-8") as file:
    print(file.read())