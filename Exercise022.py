from collections import ChainMap

def score(word):
    c={" ":0,
       "EAIONRTLSU":1,
       "DG":2,
       "BCMP":3,
       "FHVWY":4,
       "K":5,
       "JX":8,
       "QZ":10}

    scores=ChainMap(*[dict.fromkeys(letter,score) for letter,score in c.items()])
    return sum([scores[letter.upper()] for letter in word])
