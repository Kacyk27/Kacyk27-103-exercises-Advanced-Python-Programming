def calculate():
    x=[]
    for i in range(10,100):
        for j in range(10,100):
            val=i*j
            if str(val)==str(val)[::-1]:
                x.append(val)
    return max(x)


print(calculate())

