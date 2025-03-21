import heapq

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def dijkstra(sy, sx, gy, gx, board, N):
    hq = []
    heapq.heappush(hq, (0, sy, sx))  # (누적 비용, y, x)
    visited = [[0] * N for _ in range(N)]
    visited[sy][sx] = 1  # 시작점 방문 처리

    while hq:
        weight, ty, tx = heapq.heappop(hq)

        # 도착하면 최단 거리 반환
        if ty == gy and tx == gx:
            return weight

        for i in range(4):
            ny, nx = ty + dy[i], tx + dx[i]

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                visited[ny][nx] = 1  # 방문 처리
                heapq.heappush(hq, (weight + board[ny][nx], ny, nx))

# 입력값 처리
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    result = dijkstra(0, 0, N - 1, N - 1, board, N)
    print(f'#{tc} {result}')
