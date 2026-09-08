#demetler değiştirilemez (immutable) bir veri tipidir. 
demet = (1,2,3)
print(demet, type(demet)) #(1, 2, 3) <class 'tuple'>

#demet oluşturmanın 2.yolu.
demet = 1,2,3
print(demet, type(demet))

#demet oluşturmanın 3.yolu.
demet = tuple("123")
print(demet, type(demet)) #('1', '2', '3') <class 'tuple'>

#list => tuple
liste = ["ali", "cenk", "murat"]
demet = tuple(liste)
print(demet, type(demet))

#Tek Öğeli bir Demet Tanımlama.
demet = ('ahmet')
print(demet, type(demet)) #ahmet <class 'str'>
demet = ('ahmet',) #veya demet = 'ahmet',
print(demet, type(demet)) #('ahmet',) <class 'tuple'>

###
demet = ('elma', 'armut', 'kiraz')
print(demet[0]) #'elma'
print(demet[-1]) #'kiraz'
print(demet[:2]) #('elma', 'armut')

#
#sonuc = demet[0]
#print(sonuc, type(sonuc))
#demet[0] = "muz" hata! çünkü demetler değiştirilemezler.

demet = ('elma', 'armut', 'kiraz')

#demet += ('muz') #hata! Python programlama dilinde sadece aynı tür verileri birbiriyle birleştirebilirsiniz.
demet += ('muz',)
print(demet)