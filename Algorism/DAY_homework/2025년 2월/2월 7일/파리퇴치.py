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
    max_v = 0 # 죽은파리의 최대값
    for i in range(N):
        for j in range(N):
            s = 0 # 죽은파리수
            for k in range(M):
                for l in range(M):
                    if 0<=i+k<N and 0<= j+l <N: #유효성검사
                        
                        s+= matrix[i+k][j+l]  # 파리수 총합 더함
            if max_v < s:
                max_v = s
    
    result = max_v
    print(f'#{case} {result}')