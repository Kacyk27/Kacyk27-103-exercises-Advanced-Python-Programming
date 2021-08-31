def reduce(function,iterable):

    if len(iterable) == 0:
        return None
    result=iterable[0]
    for x in iterable[1:]:
        result = function(result,x)
    return result

print(reduce(lambda x,y: x+y, [1,2,3,4]))