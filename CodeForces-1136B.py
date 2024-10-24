n,k = map(int,input().split())
total = 2*n+1
m = min((k-1)+n-1,(n-k)+n-1)
print(total+m)