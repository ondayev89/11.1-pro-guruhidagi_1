"""
2. Internet-do'kon Chegirmasi: Foydalanuvchidan xarid summasini so'rang. Agar summa
50,000 so'mdan kam bo'lsa, chegirma yo'q. Agar 50,000 dan 100,000 so'mgacha bo'lsa,
5% chegirma. Agar 100,000 so'mdan yuqori bo'lsa, 10% chegirma hisoblang va yakuniy
narxni chiqaring.
"""
xarid_summasi=int(input("xarid summasi kiriting: "))
if xarid_summasi<=50000:
    print(f"chegirma yo'q, narxi {xarid_summasi} so'm")
elif 50000<xarid_summasi<=100000:
    print(f"5% chegirma bilan, narxi {xarid_summasi*0.95} so'm")
else:
    print(f"10% chegirma bilan, narxi {xarid_summasi * 0.9} so'm")
