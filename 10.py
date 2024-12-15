a = int(input("a ni kiriting: "))
b = int(input("b ni kiriting: "))

if a < b:
    for a in range(a, b + 1):
        print(a)
        a += 1
else:
    for b in range(b, a + 1):
        print(b)
        b +=1
