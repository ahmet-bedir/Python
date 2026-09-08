markalar = ["opel","bmw","togg"]

# i = 1
# for marka in markalar:
#     print(f"{i}.{marka}")
#     i += 1
#
#
# for i,marka in enumerate(markalar,1):
#     print(f"{i}-{marka}")

# obj = enumerate(markalar,1)
# print(type(obj))
# obj = list(obj)
# for i,marka in obj:
#     print(f"{i}_{marka}")

### zip metodu liste birleştirmek için kullanılır...

numara = [100,200,300]
ogrenci = ["Ali","Ayşe","Canan","Mehmet"]

print(list(zip(numara,ogrenci)))

for no,isim in zip(numara,ogrenci):
    print(no,isim)
