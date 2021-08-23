def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]

def calculate():
    x=[]
    for i in range(1,10):
        for j in range(0,10):
            for k in range(0,10):
                val=int(f"{i}{j}{k}")
                if str(val) == str(val)[::-1]:
                    y = bin(val)[2::]
                    if str(y) == str(y)[::-1]:
                        x.append(val)
    return x


print(calculate())
