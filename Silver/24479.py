import sys
sys.setrecursionlimit(10**5)
def input():
    return sys.stdin.readline().rstrip()
N, M, R = map(int, input().split())
graph = [[] for _ in range(N)]
dfns = [0] * (N)
dfn = 1

for i in range(M):
  u, v = map(int, input().split())
  graph[u-1].append(v-1)
  graph[v-1].append(u-1)

graph = [sorted(g) for g in graph]

def dfs(r):
  global dfn
  for i in graph[r]:
    if dfns[i] == 0:
      dfn += 1
      dfns[i] = dfn
      dfs(i)

dfns[R-1] = 1
dfs(R-1)

for i in dfns:
  print(i)