n=int(input())
check=False
l=input().split()
for i in range(0,len(l)-1):
    if int(l[i]) * int(l[i+1]) >0:
        check=True


if check==True:
    print("YES")
else:
     print("NO") 