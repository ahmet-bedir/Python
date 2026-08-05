"""
belge dizisi (docstring) veya
belgelendirme dizisi (documentation string)
"""
sozluk = {
	"kitap"       : "book",
	"bilgisayar"  : "computer",
	"programlama" : "programming"}

def ara(kelime):
    sorgu = sozluk.get(kelime, "hata")
    if sorgu == "hata":
        return  "'{}' kelimesi sözlükte bulunmamaktadır!".format(kelime)
    else:
	    return "'{}' kelimesinin ingilizce karşılığı : {}".format(kelime,sozluk[kelime])

def ekle(kelime, ing_anlam):
	mesaj = "'{}' kelimesi sözlüğe eklendi!"
	sozluk[kelime] = ing_anlam
	print(mesaj.format(kelime))

def sil(kelime):
	try:
		sozluk.pop(kelime)
	except KeyError as err:
		print(err, "kelimesi bulunamadı!")
	else:
		print("'{}' kelimesi sözlükten silindi!".format(kelime))