""""
2. Tasodifiy Sonni Topish O'yini: Kompyuter 1 dan 10 gacha bo'lgan tasodifiy son
o'ylaydi. Foydalanuvchidan ushbu sonni topishni so'rang. Foydalanuvchi to'g'ri sonni
topguncha davom etadi. Har bir noto'g'ri urinishdan so'ng, "Noto'g'ri, qayta urinib
ko'ring" deb chiqaring. To'g'ri topilganda, "Tabriklaymiz, siz topdingiz!" deb chiqaring.
Ko'rsatma: random. dan foydalanib tasodifiy son yarating va while sikli yordamida
foydalanuvchi kiritmalarini tekshiring.
import random
tasodifiy_son = random.randint(10)
#davom ettiring         """
import random
tasodifiy_son = random.randint(1,10)

while True:
    kiritilgan_son = int(input("son kiriting: "))
    if kiritilgan_son==tasodifiy_son:
        print("Tabriklaymiz, siz topdingiz!")
        break
    print("Noto'g'ri, qayta urinib ko'ring")


