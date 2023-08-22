import random

class Matrix:
    """класс для работы с матрицами"""

    def __init__(self, row=None, column=None, ready_matrix=None):
        self.row = row
        self.column = column 
        self.ready_matrix = ready_matrix

    def create_matrix(self):
        "метод для создания матрицы"

        matrix = [random.sample(range(0, 10), self.column) for _ in range(self.row)]
        self.ready_matrix = matrix
        return self

    def print_matrix(self):
        """метод для вывода матрицы на печать"""

        for row in self.ready_matrix:
            print(row)

    def __eq__(self, other):
        """метод для сравнения матриц"""

        return self.ready_matrix == other.ready_matrix

    def add(self, other):
        """метод для сложения матриц"""
        if self.row == other.row and self.column == other.column:
            result = []
            for i in range(self.row):
                row = []
                for j in range(self.column):
                    row.append(self.ready_matrix[i][j] + other.ready_matrix[i][j])
                result.append(row)
                self.add_matrix = result
            return self
        else:
            print("Матрицы разных размеров!")
            return None

    def mul(self, other):
        """метод для умножения матриц"""
        if self.column == other.row:
            result = []
            for i in range(self.row):
                row = []
                for j in range(other.column):
                    elem = 0
                    for k in range(self.column):
                        elem += self.ready_matrix[i][k] * other.ready_matrix[k][j]
                    row.append(elem)
                result.append(row)
                self.mul_matrix = result
            return self
        else:
            print("Умножение матриц невозможно!")
            return None


one_mat = Matrix(3, 3).create_matrix()
one_mat.print_matrix()

two_mat = Matrix(3, 3).create_matrix()
two_mat.print_matrix()

print(one_mat.add(two_mat))

three_mat = Matrix(2, 2).create_matrix()
three_mat.print_matrix()

print(one_mat.mul(three_mat))
