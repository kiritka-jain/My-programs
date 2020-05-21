import numpy
row_1,row_2,column = map(int,input().split())
matrix_1 = []
matrix_2 = []
for _ in range(row_1):
    row_1_column_1,row_1_column_2 = map(int,input().split())
    matrix_1.append(row_1_column_1)
    matrix_1.append(row_1_column_2)
for _ in range(row_2):
    row_2_column_1,row_2_column_2 = map(int,input().split())
    matrix_2.append(row_2_column_1)
    matrix_2.append(row_2_column_2)
matrix_1_array = numpy.array(matrix_1)
matrix_2_array = numpy.array(matrix_2)
matrix = (numpy.concatenate((matrix_1_array,matrix_2_array),axis = 0))
print(numpy.reshape(matrix,(int(row_1+row_2),column)))
