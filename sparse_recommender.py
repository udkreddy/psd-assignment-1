class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = {}

    def set(self, row, col, value):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Invalid row or column index")
        
        if value != 0:
            self.data[(row, col)] = value
        elif (row, col) in self.data:
            del self.data[(row, col)]

    def get(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise ValueError("Invalid row or column index")
        
        return self.data.get((row, col), 0)

    def recommend(self, vector):
        if len(vector) != self.cols:
            raise ValueError("Vector size does not match the number of columns in the matrix")
        
        result = [0] * self.rows
        for (row, col), value in self.data.items():
            result[row] += value * vector[col]
        
        return result

    def add_movie(self, matrix):
        if matrix.rows != self.rows or matrix.cols != self.cols:
            raise ValueError("Matrix dimensions do not match")

        result = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.data.items():
            result.set(row, col, value + matrix.get(row, col))
        
        return result

    def to_dense(self):
        dense_matrix = [[0] * self.cols for _ in range(self.rows)]
        for (row, col), value in self.data.items():
            dense_matrix[row][col] = value
        
        return dense_matrix
