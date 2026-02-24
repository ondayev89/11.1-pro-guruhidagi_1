""""
8. Bankomat Pul Yechish: Foydalanuvchidan kartasidagi summani va yechmoqchi
bo'lgan summani so'rang. Ya’ni 2 ta input bo’ladi. Agar kartadagi puli yechiladigan puldan
kam bo'lsa, "Hisobda yetarli mablag' mavjud emas" deb print chiqaring. Agar yechiladigan
summa 5 000 so'mdan kam bo'lsa, "Minimal yechish summasi 5 000 so'm" deb chiqaring.
Aks holda, "Pul muvaffaqiyatli yechildi" deb print chiqaring va kartadagi qolgan mablag'ni
print qiling.
"""
a=int(input("kartasidagi summani kiriting: "))
b=int(input("yechmoqchi bo'lgan summangizni kiriting: "))
if a<5000:
    c="Minimal yechish summasi 5 000 so'm"
elif a<b:
    c="Pul muvaffaqiyatli yechildi"
else:
    c="Hisobda yetarli mablag' mavjud emas"
print(c)



