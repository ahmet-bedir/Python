######################################

    
#print("Ç".encode("ascii")) #ASCII kodlama sisteminde 'Ç' harfi bulunmadığı için hata alırız.
print("a".encode("ascii")) #b'a'
print("a".encode("cp857")) #b'a'
print("a".encode("utf-8")) #b'a'
print("Bu türkçe bir cümledir.".encode("ascii", errors="ignore"))

###
karakter = "Ç".encode("utf-8") #b'\xc3\x87'(c387 sayısı utf-8 kod çözücüsünde 'Ç' harfine karşılık gelir)
str_karakter = str(karakter)[4:6]+str(karakter)[8:10]

sayi = (int(str_karakter,16)) #50055
uzunluk = sayi.bit_length()
print(f"'Ç' harfi utf-8 kod çözücüsünde {uzunluk} bit, {uzunluk//8} bayt uzunluğundadır.")


"""
print("ß".encode("latin1")) #b'\xdf'
print(int("df",16)) #223

print("€".encode("cp1254")) #b'\x80'
print(int("80",16)) #128
"""
