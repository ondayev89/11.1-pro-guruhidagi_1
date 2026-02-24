""""
3. Tizimga Kirish: Foydalanuvchidan login va parolni so'rang. Agar login "admin" va parol
"12345" bo'lsa, "Xush kelibsiz, admin!" deb chiqaring. Agar login yoki parol noto'g'ri bo'lsa,
"Login yoki parol xato" deb chiqaring.
"""
login=input("Login: ")
password=input("parol: ")
if login=="admin" and password=="12345":
    print("Xush kelibsiz, admin!")
else:
    print("login yoki parol xato")