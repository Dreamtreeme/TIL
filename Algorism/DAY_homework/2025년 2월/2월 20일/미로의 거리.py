def bfs(i, j, N): # 시작위치 i, j, 크기 N
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i,j))
    visited[i][j] = 1
    while q:
        ti, tj = q.pop(0)
        if maze[ti][tj] == '3': # 출구도착했을때
            return visited[ti][tj] -2 # 입구에서 출구 사이의 빈칸 수
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            wi, wj = ti +di, tj+dj
            # 미로를 벗어나지않고, 벽이아니고
            if 0<= wi<N and 0<= wj<N and maze[wi][wj]!='1' and visited[wi][wj]==0:
                q.append((wi,wj)) #인큐표시
                visited[wi][wj] = visited[ti][tj] +1
        
    return 0 #출구에 도착하지 못했을때

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i , j

T=int(input())
for tc in range(1, T+1):
    N = int(input()) # 미로의 크기
    maze = [input() for _ in range(N)]
    sti , stj = find_start(N)
    ans = bfs(sti, stj, N)
    print(f'#{tc} {ans}')