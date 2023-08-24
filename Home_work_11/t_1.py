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
        return Matrix(self.row, self.column, matrix)

    def print_matrix(self):
        """метод для вывода матрицы на печать"""
        print(self.ready_matrix)
          

    def __eq__(self, other):
        """метод для сравнения матриц"""

        return self.ready_matrix == other.ready_matrix


    def __add__(self, other):
        """метод для сложения матриц"""
        if self.row == other.row and self.column == other.column:
            result = []
            for i in range(self.row):
                row = []
                for j in range(self.column):
                    row.append(self.ready_matrix[i][j] + other.ready_matrix[i][j])
                result.append(row)
                
            return Matrix(self.row, self.column,result)
        else:
            print("Матрицы разных размеров!")
            

    def __mul__(self, other):
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
    
            return Matrix(self.row, self.column,result)
        else:
            print("Умножение матриц невозможно!")
        


one_mat = Matrix(3, 3).create_matrix()
one_mat.print_matrix()

two_mat = Matrix(3, 3).create_matrix()
two_mat.print_matrix()

three_mat = one_mat + two_mat
three_mat.print_matrix()

mul_mat = one_mat * three_mat
mul_mat.print_matrix()