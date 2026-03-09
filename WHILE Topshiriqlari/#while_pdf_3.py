""""
3. Do'stlar Ro'yxatini Yaratish:
● Vazifa: Foydalanuvchidan do'stlarining ismlarini kiritishni so'rang.
Foydalanuvchi "stop" deb yozmaguncha, yangi ismlar qo'shilaveradi. Oxirida
barcha do'stlarining ismlari ro'yxatini chiqaring.
● Ko'rsatma: While sikli va list metodlaridan foydalanib, ro'yxatni shakllantiring."""
drug_list=[]
ishora=True
while ishora:
    print("(dasturdan chiqish stop so'zini kiriting)")
    a = input("Do'stingizni isminigizni kiriting: ")
    drug_list.append(a)
    if a=="stop":
        ishora=False
#===================================================
print("sizning do'stlaringiz ro'yxati quyidagilar")
for b in drug_list:
    print(b,end=",")
