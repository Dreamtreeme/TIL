# 문제읽기
'''
교도소로 이송중이던 흉악범이 탈출하는 사건이 발생하여 수색에 나섰다.
탈주범은 탈출한 지 한시간뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,
지하 터널 어딘가에서 은신 중인것으로 추정된다.
터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의
개수를 계산하여야 한다.
탈주범은 시간당 1의 거리를 움직일 수 있다.
지하 터널은 총 7종류의 터널 구조물로 구성

유추
1. 시간이 주어짐
2. 탈주범이 있을 수 있는 위치의 개수를 계산해야함
3. 터널 구조물에 따라 이동 할 수 있는 위치가 달라짐
4. 이동하는 곳의 터널 구조물도 확인해야함
5. 방문한곳 표시해야함
6. BFS로 접근해야함
'''

# 자료구조
'''
1. 테스트케이스 T
2. N,M: 세로, 가로 크기 (5 <= N,M <= 50)
3. R,C: 맨홀 뚜껑이 뚫린 위치
4. L: 탈출 후 소요된 시간 (1 <= L <= 20)
5. N개의 줄에 지하 터널 지도 정보'''

# 알고리즘설계
'''
최악의 경우 시간복잡도는 50*50 = 2500 이므로 충분히 가능하다.
재귀함수는 불가능
1. 터널의 종류를 딕셔너리로 만든다
2. BFS 로 접근 따라서 deque를 사용한다

'''
from collections import deque

dr = [-1,1,0,0] # 상하좌우
dc = [0,0,-1,1]

types ={
    1:[1,1,1,1],
    2:[1,1,0,0],
    3:[0,0,1,1],
    4:[1,0,0,1],
    5:[0,1,0,1],
    6:[0,1,1,0],
    7:[1,0,1,0],
}
def bfs(R,C):
    q = deque([(R,C)])
    visited[R][C]=1
    while q:
        nowr, nowc = q.popleft()
        dirs = types[tunner[nowr][nowc]]

        for i in range(4):
            if dirs[i]==0:
                continue
            new_r = nowr + dr[i]
            new_c = nowc + dc[i]
            if not 0<=new_r<N or not 0<=new_c<M:
                continue
            if visited[new_r][new_c] :
                continue
            if tunner[new_r][new_c] == 0:
                continue

            new_dirs = types[tunner[new_r][new_c]]

            if i %2 ==0 and new_dirs[i+1]==0:
                continue
            if i % 2 ==1 and new_dirs[i-1]==0:
                continue
            if visited[nowr][nowc] + 1 > L:
                continue

            visited[new_r][new_c] = visited[nowr][nowc]+1
            q.append((new_r,new_c))
T= int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunner = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    bfs(R,C)
    result=0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                result+=1
    print(f'#{tc} {result}')