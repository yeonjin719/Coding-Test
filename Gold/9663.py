def n_queens(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for col in range(n):
        if not visited_col[col] and not visited_diag1[row - col] and not visited_diag2[row + col]:
            visited_col[col] = visited_diag1[row - col] = visited_diag2[row + col] = True
            n_queens(row + 1)
            visited_col[col] = visited_diag1[row - col] = visited_diag2[row + col] = False

n = int(input())
cnt = 0
visited_col = [False] * n
visited_diag1 = [False] * (2 * n)  
visited_diag2 = [False] * (2 * n) 
n_queens(0)
print(cnt)