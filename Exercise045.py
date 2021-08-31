def lev(a,b):
    x=len(a)
    y=len(b)
    if a==b:
        return 0

    if len(a) == 0:
        return y

    if len(b) == 0:
        return x

    if a[0] == b[0]:
        return lev(a[1:], b[1:])

    result = 1 + min(lev(a[1:],b), lev(a,b[1:]),lev(a[1:],b[1:]))
    return result
