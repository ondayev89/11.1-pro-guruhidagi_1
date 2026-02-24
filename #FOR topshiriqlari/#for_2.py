"""2. Parol Kuchini Tekshirish:
○ Foydalanuvchilarning parollar ro'yxati berilgan (masalan,
["password123", "Qwerty!", "admin", "StrongPass1!"]).
○ for sikli va shart operatorlari yordamida har bir parolni tekshiring:
■ Agar uzunligi 8 dan kam bo'lsa, "Juda qisqa"
■ Agar raqam yoki maxsus belgilar bo'lmasa, "Kuchsiz parol"
■ Aks holda, "Kuchli parol"
"""
password =["password123", "Qwerty!", "admin", "StrongPass1!"]
for sikli in password:
    sikli_1=len(sikli)
    if sikli_1<8:
        print(f" {sikli} - parol juda qisqa")
    elif sikli.isalnum():
        print(f" {sikli} - kuchsiz parol ")
    else:
        print(f" {sikli} - kuchli parol ")