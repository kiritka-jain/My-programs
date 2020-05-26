import numpy
row,column = map(int,input().split())
matrix_array = numpy.array([input().strip().split() for _ in range(row)], int)
matrix_sum =numpy.sum(matrix_array,axis=0)
print(numpy.prod(matrix_sum))
