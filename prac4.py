n=int(input())
ans=[]
while n>0:
    ans.append(n%10)
    n//=10
print(ans)