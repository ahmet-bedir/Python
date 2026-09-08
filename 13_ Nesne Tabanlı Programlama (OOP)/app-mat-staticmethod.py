class Mat():
    '''Matematik işlemleri yapmamızı sağlayan
    bir sınıf.'''

    @staticmethod
    def pi():
        return 22/7

    @staticmethod
    def karekok(sayi):
        return sayi ** 0.5
        
        
m = Mat()
#örnek üzerinden
print(m.pi())
print(m.karekok(144))

#sınıf üzerinden
print(Mat.pi())
print(Mat.karekok(144))