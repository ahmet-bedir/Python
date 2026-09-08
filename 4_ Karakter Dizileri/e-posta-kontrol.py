# E-posta Doğrulama
def email_gecerli_mi(email):
    """Basit e-posta format kontrolü"""
    if " " in email:
        return False
    if email.count("@") != 1:
        return False
    
    kullanici, domain = email.split("@")
    
    if len(kullanici) == 0:
        return False
    if "." not in domain:
        return False
    if len(domain.split(".")[-1]) < 2:
        return False
    
    return True
    
testler = [
    "ali@example.com",
    "test@test",
    "@example.com",
    "ali veli@test.com",
    "ali@@test.com",
]

for email in testler:
    sonuc = "✅" if email_gecerli_mi(email) else "❌"
    print(f"{sonuc} {email}")