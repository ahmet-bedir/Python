dosya = open("log.txt", "r")
print(*[metot for metot in dir(dosya) if not metot.startswith("_")], sep="\n")
print('#'*33)
"""
Bu nitelik, bir dosyanın kapalı olup olmadığını sorgulamamızı sağlar.
Eğer dosya kapalıysa True çıktısı, açıksa False çıktısı verilecektir.
"""
print(dosya.closed) #False
dosya.close()
print(dosya.closed) #True

#readable() Metodu bir dosyanın okuma yetkisine sahip olup olmadığını sorgulamamızı sağlar. Eğer bir dosya “r” gibi bir kiple açılmışsa, yani o dosya ‘okunabilir’ özellikle ise bu metot bize True çıktısı verir. Ama eğer dosya yazma kipinde açılmışsa bu metot bize False çıktısı verecektir.
print(dosya.readable()) #True

#writable() Metodu bir dosyanın yazma yetkisine sahip olup olmadığını sorgulamamızı sağlar. Eğer bir dosya “w” gibi bir kiple açılmışsa, yani o dosya ‘yazılabilir’ özellikle ise bu metot bize True çıktısı verir. Ama eğer dosya okuma kipinde açılmışsa bu metot bize False çıktısı verecektir.
print(dosya.writable()) #False


#truncate() Metodu ile dosyalarımızı istediğimiz boyuta getirebiliyoruz.
with open("log.txt","r+") as dosya:
    print("### dosyanın ilk hali ###", dosya.read(), sep='\n')
    
    dosya.truncate(5)
    
    dosya.seek(0)
    print("### dosyanın son hali ###", dosya.read(), sep='\n')
    

#mode niteliği bize bir dosyanın hangi kipte açıldığına dair bilgi verir:
f = open("log.txt")
print(f.mode) #'r'

#name niteliği bize bir dosyanın adını verir:
print(f.name) #'falanca.txt'

#encoding niteliği bir dosyanın hangi dil kodlaması ile kodlandığını söyler:
print(f.encoding) #'utf-8' veya 'cp1254' => Windows