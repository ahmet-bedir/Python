harfler = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZə"

print('+'+('-'*21)+'+')
print("|{:<10}|{:<10}|".format("karakter", "cp1254"))
print('+'+('-'*21)+'+')

for harf in harfler:
   print("|{:<10}|{:<10}|".format(harf, len(harf.encode("cp1254",errors="ignore"))))
print('+'+('-'*21)+'+')
