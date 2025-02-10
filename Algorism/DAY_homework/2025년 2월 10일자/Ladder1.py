T = 10
for _ in range(1, T + 1):
    test =int(input())
    ladder = [list(map(int,input().split())) for _ in range(100)]# 100*100인 배열 생성

    dr = [0,0,1] # 좌, 우,아래
    dc = [-1,1,0]

    result = 0
    for i in range(100):
        if ladder[0][i] :
            r, c = 0 , i # 시작위치
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

