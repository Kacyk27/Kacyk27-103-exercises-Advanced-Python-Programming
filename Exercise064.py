def reduce_with_start(function,iterable,start):

    if len(iterable) == 0:
        return start
    result = start + iterable[0]
    for x in iterable[1:]:
        result = function(result,x)
    return result

print(reduce_with_start(lambda x,y: x+y, [2,5,1],100))