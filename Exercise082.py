class Matrix:

    def __init__(self, array):

        if not isinstance(array, list):
            raise TypeError('To create a matrix you need to pass a nested list of values.')

        if len(array) != 0:
            if not all(isinstance(row, list) for row in array):
                raise TypeError('Each element of the array (nested list) must be a list.')

            if not all(len(row) for row in array):
                raise TypeError('Columns must contain at least one item.')

            column_length = len(array[0])

            if not all(len(row) == column_length for row in array):
                raise TypeError('All columns must be the same length.')

            if not all(type(number) in (int, float) for row in array for number in row):
                raise TypeError('The values must be of type int or float.')

            self.array = array
        else:
            self.array = []

    def __repr__(self):
        return str(self.array)

    @property
    def n_rows(self):
        return len(self.array)

    @property
    def n_cols(self):
        if len(self.array) == 0:
            return 0
        return len(self.array[0])

    @property
    def size(self):
        return self.n_rows, self.n_cols

    @property
    def is_square_matrix(self):
        return self.size[0] == self.size[1]

    def zero(self):
        array = [[0 for _ in range(self.n_cols)] for _ in range(self.n_rows)]
        return Matrix(array)

    def identity(self):
        if not self.is_square_matrix:
            return None
        array = [[1 if row == col else 0 for row in range(self.n_rows)] for col in range(self.n_cols)]
        return Matrix(array)

    def add_row(self, row, index=None):
        if not isinstance(row, list):
            raise TypeError('The matrix row must be a list.')

        for number in row:
            if not type(number) in (int, float):
                raise TypeError('Row values must be int or float.')

        if len(row) != self.n_cols:
            raise ValueError('The row must be the same length as the number of columns in the matrix.')

        if index is None:
            self.array.append(row)
        else:
            self.array = self.array[0:index] + [row] + self.array[index:]

    def add_column(self,column,index=None):
        if not isinstance(column, list):
            raise TypeError('The matrix row must be a list.')

        for number in column:
            if not type(number) in (int, float):
                raise TypeError('Row values must be int or float.')

        if len(column) != self.n_rows:
            raise ValueError('The row must be the same length as the number of columns in the matrix.')

        if index is None:
            x=0
            for i in self.array:
                i.append(column[x])
                x+=1
        else:
            x = 0
            for i in self.array:
                i.insert(index,column[x])
                x += 1