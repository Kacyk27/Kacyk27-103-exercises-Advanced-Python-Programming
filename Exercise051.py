class CaesarCipher:

    def __init__(self, alphabet, key):
        self.alphabet = alphabet
        self.key = key

    @property
    def cipher(self):
        result = ''
        for letter in self.alphabet:
            new_idx = (self.alphabet.index(letter) + self.key) % len(self.alphabet)
            result += self.alphabet[new_idx]
        return result

    def encrypt(self,message):
        result = ""
        for i in message:
            if i not in self.alphabet:
                result += i
            else:
                result += self.cipher[self.alphabet.index(i)]
        return result


    def decrypt(self,message):

        result=""
        for i in message:
            if i not in self.alphabet:
                result += i
            else:
                result += self.alphabet[self.cipher.index(i)]
        return result