"""
1. Ob-havo Tavsifi: Foydalanuvchidan ob-havo haroratini inputda so'rang.
Agar harorat 0 dan past bo'lsa, "Sovuq" deb print chiqaring.
Agar 0 dan 20 gacha bo'lsa, "Salqin".
Agar 21 dan 30 gacha bo'lsa, "Iliq".
Agar 31 dan yuqori bo'lsa, "Issiq" deb chiqaring.
"""
a=int(input("taom nomini kiriting: "))
if a<0:
    b="Sovuq"
elif 0<=a<=20:
    b="Salqin"
elif 20<=a<=30:
    b="Iliq"
else:
    b="Issiq"
#-------------------------
print(f"buhun ob havo {b} bo'ladi")
