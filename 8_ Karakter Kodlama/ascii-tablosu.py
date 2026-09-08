#ASCII Bilgi Alışverişi için Standart Amerikan Kodu ‘American Standard Code for Information Interchange’ tablosu yedi bitlik bir sistemdir.
for i in range(128):
    if i % 4 == 0:
        print("\n")

    print("|{:<1}{:>7}|\t".format(i, repr(chr(i))), sep="", end="")
print("\n")