# N x N 배열
# 5<= N <=15
# 2<= M <= N
# N[i][j] <30
T= int(input())
for case in range(1,T+1):
    N, M = list(map(int, input().split()))
    matrix=[]
    for _ in range(N):
        matrix.append(list(map(int, input().split()))) # 파리 배열 만들기
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    ci = [1,1,-1,-1]
    cj = [1,-1,-1,1]
    max_v = 0 # 파리의 최대값
    for i in range(N):
        for j in range(N):
            s = matrix[i][j] # 중심좌표 파리수
            for dir in range(4): # 4방향 각 반복
                for c in range(1, M): #분사세기만큼 조회
                    ni = i + di[dir]*c # 이동할 행 좌표
                    nj = j + dj[dir]*c # 이동할 열 좌표
                    if 0<=ni<N and 0<= nj <N: #예측 후 유효성검사
                        s+= matrix[ni][nj] # 파리수 총합 더함
            if max_v < s:
                max_v = s
    for i in range(N):
        for j in range(N):
            s = matrix[i][j]
            for dir in range(4): # 4방향 각 반복
                for c in range(1, M): #분사세기만큼 조회
                    ni = i + ci[dir]*c # 이동할 행 좌표
                    nj = j + cj[dir]*c # 이동할 열 좌표
                    if 0<=ni<N and 0<= nj <N: #예측 후 유효성검사
                        s+= matrix[ni][nj]
                if max_v < s:
                    max_v = s
    result = max_v
    print(f'#{case} {result}')