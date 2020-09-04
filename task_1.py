import numpy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join([str(i) for i in row]) for row in self.matrix)

    def __add__(self, other):
        return Matrix((numpy.array(self.matrix) + numpy.array(other.matrix)).tolist())


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print("Матрица m_1:", m_1, sep="\n")
print("Матрица m_2:", m_2, sep="\n")
print("Сумма матриц m_1 + m_2:", m_1 + m_2, sep="\n")
