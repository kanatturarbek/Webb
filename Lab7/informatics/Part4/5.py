n=int(input())
check=False
l=input().split()
for i in range(0,len(l)-1):
    if (int(l[i])>0 and int(l[i+1]) >0 )  or  (int(l[i])<0 and int(l[i+1])<0):
        check=True


if check:
    print("YES")
print("NO") 