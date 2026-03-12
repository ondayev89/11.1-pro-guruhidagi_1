"""#While orqali 1 dan 100 gacha bo'lgan toq solar yig'indisini topuvchi dastur tuzing
i=1
s=0
while i<100:
    s+=i
    i=i+2
print(s)"""
#While orrqali Ro'yxatdagi 2-eng katta sonni topuvchi dastur yozing
a=[]
while True:
    son_kir=int(input("son kirit"))
    a.append(son_kir)
    takrorlash=input("yana son kiritasanmi (ha/yo'q)")
    if takrorlash!="ha":
        break
print(max(a))