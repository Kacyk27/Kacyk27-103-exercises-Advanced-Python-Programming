def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def calculate():
    counter=0
    n=2
    while True:
        if is_prime(n):
            counter+=1
            if counter == 100:
                return  n
        n+=1
print(calculate())