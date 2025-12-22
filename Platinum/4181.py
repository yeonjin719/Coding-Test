import sys, math
input = sys.stdin.readline

N = int(input())
points = []
for _ in range(N):
    x, y, c = input().split()
    if c == "N":
        continue
    points.append((int(x), int(y)))

minPoint = min(points, key=lambda p: (p[0], p[1]))
x0, y0 = minPoint

others = []
for x, y in points:
    if (x, y) == minPoint:
        continue
    dx, dy = x - x0, y - y0
    ang = math.atan2(dy, dx)
    if ang < 0:
        ang += 2 * math.pi          # 0 ~ 2pi로 보정 (CCW)
    dist2 = dx*dx + dy*dy
    others.append((ang, dist2, x, y))

# 1) 각도 오름차순, 같은 각도면 거리 오름차순
others.sort(key=lambda t: (t[0], t[1]))

# 2) "마지막 각도"와 같은 각도인 구간만 뒤집기 (거리 내림차순 효과)
EPS = 1e-12
last_ang = others[-1][0]
k = len(others) - 1
while k > 0 and abs(others[k-1][0] - last_ang) < EPS:
    k -= 1
others[k:] = reversed(others[k:])

print(len(others) + 1)
print(x0, y0)
for _, __, x, y in others:
    print(x, y)