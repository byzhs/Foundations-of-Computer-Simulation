import numpy as np
import matplotlib.pyplot as plt

class CalculateMatrix:
    def __init__(self, size, top, left, bottom, right):
        self.matrix = np.zeros((size * size, size * size))
        self.vector = np.zeros(size * size)
        self.size = size
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right

    def calculate(self):
        index = 0
        for i in range(self.size):
            for j in range(self.size):
                self.calculate_top(i, j, index)
                self.calculate_bottom(i, j, index)
                self.calculate_right(i, j, index)
                self.calculate_left(i, j, index)
                self.matrix[index, index] = -4
                index += 1

    def calculate_top(self, i, j, index):
        if i == self.size - 1:
            self.vector[index] += self.top
        else:
            self.matrix[index, (i + 1) * self.size + j] = 1

    def calculate_bottom(self, i, j, index):
        if i == 0:
            self.vector[index] += self.bottom
        else:
            self.matrix[index, (i - 1) * self.size + j] = 1

    def calculate_left(self, i, j, index):
        if j == self.size - 1:
            self.vector[index] += self.left
        else:
            self.matrix[index, i * self.size + j + 1] = 1

    def calculate_right(self, i, j, index):
        if j == 0:
            self.vector[index] += self.right
        else:
            self.matrix[index, i * self.size + j - 1] = 1

    def get_matrix(self):
        return self.matrix

    def get_vector(self):
        return self.vector

class GaussianElimination:
    @staticmethod
    def solve(A, B):
        n = len(A)
        for p in range(n):
            max_index = np.argmax(np.abs(A[p:, p])) + p
            A[[p, max_index]] = A[[max_index, p]]
            B[p], B[max_index] = B[max_index], B[p]

            if abs(A[p, p]) <= 1e-10:
                raise RuntimeError("The matrix is singular or nearly singular")

            for i in range(p + 1, n):
                alpha = A[i, p] / A[p, p]
                B[i] -= alpha * B[p]
                A[i, p:] -= alpha * A[p, p:]

        x = np.zeros(n)
        for i in range(n - 1, -1, -1):
            x[i] = (B[i] - np.sum(A[i, i + 1:] * x[i + 1:])) / A[i, i]

        return x

if __name__ == "__main__":
    matrix = CalculateMatrix(40, 200, 100, 150, 50)
    matrix.calculate()

    answer = GaussianElimination.solve(matrix.get_matrix(), matrix.get_vector())

    answer_matrix = answer.reshape(matrix.size, matrix.size)

    for i in range(39, -1, -1):
        for j in range(39, -1, -1):
            print(f"{answer[40 * i + j]:.2f}", end=" ")
        print()

    plt.imshow(answer_matrix, cmap='inferno', origin='lower')
    plt.colorbar(label='Values')
    plt.title('Heatmap')
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.show()
