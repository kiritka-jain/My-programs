import numpy

def arrays(arr):
    # complete this function
    # use numpy.array\
    ary = numpy.array(arr[::-1],float)
    return ary



arr = input().strip().split(' ')
result = arrays(arr)
print(result)
