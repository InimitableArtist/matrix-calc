import numpy as np
from numpy.linalg import matrix_rank

class MatrixCalculator:
    
    def __init__(self, array):
        self.array = array

    def turn_blanks_to_zeroes(self, array):
        for i in range(len(array)):
            array[i] = '0' if array[i] == '' else array[i]

        return array

    def dimensions_to_normal_form(self):
        dimensions = list(self.array.keys())[len(list(self.array.keys())) - 2]
        return list(map(int, dimensions))
    
    def numbers_to_normal_form(self):
        content_clean = list(self.array.values())[1:len(self.array.values()) - 1]
        array_numbers = self.turn_blanks_to_zeroes(content_clean)
        array_numbers = list(map(int, content_clean))

        return array_numbers

    def Determinant(self, mtrix, dim):
        np_array = np.array(mtrix).reshape(dim[0] + 1, dim[1] + 1)
        result = round(np.linalg.det(np_array))

        return result

    def Rank(self, mtrix, dim):
        mtrix = np.array(mtrix)
        mtrix = mtrix.reshape(dim[0] + 1, dim[1] + 1)
        rank = matrix_rank(mtrix)

        return rank
    
