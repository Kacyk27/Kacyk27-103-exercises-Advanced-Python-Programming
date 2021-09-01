class EmptyStackError(Exception):
    pass


class Stack:
    """The simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data[-1]

def is_valid_expression(expression):
    left="({["
    right=")}]"

    stack=Stack()
    for i in expression:
        if i in left:
            stack.push(i)
        elif i in right:
            if stack.is_empty():
                return False
            if right.index(i) != left.index(stack.pop()):
                return False
    return stack.is_empty()