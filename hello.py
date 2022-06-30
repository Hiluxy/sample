n,k=map(int,input().split())
a=[]
cnt=0

for i in range(n):
     a.append(int(input()))

for i in reversed(range(n)):
        if (k//a[i])!=0:
                k%=a[i]
                cnt+=k//a[i]

print(cnt)
