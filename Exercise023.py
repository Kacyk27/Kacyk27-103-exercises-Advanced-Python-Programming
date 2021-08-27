def get_slices(sequence,length):
    if length<0:
        raise ValueError("The length cannot be less than 1.")
    elif length>len(sequence):
        raise ValueError("The length cannot be greater than sequence.")
    x=[]
    for i in range(len(sequence) - length+1):
            x.append(sequence[i:i+length])
    return x

print(get_slices("esmartdata",5))