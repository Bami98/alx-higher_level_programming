def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrixx = [ [el*el  for el in row] for row in matrix]
    return new_matrixx
    