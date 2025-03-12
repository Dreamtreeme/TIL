# N*N칸에 숫자가 적힌 판이 주어지고 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.

# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가
# 되도록 움직였다면 이때까지 합계가 얼마인지 출력

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def d(r, c, current_sum):
    global min_sum
    if r == N-1 and c == N-1:
        if current_sum < min_sum:
            min_sum = current_sum
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            d(nr, nc, current_sum + arr[nr][nc])
            visited[nr][nc] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    min_sum = float('inf')
    visited[0][0] = True
    d(0, 0, arr[0][0])
    print(f'#{tc} {min_sum}')
    