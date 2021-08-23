def is_prime(val):
    x=[]
    if not isinstance(val,int):
        raise TypeError("Must be int type and greater than 0.")
    else:
        for i in range(2,val):
            if val % i == 0:
                x.append(i)
    if len(x) != 0:
        return False
    elif val < 2:
        return False
    else:
        return True

print(is_prime(1))