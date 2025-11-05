from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [input().strip() for _ in range(n)]

# check[r][c] = (r,c)에 도달했을 때 사용한 최소 벽 부순 횟수
check = [[k + 1 for _ in range(m)] for _ in range(n)]
check[0][0] = 0

dr = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dc = [0, 1, 0, -1]

queue = deque()
queue.append([0, 0, 0])  # (r, c, 지금까지 부순 벽 개수)

cnt = 1       # 현재 이동 거리
day = True    # 낮 여부 (True=낮, False=밤)

while queue:
    # 현재 거리(cnt)에서 탐색할 노드들 모두 처리
    for _ in range(len(queue)):
        r, c, w = queue.popleft()

        # 목표 지점 도달 시 결과 출력
        if r == n - 1 and c == m - 1:
            print(cnt)
            exit(0)

        # 사방 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 범위 안이고, 더 적게 벽을 부순 경우에만 탐색
            if 0 <= nr < n and 0 <= nc < m and check[nr][nc] > w:
                if board[nr][nc] == '0':
                    # 빈칸이면 이동
                    check[nr][nc] = w
                    queue.append([nr, nc, w])
                elif w < k:
                    if not day:
                        # 밤이면 벽 부술 수 없음 → 제자리 대기
                        queue.append([r, c, w])
                    else:
                        # 낮이면 벽 부수고 이동
                        check[nr][nc] = w + 1
                        queue.append([nr, nc, w + 1])

    # 한 턴이 끝나면 거리 증가, 낮/밤 전환
    cnt += 1
    day = not day

# 목표 지점 도달 불가 시 -1 출력
print(-1)
