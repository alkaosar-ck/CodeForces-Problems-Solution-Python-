for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    same = 0
    while (same < len(s) and same< len(t) and 
           s[same] == t[same]):
        same += 1
    if same >0:
      operations = same + 1
    else:
       operations = 0
       same = 0
    operations += (len(s) - same) + (len(t) - same)
    print(operations)
