###
# İkili (binary) — 0b öneki
binary = 0b1010
print(binary)  # 10

# Sekizli (octal) — 0o öneki
octal = 0o17
print(octal)  # 15

# Onaltılı (hexadecimal) — 0x öneki
hexa = 0xFF
print(hexa)  # 255

# Dönüşüm fonksiyonları
print(bin(255))  # '0b11111111'
print(oct(255))  # '0o377'
print(hex(255))  # '0xff'

###
sayi_sistemleri = ["onlu", "sekizli", "on altılı", "ikili"]

print(("{:^9} "*len(sayi_sistemleri)).format(*sayi_sistemleri))

for i in range(17):
    print("{0:^9} {0:^9o} {0:^9x} {0:^9b}".format(i))
    
### bin() fonksiyonu onlu sistemdeki bir sayının ikili (binary) sayı sistemindeki karşılığını verir.
print(bin(4)) #0b100
print(bin(4)[2:]) #100

### hex() fonksiyonu onlu sistemdeki bir sayının on altılı sistemdeki karşılığını verir.
print(hex(11)) #0xb
print(hex(11)[2:]) #b

### oct() fonksiyonu onlu sistemdeki sayının sekizli sistemdeki karşılığını verir.
print(oct(8)) #0o10
print(oct(8)[2:]) #10

### int() fonksiyonu başka bir sayı sistemindeki sayı değerli karakter dizisini onlu sistemdeki karşılığına dönüştürmek için kullanılıyor.
print(int('a',16)) #10
print(int('101',2)) #5
print(int('10',8)) #8

#
print("{:b}".format(10)) #1010

print("{:x}".format(10)) #a
print("{:X}".format(10)) #A

print("{:o}".format(10)) #12

n = '7bc'
print("{} sayısının onlu karşılığı {:d} sayısıdır.".format(n, int(n, 16)))


#
for i in range(256):
    print(i, bin(i)[2:], hex(i)[2:])