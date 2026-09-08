# Tek dosyayı kontrol işlemi.
dosya = open("1_os.jpg","rb")
veri = dosya.read(10)
print(veri)
print(veri[6:])
print(veri[6:11] in b"JFIF")

if veri[6:11] in [b"JFIF", b"Exif"]:
	print("JPEG Dosyasıdır.")
else:
	print("JPEG Dosyası Değildir!")

dosya.close()

print('\n', '*'*45, '\n', sep='')

# Çok dosyayı kontrol işlemi.
dosyalar = ["dosya1","dosya2","dosya3","dosya4","dosya5","dosya6"]
for dosya in dosyalar:
	with open(dosya,"rb") as file:
		okunan = file.read(16)
		print(okunan)
		
		if okunan[6:10] in [b"JFIF", b"Exif"]:
		    print(f"'{dosya}' Dosyası JPEG Dosyasıdır.\n")
		    
		elif okunan[1:4] in b"PNG":
		    print(f"'{dosya}' Dosyası PNG Dosyasıdır.\n")
		
		else:
		    print(f"'{dosya}' Dosyası Bilinmeyen Bir Dosya Türüdür!\n")