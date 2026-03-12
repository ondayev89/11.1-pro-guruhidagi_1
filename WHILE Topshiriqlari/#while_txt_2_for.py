# 4 xil usulda
son_kirit=int(input("son kirit: "))
a_list=list(str(son_kirit))
x=(len(a_list))
i=0
s=0
#1range kerak emas
for i in a_list:
    s = s + int(i)
print(s)
#2
""" for yordamida range kerak
for i in range(x):
    s=s+int(a_list[i])
print(son_kirit," sonining raqamlar yig'indisi ",s)
"""
#==========================================
#3
"""map yordamida
s = s+sum(map(int, a_list))
print(s)
"""
#4 for qisqa shaklida
#s =s+ sum(int(i) for i in a_list)
#print(s)