class IntList(list):

    def append(self,x):
        if isinstance(x,int):
            list.append(self,x)
        else:
            raise TypeError("The value must be an integer.")