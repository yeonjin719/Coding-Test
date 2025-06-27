def n_queens(i, col):
    global cnt
    n = len(col) -1
    if (dfs(i, col)):
        if (i == n):
            cnt += 1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                n_queens(i+1, col)

def dfs(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

cnt = 0
n = int(input())
col = [0] * (n + 1)
n_queens(0, col)
print(cnt)