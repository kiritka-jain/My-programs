import numpy
row,column = map(int,input().split())
matrix_array_1 = numpy.array([input().strip().split() for _ in range(row)], int)
matrix_array = numpy.reshape(matrix_array_1,(row,column))
print(numpy.transpose(matrix_array))
print(matrix_array.flatten())
