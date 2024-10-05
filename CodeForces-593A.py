from collections import Counter
from itertools import combinations

i = int(input())
words = [input().strip() for _ in range(i)]

max_total_length = 0

for letter1, letter2 in combinations('abcdefghijklmnopqrstuvwxyz', 2):
    total_length = 0
    for word in words:
        count = Counter(word)
        if all(c in {letter1, letter2} for c in count):
            total_length += len(word)
    max_total_length = max(max_total_length, total_length)

print(max_total_length)
