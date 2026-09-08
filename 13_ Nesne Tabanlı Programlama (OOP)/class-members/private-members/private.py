class Sinif():
    sinif_niteligi = 'sınıf niteliği'
    __gizli = "gizli data"

    def ornek_metodu(self):
        print('örnek metodu')
        print(self.__gizli) #Gizli üyeler yalnızca sınıf dışına kapalıdır. Bu üyelere sınıf içinden rahatlıkla erişebiliriz. Mesela __gizli adlı değişkene ornek_metodu() içinden normal bir şekilde erişebiliyoruz.

    @classmethod
    def sinif_metodu(cls):
        print('sınıf metodu')

    @staticmethod
    def statik_metot():
        print('statik metot')