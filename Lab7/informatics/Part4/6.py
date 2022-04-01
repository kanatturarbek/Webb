n=int(input())
check=0
l=input().split()
for i in range(1,len(l)-1):
    if (int(l[i])>int(l[i+1]) and int(l[i]) > int(l[i-1])):
        check+=1



print(check) 