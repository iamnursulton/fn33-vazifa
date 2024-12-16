
n = int(input("sonni kiriting: "))
too=0
if n <=1:
    print(f"{n}  tub emas")
else:
    
    is_prime = True 
    for i in range(2, int(n**(1/2)) + 1): 
            is_prime = False
            break
    
    
    if is_prime:
        print(f"{n}sonni  tub")
    else:
        print(f"{n}soni tub emas")