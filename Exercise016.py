class Matrix:

    def __init__(self,string):
        self.matrix=[[int(i) for i in line.split()] for line in string.splitlines()]

m=Matrix('3 4\n5 6')
print(m.matrix)
