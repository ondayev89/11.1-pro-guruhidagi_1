"""
9. Ish Jadvalini Tekshirish: Foydalanuvchidan haftaning kunini so'rang (Dushanba,
Seshanba, ... , Yakshanba). Agar kun "Shanba" yoki "Yakshanba" bo'lsa, "Bugun dam olish
kuni" deb chiqaring. Aks holda, "Bugun ish kuni" deb chiqaring.
"""
hafta_kunlari = ["Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba", "Yakshanba"]
hafta_answer=input("hafta kunini kiriting: ")
if hafta_answer.title() in hafta_kunlari[0:4]:
    print("bugun ish kuni")
elif hafta_answer.title() in hafta_kunlari[5:6]:
    print("Bugun dam olish kun")
else:
    print("bunday hafta kuni yo'q")
