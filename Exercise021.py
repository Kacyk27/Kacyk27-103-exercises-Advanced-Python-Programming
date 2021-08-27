def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1
    return distance

def hamming_weight(u):
    v= str(len(u)*"0")
    return hamming_distance(u,v)

