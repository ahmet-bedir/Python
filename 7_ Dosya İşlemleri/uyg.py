"""
dosya = open("metin.txt","w",encoding="cp1254")
dosya.write("ağıt\n")
dosya.seek(5)
liste = ["a\n","b\n","c\n","ç\n"]
dosya.writelines(liste)
dosya.close()
"""
# cp1254 ile kodlanmış bir belgeyi UTF-8 ile açmaya kalkışırsanız veya siz hiçbir kod çözücü belirtmediğiniz halde kullandığınız işletim sistemi öntanımlı olarak dosyaları açmak için cp1254 harici bir kod çözücüyü kullanıyorsa, dosyayı okuma esnasında 'UnicodeDecodeError' hatası alırsınız. Hata almamak için open foksiyonunun errors parametresini kullanmalısınız. 
with open("metin.txt",encoding="utf-8",errors="ignore") as dosya:
    print(dosya.read())
#'ignore' değerini kullanarak, Python’ın kodlanamayan karakterleri görmezden gelmesini sağlıyoruz. 'replace' değeri ise kodlanamayan karakterlerin yerine \ufffd karakterini yerleştirecektir. Bazı yerlerde bu karakteri elmas şeklinde siyah bir küp içine yerleştirilmiş soru işareti şeklinde görebilirsiniz.