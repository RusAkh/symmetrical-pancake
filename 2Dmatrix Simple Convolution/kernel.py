import numpy as np


class Kernel3x3:
    def __init__(self):
        self.width = 3
        self.height = 3

    # def get_matrix(self):
    #     matrix = [[i for i in range(self.width)] for _ in range(self.height)]
    #     return np.array(matrix)

    def fill_matrix(self, mode='VERTICAL'):
        matrix = [[i for i in range(self.width)] for _ in range(self.height)]
        counter = 1
        if mode == 'VERTICAL':
            for i in range(self.height):
                counter = 1
                for j in range(self.width):
                    matrix[i][j] = counter
                    counter -= 1
        elif mode == 'HORIZONTAL':
            for i in range(self.height):
                for j in range(self.width):
                    matrix[i][j] = counter
                counter -= 1
        return np.array(matrix)


