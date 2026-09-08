print('+'+('-'*72)+'+')
for i in range(1, 5):
    print("|{} bayt kullanırsak toplam 2**{:<2} = {:<13,} karakter kodlanabilinir.|".format(i, i*8, (2**(i*8))))
print('+'+('-'*72)+'+')
    
    
harfler = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZə"
print('+'+('-'*28)+'+')
for s in harfler:
    print("|{:<5}{:<15}{:<8}|".format(s,str(s.encode("utf-8")), str(len(s.encode("utf-8")))+" bayt"))
print('+'+('-'*28)+'+')