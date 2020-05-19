import numpy
n,m = map(int,input().split()) #n*m dimension of array
aray = []
for index in range(n):
    a,b = map(int,input().split())
    aray.append(a)
    aray.append(b)
ary = numpy.array(aray)
reshape_array = numpy.reshape(ary,(n,m))
min_along_axix = (numpy.min(reshape_array,axis=1))
print(numpy.max(min_along_axix))


