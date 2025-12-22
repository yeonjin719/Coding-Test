A, B = map(int, input().split())
C, D = map(int, input().split())

answer = min(A+D, B+C)
print(answer)