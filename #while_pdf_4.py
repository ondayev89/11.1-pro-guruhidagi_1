"""
4. Valyuta Ayirboshlash Kalkulyatori: Foydalanuvchiga valyuta ayirboshlash
imkoniyatini bering. U so'mni dollarga almashtirishi mumkin. Valyuta kurslarini
oldindan belgilang (masalan, 1 USD = 12,600 so'm). Foydalanuvchi summani
kiritadi, dastur esa hisob-kitobni chiqaradi. Foydalanuvchi "exit" deb yozmaguncha
dastur davom etadi.exit deb yozsa dastur to’xtaydi.
"""
ishora=True
while ishora:
    print("(dasturdan chiqish 'exit' so'zini kiriting)")
    a = int(input("summani so'mda kiriting: "))
    dollar=a/12600
    print(f"{a} so'm = {dollar:.2f} $")
    javob=input("davom ettirmoqchi bo'lsangiz 'ha', dasturdan chiqmoqchi bo'lsangzi 'exit' deb yozing ")
    if javob=="exit":
        ishora=False
