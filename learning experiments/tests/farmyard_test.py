def farmyard(heads, legs):
    for chickens in range(0, heads + 1):
        pigs = heads - chickens
        if (4 * pigs) + (2 * chickens) == legs:
            print(chickens, pigs)
        
x = int(input("number of heads:"))
y = int(input('number of legs:'))
farmyard(x, y)
