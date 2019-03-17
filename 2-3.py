#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)

tab = []

for x in range(1,50):
    for y in range(1,50):
        if x%y == 0:
            if x%2 == 0 and y%2==0: 
                tup = (x,y)
                tab.append(tup)

print(tab)
