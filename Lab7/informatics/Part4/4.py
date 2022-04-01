n=int(input())
count=0
l=input().split()
for i in range(1,len(l)):
    if int(l[i])>int(l[i-1]):
         count+=1
print(count)