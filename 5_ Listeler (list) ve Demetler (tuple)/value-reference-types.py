# değer tipler (value types) : bellekte değer olarak tutulur.
x  = 10
y = 20
x = y
y = 30
print("x :", x) #x : 20
print("y :", y) #y : 30


# referans tipler (reference types) : bellekte adres olarak tutulur.
liste1 = [1,2,3]
liste2 = [4,5,6]
liste1 = liste2
liste1[0] = 11
print("liste1 :", liste1) #liste1 : [11, 5, 6]
print("liste2 :", liste2) #liste2 : [11, 5, 6]


# copy metodu ile liste kopyalama (değer tip)
listeA = [1,2,3]
#listeB = listeA.copy() # 1.yol
listeB = list(listeA) # 2.yol
listeA[0] = 11
print("listeA :", listeA) #listeA : [11, 2, 3]
print("listeB :", listeB) #listeB : [1, 2, 3]