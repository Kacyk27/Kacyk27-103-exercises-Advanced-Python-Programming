import itertools

def compress(thing):
    comp_list=[]
    key_func = lambda x: x[0]
    iterator=itertools.groupby(str(thing),key_func)
    for key,group in iterator:
        key_and_group = (key, len(list(group)))
        comp_list.append(key_and_group)


    return comp_list
print(compress(1112))