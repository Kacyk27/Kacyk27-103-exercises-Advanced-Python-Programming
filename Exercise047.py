import string

def generate_cipher(alphabet,key=2):

    result=""
    for i in alphabet:
        new = (alphabet.index(i) + key) % len(alphabet)
        result += alphabet[new]
    return result
