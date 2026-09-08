class Program():
    def __init__(self):
        pass
    #versiyon() adlı metodu @property bezeyicisi ile bu metodu bir ‘nitelik’ haline getirmiş olduk.
    @property
    def versiyon(self):
        return '0.1'
        
program = Program()
version = program.versiyon
print(version)

version = program.version = "0.2" #Normalde bir metodu değer atama işlemi ile değiştiremeyiz ancak @property bezeyicisi bu işleme olanak sağlar.
print(version)