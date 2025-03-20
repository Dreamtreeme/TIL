#출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라지기 때문에, 최적의 경로로 이동하면 최소한의 연료로 이동할 수 있다.

# 다음은 각 지역의 높이를 기록한 표의 예로, 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래이며, 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.

# (표에 표시되지 않은 지역이나 대각선 방향으로는 이동 불가.)
import heapq

dr = [-1,1,0,0]
dc = [0,0,-1,1]
def dijkstra():
    hq = [(0, 0, 0)]
    visited = [[0]*N for _ in range(N)] # 2차원 체크
    visited[0][0]=1

    while hq:
        
        weight, r,c = heapq.heappop(hq)

        if r==N-1 and c==N-1:
            return weight
         
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if not (0<=nr<N) or not (0<=nc<N):
                continue
            if visited[nr][nc] :
                continue
            visited[nr][nc]=1
            heapq.heappush(hq,(weight+1+abs(arr[nr][nc]-arr[r][c]), nr, nc))


T=int(input())
for tc in range(1, T+1):
    N= int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = dijkstra()
    print(f'#{tc} {result}')