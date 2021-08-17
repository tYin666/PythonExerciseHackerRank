import numpy

n,m=map(int, input().split())

lis=[]

for i in range(n):
    
    k= [int(i) for i in input().split()]
    lis.append(k)

    
my_array = numpy.array(lis)
#my_array = numpy.array([[2, 2],[1, 2],[3, 4]])
lis1= numpy.sum(my_array, axis = 0)

print(lis1)
3