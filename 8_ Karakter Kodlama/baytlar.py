a = b''
print(f"{a} => {type(a)}") #b'' => <class 'bytes'>

#Bayt veri tipi temel olarak ASCII karakterleri kabul eder. Dolayısıyla ASCII tablosu dışında kalan karakterleri doğrudan bayt olarak temsil edemezsiniz:
#a = b'ş' #hata!

#ASCII dışında kalan karakterleri de bayt’a dönüştürmek için bytes() adlı bir fonksiyon kullanılır:
b = bytes("ş", "utf-8") #yada b = "ş".encode("utf-8")
print(b) #b'\xc5\x9f'
b = str(b)[4:6]+str(b)[8:10]
print(b) #c59f sayısı utf-8 kod çözücünde 'ş' harfini temsil etmektedir.
b = int(b,16) #50591
print(bin(b)) #11000101:10011111
print(int("1100010110011111",2)) #50591
print(f"{b.bit_length()} bit.") #16 bit.

##
b = bytes("Fırat", "ascii", errors="xmlcharrefreplace")
print(b) #b'F&#305;rat'


##
print(len(b'')) #0
print(len(b'abc')) #3
print(len(b'abc\xc3\xa7')) #5

print(len(b'\xc3\xa7')) #2
print(len('ç')) #1


### Baytların Metotları
### decode() metodu baytları belli bir kodlama biçimine göre karakter dizilerine dönüştürebilmek için kullanılır.
d = b"\xc4\xb0".decode("utf-8")
print(d)

print('ç'.encode("utf-8")) #b'\xc3\xa7'
print(b'\xc3\xa7'.decode("utf-8")) #ç

### fromhex metodu onaltılı sayma sistemindeki bir sayıdan oluşan bir karakter dizisini alıp, bayta dönüştürür.

print(bytes.fromhex("c4b0")) #b'\xc4\xb0'


### Bayt Dizileri
pdf = bytearray(b'PDF-1.7')
print(pdf)