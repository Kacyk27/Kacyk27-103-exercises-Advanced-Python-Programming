import string

def generate_cipher(alphabet,key=2):

    result=""
    for i in alphabet:
        new = (alphabet.index(i) + key) % len(alphabet)
        result += alphabet[new]
    return result


def encrypt(alphabet,message,key):


    cipher=generate_cipher(alphabet,key)
    result=""
    for i in message:
        if i not in alphabet:
            result += i
        else:
            result += cipher[alphabet.index(i)]
    return result