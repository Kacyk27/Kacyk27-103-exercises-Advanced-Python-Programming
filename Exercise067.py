class IntDict(dict):

    def __setitem__(self, key, value):
        if isinstance(value,int):
            dict.__setitem__(self,key,value)
        else:
            raise TypeError("The value must be an integer.")
