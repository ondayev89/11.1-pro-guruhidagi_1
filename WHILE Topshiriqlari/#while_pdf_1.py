"""
1. Svetafor: Foydalanuvchidan inputda svetavor qaysi rangda deb so’rang. qizil,
sariq yoki yashil deb yozmagunicha, bu xato rang deb qayta so’rayvering. Agar shu
ranglardan birini tanlasa “rahmat, to’g’ri keladi” degan print chiqazing.
"""
#svetafor = input("svetavor qaysi rangda")
rangi=["qizil","sariq", "yashil"]
#svetafor = input("svetavor qaysi rangda").lower().strip()
while True:
    # Foydalanuvchidan rangni so'rash
    # .lower() va .strip() kiritilgan matnni tozalash uchun ishlatiladi
    # agar input ichkarida berilmasa sikl cheksiz davom etadi
   svetafor = input("svetavor qaysi rangda").lower().strip()
   if svetafor in rangi:
       print("rahmat, to’g’ri keladi")
       break
   else:
       # Agar rang noto'g'ri bo'lsa, xabar chiqadi va sikl qaytadan so'raydi
       #input ichkarida bo'lgan uchun sikl cheksiz davom etadi
        print("Bu xato rang. Iltimos, faqat 'qizil', 'sariq' yoki 'yashil' deb yozing.")
