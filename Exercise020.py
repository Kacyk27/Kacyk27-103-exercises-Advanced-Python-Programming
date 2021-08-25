def hamming_distance(x,y):

    a = 0
    if len(x) != len(y):
        raise ValueError("Both vectors must be the same length.")
    for i in range(len(x)):
        if x[i] != y[1]:
            a+=1
    return a

print(hamming_distance('0101','1101'))