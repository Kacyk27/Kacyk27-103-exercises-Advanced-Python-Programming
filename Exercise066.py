class NaturalList(list):

    def append(self,x):
        if isinstance(x,int):
            if x > 0:
                list.append(self,x)
            else:
                raise ValueError("The value must be a natural number.")
        else:
            raise TypeError("The value must be an integer.")