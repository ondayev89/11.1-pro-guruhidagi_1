"""
4. Taxmin qilish o'yinini simulyatsiya qiladigan dastur yarating.
Dastur 1 dan 100 gacha bo'lgan tasodifiy sonni yaratishi va
foydalanuvchidan raqamni taxmin qilishni so'rashi kerak.
Agar foydalanuvchi taxmini haqiqiy raqamdan yuqori bo'lsa, dastur "Juda baland!" va
foydalanuvchidan yana taxmin qilishni so'rang. Xuddi shunday, agar foydalanuvchining
taxmini haqiqiy raqamdan past bo'lsa, dastur "Juda past!" va foydalanuvchidan yana taxmin
qilishni so'rang. Dastur foydalanuvchidan to'g'ri raqamni topmaguncha taxmin qilishni so'rashi kerak.
"""
import random
a=random.randint(1,100)

while True:
    kirit = int(input("o'ylagan sonimni top"))
    if kirit==a:
        print("BARAKALLA, topdingiz")
        break
    elif kirit<a:
        print("kattaroq sonni taxmin qil")
    elif kirit>a:
        print("kichikroq sonni taxmin qil")

breakpoint()
