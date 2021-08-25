import itertools

def compress(thing):
    comp_list=[]
    key_func = lambda x: x[0]
    iterator=itertools.groupby(str(thing),key_func)
    for key,group in iterator:
        key_and_group = f"{key}{len(list(group))}"
        comp_list.append(key_and_group)

    result="_".join(comp_list)
    return result
print(compress(11122000))