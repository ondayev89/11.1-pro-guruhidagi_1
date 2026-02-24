"""
3. Ob-havo Ma'lumotlarini Tahlil Qilish:
○ Bir hafta davomida kundalik haroratlar ro'yxati berilgan (masalan, [20,
22, 19, 24, 25, 23, 21]).
○ for sikli yordamida o'rtacha haroratni hisoblang va har bir kun uchun
agar harorat 22 dan yuqori bo'lsa, "Iliq kun", aks holda "Salqin
kun" deb chiqaring.
"""
s=0
sum=0
ob_havo=[20,22, 19, 24, 25, 23, 21,28]
for harorat in ob_havo:
    s+=1
    sum=sum+harorat
    if harorat>22:
        print(f" {harorat} - Illiq kun")
    else:
        print(f" {harorat} - Salqin")
print(f"o'rtacha harorat {sum/s} gradus")
