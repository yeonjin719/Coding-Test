R = int(input())
S = int(input())

answer = R * 8 + S * 3 - 28
if answer < 0:
    answer = 0

print(answer)