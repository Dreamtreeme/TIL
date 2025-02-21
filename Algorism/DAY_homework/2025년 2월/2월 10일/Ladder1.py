# 핵심풀이
# 델타를 이용해 방향정하고
# 정한 방향으로 좌표이동
T = 10
for _ in range(1, T + 1):
    test =int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]# 

    dr = [0,0,1] # 좌, 우,아래
    dc = [-1,1,0]

    result = 0
    for i in range(100): # 100개의 행 위치 확인
        if ladder[0][i] : # 어차피 첫번째 위치에 시작점이니
            r, c = 0 , i # 시작위치 row, colum은 0행 열위치
            d=2
            
            while r < 99 :
                
                if d == 2:
                    if c > 0 and ladder[r][c-1]:
                        d=0
                    elif c < 99 and ladder[r][c+1]:
                        d=1
                else:
                    if ladder[r+1][c]:
                        d=2
                # 방향을 설정하고 이제 좌표증가
                r += dr[d] # 좌표방향만큼 행 위치증가
                c += dc[d] # 좌표방향만큼 열 위치증가
        
            if ladder[r][c] ==2:
                result = i
                break
    print(f'#{test} {result}')

