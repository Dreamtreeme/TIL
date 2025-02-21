def startpoint(N):
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                return r,c

def dfs(r, c, N, visited):
    if not (0 <= r < N and 0 <= c < N) or visited[r][c] or maze[r][c] == '1':
        return False

    if maze[r][c] == '3':
        return True

    visited[r][c] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if dfs(nr, nc, N, visited):
            return True

    return False

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [input() for _ in range(N)]
    str1, stc1 = startpoint(N)
    result = 0
    visited = [[False] * N for _ in range(N)]
    if dfs(str1, stc1, N, visited):
        result = 1
    print(f"#{t} {result}")