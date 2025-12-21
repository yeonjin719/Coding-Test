import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

evens = [x for x in arr if x % 2 == 0]
odds = [x for x in arr if x % 2 == 1]

INF = 10**18
min_even = INF  
min_odd  = INF

for lst in (evens, odds):
    for i in range(1, len(lst)):
        min_even = min(min_even, lst[i] - lst[i-1])

i = j = 0
while i < len(evens) and j < len(odds):
    min_odd = min(min_odd, abs(evens[i] - odds[j]))
    if evens[i] < odds[j]:
        i += 1
    else:
        j += 1

if min_even == INF: min_even = -1
if min_odd  == INF: min_odd  = -1

print(min_even, min_odd)