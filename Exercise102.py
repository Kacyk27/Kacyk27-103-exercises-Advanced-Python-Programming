class Queue:
    """The simplest queue."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError('The queue is empty.')
        return self._data.pop(0)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        return self._data[0]

q1=Queue()
q1.enqueue("529")
q1.enqueue("623")
q1.dequeue()
q1.enqueue("532")
q1.first()
q1.enqueue("304")
q1.dequeue()
print(len(q1))