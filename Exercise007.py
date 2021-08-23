def greatest_common_divisor(x,y):
    divisors=[]
    for i in range(1,min(x+1,y+1)):
        if x % i == 0 and y % i == 0:
            divisors.append(i)
    return max(divisors)

print(greatest_common_divisor(64,128))