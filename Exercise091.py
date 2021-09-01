class EmptyStackSError(Exception):
    pass


class Stack:

    def __init__(self):
        self._data=[]

    def __len__(self):
        return len(self._data)

    def push(self,item):
        self._data.append(item)

    def pop(self):
        if len(self._data) !=0:
            return self._data.pop()
        else:
            raise EmptyStackSError("The stack is empty.")
