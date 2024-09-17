n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

time1 = 0
limak = 0
for x in range(n):
    time1 += t[x]
    limak += max(0, p[x] - c * time1)

time2 = 0
radewoosh = 0
for x in range(n-1, -1, -1):
    time2 += t[x]
    radewoosh += max(0, p[x] - c * time2)

if limak > radewoosh:
    print('Limak')
elif limak < radewoosh:
    print('Radewoosh')
else:
    print('Tie')
