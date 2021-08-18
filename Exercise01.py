def calculate(val):
    x=[]
    for i in range(val):
        if i%5==0 or i%7==0:
            x.append(i)
    return sum(x)
print(calculate(100))