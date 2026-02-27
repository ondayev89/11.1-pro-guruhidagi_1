"""
6. Mobil Ilova Bildirishnomalari: Bildirishnomalar sarlavhalari ro'yxati berilgan
xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]).
for sikli yordamida agar sarlavha "Batareya past" bo'lsa,
"Telefoningizni quvvatlang" deb print chiqaring.
"""
xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
for note in xabarlar:
    if note=="Batareya past":
        print("Telefoningizni quvvatlang")