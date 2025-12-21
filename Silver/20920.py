import sys

N, M = map(int, sys.stdin.readline().split())
counts = {}

for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) < M:
        continue
    counts[word] = counts.get(word, 0) + 1

words = sorted(counts.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

for word, _ in words:
    print(word)
