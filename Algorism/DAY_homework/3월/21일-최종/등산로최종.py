# 방향 배열 (상, 하, 좌, 우)#이건 생각했음
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# DFS 함수
def dfs(r,c,cnt,load,visited,current_height):
    global result, arr, K, N #전역변수 선언
    result = max(result,load) # 여기선 max함수로 함

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            # 여기까진 동일
            next_height = arr[nr][nc] # 핵심 다른부분, 다음 값을 일단 넣어둠
            if next_height < current_height: #다음부분이 안 깍아도되면
                visited[nr][nc] = 1
                dfs(nr, nc, cnt, load + 1, visited, next_height)
                visited[nr][nc] = 0 # 실행함
            elif cnt: # 나는 깎는거 먼저 했는데 여기선 그 반대 깎아야하는 경우만 봄
                e = next_height - current_height +1 # 다음값에 현재길이 뺀거에 1을 더해야 깎는값나옴
                # 예를들어 다음값9 현재값9라면 9-9+1은 1 1만깎아도 내려감
                # 이부분이 가장 차이나는거 같음. 불필요한 반복 필요없음. 한번만 내려가야 다음이 모두 7이여도 갈 수 있음. 7까지 깎은건 어차피 동일해서 막히는 부분
                if e <= K and e > 0:  # 깎을 수 있으면
                    visited[nr][nc] = 1
                    dfs(nr, nc, 0, load + 1, visited, current_height - 1)
                    visited[nr][nc] = 0


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
    for r, c in starts: # 나는 bfs로 따로 뺏지만 여기선 리스트로 실행
        visited = [[0] * N for _ in range(N)] 
        visited[r][c] = 1 
        dfs(r, c, 1, 1, visited, arr[r][c])  # 여기파라미터 부분부터 다름
        # 나는 깎기기회, 스택, 방문배열,배열,현재경로길이를 넘김
        # 여기선 행, 열, 깎기 기회, 경로 길이, 방문 배열, 현재 높이를 넘김 스택에 행,열,현재높이를 합치지 않음

    print(f'#{tc} {result}')

#결론 : 접근방식은 맞았음. 하지만 문제 조건설정을 더 유심히 볼것. 그리고 파라미터를 넘길때 귀찮아도 그대로 쓰는게 나을 수 잇음. 또 조건에 맞춰 시뮬레이션 그려보기