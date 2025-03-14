xr = [1,1,-1,-1]
xc = [-1,1,1,-1]# 좌하,우하,우상,좌상

def recur(r,c,path_len,dir,path):
    global result
    if dir > 3: # 무조건 종료 방향은 3번 바꾸면 끝 가지치기 더 바꾸면 끝내야함.
        return
    if dir == 3 and (i,j) == (r,c): # 돌아온 경우
        result = max(result, path_len)
        return
    else: # 아직 방향전환을 모두 이루지 못함.
        for d in range(2):
            di = (dir + d) % 4
            nr = r + xr[di]
            nc = c + xc[di]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] not in path:
                    path.append(arr[nr][nc])
                    recur(nr, nc, path_len+1, dir+d, path)
                    path.pop()

T=int(input())
for tc in range(1, T+1):
    result=-1
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            start= (i,j)
            recur(i, j, 0,0,[])
    print(f'#{tc} {result}')

# 문제였던곳, 모든 경우를 다 봤지만 사실 방향 3번 바꾸면 끝나야함.
# 방향전환을 하는경우 안하는경우 2개로 나눠서 봐야함

# 대각선 방향으로 움직이고 사각형 모양을 그리며 출발한 카페로 돌아와야 한다. 문제를 잘 읽자

