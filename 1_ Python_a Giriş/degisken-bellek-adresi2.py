a = [1, 2, 3]
b = a

b.append(4)

print(a)  # [1, 2, 3, 4] — a da değişti!
print(b)  # [1, 2, 3, 4]

"""
Neden a da değişti? Çünkü a ve b aynı listeye referans veriyor. Listeyi b üzerinden değiştirdiğinde, a da aynı listeye baktığı için değişikliği görüyor.
"""