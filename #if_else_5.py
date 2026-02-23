""""
5. Restoran Menyusi: Foydalanuvchiga menyudan taom tanlash imkoniyatini bering: 1 -
"Osh", 2 - "Mastava", 3 - "Shashlik". Tanlovga qarab taomning narxi va tayyorlanish vaqtini
chiqaring.
"""
print("--- Restoran Menyusi ---")
print("1 - Osh")
print("2 - Mastava")
print("3 - Shashlik")
kiritish=input("Iltimos, taom raqamini tanlang (1, 2 yoki 3): ")
# # Kiritilgan ma'lumot ro'yxatga (list) aylanadi
tanlov=kiritish.split()
if '1' in tanlov:
    a="osh narxi: 30 000 so'm, tayyorlanish vaqti: 10 min"
elif '2' in tanlov:
    a="mastava narxi: 20 000 so'm, tayyorlanish vaqti: 5 min"
elif '3' in tanlov:
    a="shashlik narxi: 2 5000 so'm, tayyorlanish vaqti: 30 min"
else:
    a="bizda bunday taom yo'q"
print("\n", a)