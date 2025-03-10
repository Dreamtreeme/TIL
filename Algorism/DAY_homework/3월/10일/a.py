import sys
sys.stdin = open("input.txt", "r")
from collections import deque

# 리스트에서 제일 앞에 데이터를 꺼내면 리스트의 길이만큼 시간이 발생생
# 터널들의 종류에 따라, 이동가능여부
types= {
    1: [1,1,1,1],
    2: [1,1,0,0],
    3: [0,0,1,1],
    4: [1,0,0,1],
    5: [0,1,0,1],
    6: [0,1,1,0],
    7: [1,0,1,0],
}
# 1. BFS 로 접근
# - 이동이 불가능한 케이스
#   1) 범위 밖으로 나가면못감
#   2) 이미 방문한 곳은 안감
#   3) 현재 위치에서 갈 수 없는 방향으로 가면 안됨
#   4) 다음 가려는 곳의 터널이 뚫려있어야함
# 2. 방문 기록을 해야한다 (visited)
def bfs(R,C):
    dq = deque([(R,C)])
    visited[R][C] = 1 # 출발점 초기화

    while dq:
        nowr, nowc = dq.popleft()
        dirs = types[tunnel[nowr][nowc]]
        for i in range(4):
            # 출구가 안열려있는 경우 continue
            if dirs[i] == 0:
                continue
            new_r = nowr + dx[i]
            new_c = nowc + dy[i]
            # 범위 넘어가면 pass
            if new_r < 0 or new_r >= N or new_c < 0 or new_c >= M:
                continue
            # 이미 방문했다면 pass
            if visited[new_r][new_c]:
                continue
            # 못가면 pass
            if tunnel[new_r][new_c] == 0:
                continue

            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[tunnel[new_r][new_c]]

            # 현재 상좌 -> next_dirs가 하우 안뚤렸으면 못감
            if i % 2 == 0 and next_dirs[i+1] == 0:
                continue
            # 현재 하우 -> next_dirs가 상좌 안뚤렸으면 못감
            if i % 2 == 1 and next_dirs[i-1] == 0:
                continue
            # 시간을 +1 해주면서 기록
            visited[new_r][new_c] = visited[nowr][nowc] + 1
            dq.append((new_r, new_c))
T= int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    bfs(R,C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] and visited[i][j] <= L:
                cnt += 1
    
    print(f'#{tc} {cnt}')
