"""
4. Film Yosh Cheklovi: Foydalanuvchidan yoshini so'rang. Agar yosh 13 dan kichik bo'lsa,
"Sizga ushbu film tavsiya etilmaydi" deb chiqaring. Agar 13 dan 17 gacha bo'lsa, "Siz filmni
ota-onangiz bilan ko'rishingiz mumkin". Agar 18 va undan katta bo'lsa, "Siz filmni tomosha
qilishingiz mumkin" deb chiqaring.
"""
yosh=int(input("yoshingizni kiriting: "))
if yosh<13:
    chiqar="Sizga ushbu film tavsiya etilmaydi"
elif 13<=yosh<=17:
    chiqar="Siz filmni ota-onangiz bilan ko'rishingiz mumkin"
else:
    chiqar="Siz filmni tomosha qilishingiz mumkin"
#-------------------------
print(chiqar)
