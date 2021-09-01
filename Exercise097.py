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


# Very hard
def is_valid_html(code):


    stack=Stack()
    first_char = code.find("<")
    while first_char != -1:
        next_char = code.find(">",first_char + 1)
        if next_char == -1:
            return False
        tag = code[first_char+1:next_char]
        if not tag.startswith("/"):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if tag[1:] != stack.pop():
                return False
        first_char = code.find("<",next_char + 1)
    return stack.is_empty()


with open("template1.html", "r") as file:
    data1 = file.read()

with open("template2.html", "r") as file:
    data2 = file.read()

print(is_valid_html(data1))
print(is_valid_html(data2))