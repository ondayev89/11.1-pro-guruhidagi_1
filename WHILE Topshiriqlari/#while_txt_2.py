"""2. While dan foydalanib sondagi raqamlar yig'indisini topadigan dastur tuzing.
input: 555   output: 15
input: 8125   output: 16
"""

son_kirit=int(input("son kirit: "))
a_list=list(str(son_kirit))
i=0
s=0
while i<len(a_list):
    s=s+int(a_list[i])
    i=i+1
print(s)

