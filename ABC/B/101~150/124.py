n=int(input())
h=list(map(int,input().split()))

ans=1
for i in range(1,n):
    if max(h[:i])*i<=h[i]*i:
        ans+=1
print(ans)