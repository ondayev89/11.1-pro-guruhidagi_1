"""
7. Talaba Baholash Tizimi: Foydalanuvchidan olgan ballini so'rang (0 dan 100 gacha).
Quyidagi mezonlarga ko'ra bahoni print qiling:
● 86 dan 100 gacha: 5 baho
● 70 dan 85 gacha: 4 baho
● 55 dan 69 gacha: 3 baho
● 55 dan past: 2 baho
"""
a=int(input("olgan balling(0 dan 100 gacha)"))
if 85<a<=100:
    a="olgan bahong: 5 baho"
elif 70<a<=85:
    a="olgan bahong: 4 baho"
elif 55<=a<=70:
    a="olgan bahong: 3 baho"
else:
    a="olgan bahong : 2 baho"
print(a)