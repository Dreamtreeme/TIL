#N-Queen

# (r,c) 좌표에 쿠니을 놓은 적이 있다.
# 방문 기록 방법
# 1. 이차원 배열
# 2. 일차원 배열로 효율적으로 하는법

# level: N개의 행 만큼
# branch : N 개의 열
def check(row, col):
    # 1. 같은 열에 놓은 적이 있는가
    for r in range(row):
        if visited[r][col]:
            return False
    # 2. 왼쪽 대각선
    i,j = row -1, col -1
    while i>=0 and j>=0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1
    # 3. 오른쪽 대각선
    i,j = row -1, col +1
    while i>=0 and j<N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    # # 반복문 버전
    # for i , j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
    #     if visited[i][j]:
    #         return False
def dfs(row):
    global answer
    # 기저조건
    if row == N:
        answer+=1
        return
    
    #후보군 N개의 열
    for col in range(N):
        # 여기에다 가지치기 써줌
        if check(row,col) is False:# 기존에 같은 열이나 대각선에 놓았다면 안된다. 코드가 길어지면 함수로 빼자
            continue
        visited[row][col] = 1
        dfs(row+1)
        visited[row][col] = 0

N=4
# 1. 이차원 배열 방문기록
visited = [[0]* N for _ in range(N)]
# 2. 일차원 배열
# if abs(visited[row]-visited[col])==abs(row-col)
answer = 0 # 가능한 정답의 수




