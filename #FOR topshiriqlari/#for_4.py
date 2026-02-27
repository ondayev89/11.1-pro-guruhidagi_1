"""
4. Restoran Buyurtmalari:
● Mavjud taomlar ro'yxati berilgan (masalan, ["Osh", "Shashlik", "Manti",
“Lag’mon” ]).
● Foydalanuvchidan buyurtma kiritishni so'rang.
● for sikli yordamida foydalanuvchi kiritgan buyurtma mavjud taomlarga mos
keladimi-yo'qligini tekshiring:
○ Agar mos kelsa, "Buyurtmangiz qabul qilindi" deb chiqaring.
○ Aks holda, "Kechirasiz, bunday taom yo'q" deb chiqaring
"""
from tabnanny import check

taom_menyu=["Osh", "Shashlik", "Manti","Lag’mon","chuchvara" ]
#===========================================================
buyurtma=input("Buyurtma bering")
# Standart xabar (agar taom topilmasa shu xabar qoladi)
xabar="kechirasiz bunday taom yo'q"
for sikli in taom_menyu:
    if buyurtma.lower()==sikli.lower():
        xabar="Buyurtmangiz qabul qilindi"
        break   # Taom topilgach, qolganlarini tekshirish shart emas
print(xabar)
