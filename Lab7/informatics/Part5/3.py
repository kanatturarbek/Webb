import math
l=input().split()

a=float(l[0])
b=int(l[1]) 

def xor(a, b):
    if a!=b:
        return 1
    else:
        return 0
 
 
print(xor(a,b))