from cmath import sqrt
import math
a=int(input())
b=int(input())

for i in range(a,b):
    if math.sqrt(i)==int(math.sqrt(i)):
        print(i,end=" ")