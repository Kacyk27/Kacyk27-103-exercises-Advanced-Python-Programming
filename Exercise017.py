class Matrix:

    def __init__(self,string):
        self.matrix=[[int(i) for i in line.split()] for line in string.splitlines()]

    def __repr__(self):
        return "\n".join([(" ".join([str(i) for i in row])) for row in self.matrix])

m=Matrix('3 4\n5 6')
print(m.matrix)
