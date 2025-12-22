N = int(input())
W = int(input())

point = 0
point += N * 10
if N >= 3:
  point += 20

if N == 5:
  point += 50

if W > 1000:
  point -= 15

if point < 0:
  point = 0

print(point)