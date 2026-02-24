""""
1. Elektron Pochta Manzillarini Tekshirish:
Email manzillar ro'yxati berilgan:
pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
for sikli va string metodlari yordamida har bir email manzilida "@" belgisi
bor-yo'qligini tekshiring: Agar bo'lmasa, "Noto'g'ri email: email_manzi" deb
chiqaring.
"""
pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com","@outlook.com"]
for sikli in pochtalar:
    if sikli.find("@")==-1:
        print("Noto'g'ri email: email_manzil", sikli)
