"""5. Anketa Tahlili:
● Foydalanuvchilarning yoshlari ro'yxati berilgan (masalan, [16, 21, 17,30, 25]).
● for sikli yordamida har bir foydalanuvchining yoshini tekshiring:
○ Agar yosh 18 dan kichik bo'lsa, "Yosh chegarasiga yetmagan"deb chiqaring.
○ Aks holda, "Xush kelibsiz" deb chiqaring."""
user_list_1=[16, 21, 17,30, 25]
#==============================================================
for age in user_list_1:
    #=======================>>>>>
    if age<18:
        print(f"{age} yosh - Yosh chegarasiga yetmagan hisoblanadi")
    else:
        print(f" {age} yoshli inson -Xush kelibsiz")
    #=======================<<<<<<<<<<<<<<<<<.

