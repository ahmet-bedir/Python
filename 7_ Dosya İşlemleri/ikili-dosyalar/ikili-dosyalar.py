### PDF dosyasından bilgi alma.
with open("bilgi-iletisim-teknolojileri.pdf","rb") as file:
    okunan = file.read()
    print(okunan[1:8])
    producer_index = okunan.index(b"/Producer")
    
    print(okunan[producer_index:producer_index+80])
    
###
print('#'*40)

liste = ["git-commands.pdf","git-commands.html","metin.txt"]
for dosya in liste:
    print(open(dosya,"rb").read(22))
    print('---')
    
    
###
print('#'*40)

liste = ["git-commands.html","metin.txt"]
for dosya in liste:
    print(open(dosya,"r").read(22))
    print('---')