def calculate():
    x = []
    maxval = 1000000
    a = 0
    b = 1
    while b < maxval:
        a,b=b,a+b
        if b % 2 == 0:
            x.append(b)
    print(sum(x))
calculate()