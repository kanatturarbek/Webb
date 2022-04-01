l=input().split()

a=int(l[0])
b=int(l[1]) 
c=int(l[2])
d=int(l[3])  
def min4(a, b, c, d):
    return min(min(min(a, b), c), d)
 
 
print(min4(a, b, c, d))