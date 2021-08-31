class CaesarCipher:

    def __init__(self,alphabet,key):
        self.alphabet=alphabet
        self.key=key

    @property
    def cipher(self):
        result = ""
        for i in self.alphabet:
            new = (self.alphabet.index(i) + self.key) % len(self.alphabet)
            result += self.alphabet[new]
        return result