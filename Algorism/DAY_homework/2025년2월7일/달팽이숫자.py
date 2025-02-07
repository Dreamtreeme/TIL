T= int(input())
for case in range(1,T+1):
    N = int(input())
    di = [0,1,0,-1]
    dj = [1,0,-1,0] # 방향좌표
    matrix=[[0]*N for _ in range(N)]
    dir = 0 # 방향지정
    num=1 # 시작번호준비
    r,c =0 ,0 # 시작 좌표지정
    for i in range(N*N):
        
        matrix[r][c]=num
        num +=1
        ni,nj = r+di[dir], c+dj[dir] #시작좌표에 방향이동
        if 0<= ni < N and 0<= nj <N and matrix[ni][nj] ==0 : 
            #유효성 검사 1. 배열 안에있는지, 2.숫자를 이미 기입했는지(0을만나면 아직기입X)
            r, c = ni, nj
        else:
            dir = (dir+1)%4 # 방향전환 방향이 바뀌면 더해지는 값도 바뀜
            r, c = r+ di[dir], c+dj[dir]
            

    
    
    print(f'#{case}')
    for row in matrix:
        print(*row)