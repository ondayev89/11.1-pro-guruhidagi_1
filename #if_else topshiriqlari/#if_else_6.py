"""
6. Email Tekshiruvi: Foydalanuvchidan email manzilini inputda kiritishni so'rang. Agar
emailda "@" belgisi va "." nuqtasi bo'lmasa, "Noto'g'ri email manzili" deb chiqaring. Aks
holda, "Email qabul qilindi" deb chiqaring.
"""
e_mail=input("E-Mail manzilngizni kiriting: ")
e_mail=e_mail.strip()
if e_mail.find("@" and ".")!=-1:
    print("Email qabul qilindi")
else:
    print("Noto'g'ri email manzili")