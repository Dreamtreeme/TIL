# N*N 격자. 각 칸은 . 빈칸, # 벽, U/D/L/R 컨베이어
# 매 분마다 모든 컨베이어가 시계방향으로 방향이 바뀐다
# 시작 S에서 도착 E까지 최단시간

# 이동규칙
# 1분에 한칸 상하좌우 이동가능
# 이동 후 그 칸이 컨베이어면, 그 시점의 방향으로 추가
# 1칸 강제이동(연쇄이동 없음, 벽/ 범위 밖이면 실패하고 해당 이동 무효)

# 조건 (2<= N <= 50)
# 출력 최단시간(분) or -1

# 생각
#1. 한턴에 최대 2칸 이동
#2. 벽이면 무효
#3. 빈칸일때 대기전략 유효
#4. 아무데나 가는 이동함수1개 만듦(상하좌우순)
#5. 시간증가는 이동할때마다 1씩 증가, 단 같이 갖고가야함
#6. 내 좌표, 현재시간, 다음에 갈 방향을 큐에 넣으면 작동


# 실제 풀이
# 1. bfs니 데큐를 임포트
from collections import deque
# 2. 입력 N을 받음(받고 인트로 변환)
result = -1
N = int(input())
# 3. 격자를 받음(리스트를 input으로 받고 .strip()으로 공백제거, 리스트로 변환)
grid = [list(input().strip()) for _ in range(N)]
# 4. 방향을 정의, 튜플로 (상,우,하,좌) 저장
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
# 5. 회전순서대로 딕셔너리로 저장
dirs_map = {'U':0,'R':1,'D':2,'L':3}
# 6. 격자에서 시작과 끝 좌표 찾음
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'S':
            sr,sc = i, j
        if grid[i][j] == 'E':
            er,ec = i, j
# 7 방문처리 3차원 리스트로 만듦(행,열,시간)
visited = [[[False]*4 for _ in range(N)]for _ in range(N)]
# 8. 데큐로 q생성
q = deque()
# 9. 시작좌표와 시간0을 넣고 방문처리
q.append((sr,sc,0))
visited[sr][sc][0] = True
# 10. while q: popleft로 (r,c,t) 꺼냄
while q:
    r,c,t=q.popleft()
    # 11. 출구조건
    if r==er and c == ec:
        result = t
        break
    # 12. 5가지 선택지(상하좌우+대기) for문
    for dr, dc in [(-1,0),(0,1),(1,0),(0,-1),(0,0)]:    
        # 13. 다음 좌표 저장, 범위밖/벽이면 continue
        nr, nc = r+ dr, c+dc
        if not (0<=nr<N and 0<=nc<N): continue
        if grid[nr][nc] == '#': continue
        # 14. 다음 좌표가 컨베이어면, 그 시점의 방향으로 추가이동

        if grid[nr][nc] in dirs_map:
            n_s = dirs_map[grid[nr][nc]] # 해당칸 맵핑 번호 다음 상태저장
            d = dirs[(t+n_s)%4] # 다음 이동할 좌표계산
            nr, nc = nr+d[0], nc+d[1] # 1번이동
            # 15. 범위밖/벽이면 continue
            if not (0<=nr<N and 0<=nc<N): continue
            if grid[nr][nc] == '#': continue

        # 16. 시간 1증가
        nt = t+1

        # 17. 방문처리 안했으면 방문처리하고 큐에 추가
        if not visited[nr][nc][nt %4]:
            visited[nr][nc][nt%4] = True
            q.append((nr,nc,nt))

# 18. while문 끝나고 도달못하면 -1출력, 아니면 시간출력
print(result)






