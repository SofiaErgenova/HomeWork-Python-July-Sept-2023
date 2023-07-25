"""
Напишите функцию для транспонирования матрицы
"""

def trans_matrix(matrix):
    
    rows = len(matrix)
    if matrix:
        cols = len(matrix[0])
    else:
        cols = 0

    trans = []
    for i in range(cols):
        new_row = [0 for i in range(rows)]
        trans.append(new_row)

    for i in range(rows):
        for j in range(cols):
            trans[j][i] = matrix[i][j]

    return trans


matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = trans_matrix(matrix)
print(transposed_matrix)


