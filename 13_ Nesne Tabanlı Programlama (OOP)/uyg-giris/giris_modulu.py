class Giris():
    def __init__(self, mesaj='Müşteri numaranızı giriniz: '):
        cevap = input(mesaj)
        print('Hoşgeldiniz!')

    #Aynı zamanda bir parola ve TC Kimlik Numarası ile de giriş imkanı sağlamak istersek, sınıf metotlarından yararlanabiliriz:
    @classmethod
    def paroladan(cls):
        mesaj = 'Parolanızı giriniz: '
        cls(mesaj)

    @classmethod
    def tcden(cls):
        mesaj = 'TC kimlik numaranızı giriniz: '
        cls(mesaj)