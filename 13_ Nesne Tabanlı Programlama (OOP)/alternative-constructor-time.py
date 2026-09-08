### Tarih oluşturmak için, yıl, ay ve gün bilgilerini date sınıfına elle girebileceğiniz gibi, bugünün tarihi için today() adlı sınıf metodunu kullanabilirsiniz:
import datetime

bugun = datetime.date(2015, 6, 16)

bugun = datetime.date.today()
#İşte böylece, date sınıfının size sunduğu bir alternatif inşacı(alternative constructor) (today()) vasıtasıyla bugünün tarihini otomatik olarak elde etmiş oldunuz.
print(bugun)

### Zaman damgasından bir tarih elde etmek istiyorsanız yine date sınıfının sunduğu bir başka alternatif inşacıdan yararlanabilirsiniz:
import time
zaman_damgasi = time.time()
tarih = datetime.date.fromtimestamp(zaman_damgasi)

print("Tarih:", tarih)
