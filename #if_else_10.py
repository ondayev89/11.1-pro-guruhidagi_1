"""
10. Mobil Tarif Tanlash: Foydalanuvchidan oyiga qancha internet trafikidan foydalanishini
so'rang (GB da). Agar trafik 1 GB dan kam bo'lsa, "Sizga 'Mini' tarifi mos keladi" deb
chiqaring. Agar 1 GB dan 5 GB gacha bo'lsa, "Sizga 'Standard' tarifi mos keladi". Agar 5
GB dan yuqori bo'lsa, "Sizga 'Unlimited' tarifi mos keladi" deb chiqaring.
"""
trafik_user_miqdori=float(input("oyiga qancha internet trafikidan foydalanasiz 'GB ayting' "))
if trafik_user_miqdori<1:
    chiqar="Sizga 'Mini' tarifi mos keladi"
elif 1<=trafik_user_miqdori<=5:
    chiqar="Sizga 'Standard' tarifi mos keladi"
else:
    chiqar="Sizga 'Unlimited' tarifi mos keladi"
print(chiqar)