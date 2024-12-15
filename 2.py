# 2. n butun soni berilgan (n > 0). Shu sonning kvadratini quyidagi formula asosida hisoblovchi programma tuzilsin.
# n^2=1+3+5+ ... + (2*n - 1)
# har bir qo'shiluvchidan keyin natijani ekranga chiqarib boring. 

son = int(input("son kiritig: "))
kv = 0
m = 1
i = 0

for i in range(son):
    kv += m
    m += 2
    print(kv)
