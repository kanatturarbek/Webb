n=int(input())
count=0
l=input().split()
for i in range(0,len(l)):
    if int(l[i])>0:
         count+=1
print(count)