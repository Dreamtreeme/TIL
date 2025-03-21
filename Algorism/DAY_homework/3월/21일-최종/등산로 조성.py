# 방향 배열 (상, 하, 좌, 우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# DFS 함수
def dfs(r, c, cnt, load, visited, current_height):
    global result, arr, K, N
    result = max(result, load)  # 최대 경로 길이 갱신

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            next_height = arr[nr][nc]
            if next_height < current_height:  # 깎지 않고 이동 가능
                visited[nr][nc] = 1
                dfs(nr, nc, cnt, load + 1, visited, next_height)
                visited[nr][nc] = 0
            elif cnt:  # 깎기 기회 있음
                # 필요한 최소 깊이 계산
                e = next_height - current_height + 1
                if e <= K and e > 0:  # 깎을 수 있으면
                    visited[nr][nc] = 1
                    dfs(nr, nc, 0, load + 1, visited, current_height - 1)
                    visited[nr][nc] = 0

# 전역 변수 선언
arr = []
result = 0
K = 0
N = 0

# 입력 처리 및 실행
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 가장 높은 지점 찾기
    maxnum = max(max(row) for row in arr)
    starts = [(i, j) for i in range(N) for j in range(N) if arr[i][j] == maxnum]

    result = 0
    for r, c in starts:
        visited = [[0] * N for _ in range(N)]
        visited[r][c] = 1
        dfs(r, c, 1, 1, visited, arr[r][c])  # (행, 열, 깎기 기회, 경로 길이, 방문 배열, 현재 높이)

    print(f'#{tc} {result}')