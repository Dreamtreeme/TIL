T= int(input())
for case in range(1,T+1):
    N = int(input())
    di=[0,1,0,-1]
    dj=[1,0,-1,0]
    num=1
    matrix=[[0]*N for _ in range(N)]
    d=0
    r, c = 0, 0
    for i in range(N*N):
        matrix[r][c] = num
        num+=1
        ni , nj = r+di[d], c+dj[d]
        if 0<=ni<N and 0<=nj<N and matrix[ni][nj] ==0:
            r,c = ni, nj
        else:
            d= (d+1)%4
            r,c = r+di[d], c+dj[d]

    print(f'#{case}')
    for row in matrix:
        print(*row)