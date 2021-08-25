from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)

def decompress(number):
    result = [tuple(item) for item in number.split("_")]
    result = [i * int(j) for i,j in result]
    return int("".join(result))

print(decompress('12_12'))