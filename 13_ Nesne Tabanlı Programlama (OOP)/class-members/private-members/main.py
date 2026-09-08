import private

s = private.Sinif()

print(dir(s))

s.ornek_metodu()

# print(s.__gizli) #hata!
# print(private.Sinif.__gizli) #hata!

print(private.Sinif.sinif_niteligi)

'''
Python’da baş tarafında iki adet alt çizgi olan, ancak uç tarafında alt çizgi bulunmayan bütün öğeler birer gizli üyedir. Dışarıya kapalı olan bu gizli üyelere, normal yöntemleri kullanarak sınıf dışından erişemezsiniz.
'''
