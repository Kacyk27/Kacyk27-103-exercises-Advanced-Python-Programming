def is_palindrome(n):
    if str(n)==str(n)[::-1]:
        x=bin(n)[2::]
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False

    else:
        return False

print(is_palindrome(99))
print(is_palindrome(100))