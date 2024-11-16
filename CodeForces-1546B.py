import sys
input = sys.stdin.readline
read= sys.stdin.buffer.read


f=lambda:map(int,input().split())

for _ in range(int(input())):
    n,m=f()
    d=[{} for  _ in range(m)]
    e=[{} for  _ in range(m)]
    # e={}
    for i in range(n):
        x=input().strip()
        for i in range(m):
            if x[i] not  in d[i]:
                d[i][x[i]]=0
            d[i][x[i]]+=1
    # print(d)
    for i in range(n-1):
        x=input().strip()
        for i in range(m):
            if x[i] not  in e[i]:
                e[i][x[i]]=0
            e[i][x[i]]+=1
    # print(e)
    s=[]
    for i in range(m):
        for j in d[i]:
            if j not in e[i]:
                s.append(j)
                break
            else:
                if d[i][j]!=e[i][j]:
                    s.append(j)
                    break
    print(''.join(s))