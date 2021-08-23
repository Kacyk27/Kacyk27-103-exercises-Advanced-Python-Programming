def calculate(val):
    x=[]
    i=2
    while i * i<=val:
        if val % i !=0:
            i+=1
        else:
            val=val/i
            x.append(i)
    if val>1:
        x.append(val)
    return max(x)