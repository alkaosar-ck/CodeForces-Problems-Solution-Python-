from collections import Counter

for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    p = input().strip()

    target = Counter(t)
    from_s = Counter(s)
    from_p = Counter(p)

    have = from_s + from_p

    possible = True
    for char in target:
        if target[char] > have[char]:
            possible = False
            break

    if not possible:
        print('NO')
        continue
    j = 0
    current = 0
    for x in t:
       if x == s[current]:
          current+=1
          j+=1
          if current == len(s):
             break
    if j == len(s):
       print('YES')
    else:
       print('NO')
