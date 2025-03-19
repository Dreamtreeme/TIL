import sys
from collections import deque
import copy
sys.stdin= open("input.txt" , "r")
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def blocksort(arr):
    for c in range(W):
        idx = H-1
        for r in range(H-1, -1, -1):
            if arr[r][c]: # 만약 블록이 남아있으면
                arr[r][c], arr[idx][c] = arr[idx][c],arr[r][c]
                idx-=1

def bfs(r,c,arr):
    q = deque([(r,c,arr[r][c])]) #데큐에 좌표와 값 넣음
    broken_blocks=0
    if arr[r][c] != 0:
        broken_blocks += 1
    arr[r][c]=0 # 맞은곳 초기화

    while q:
        r,c,b = q.popleft()
        for k in range(1, b): # b는 써진 숫자범위
            for i in range(4): # 델타방향만큼 반복
                nr = r+(dy[i]*k)
                nc = c+(dx[i]*k)

                # 조건 시작
                if not (0<=nr<H) or not (0<=nc<W):
                    continue
                if arr[nr][nc] : # 범위안에 들어있고 0이아니면 파괴할 벽돌
                    q.append((nr,nc,arr[nr][nc]))
                    broken_blocks+=1
                    arr[nr][nc]=0 # 방문처리
    return broken_blocks



def dfs(cnt, remains, arr):
    global min_blocks
    # 종료조건
    if cnt==N or remains==0:
        #더이상 할 필요 없으므로
        min_blocks = min(min_blocks,remains)
        return
    
    for col in range(W): # 가로 열 갯수만큼 구슬 쏠 준비
        copy_arr = copy.deepcopy(arr) # 한번 쏠때마다 넘겨줄 배열
        
        row =-1 # 벽돌이 없는경우
        for r in range(H):
            if copy_arr[r][col]:
                # 벽돌찾았으면
                row = r
                break
        if row ==-1: # 벽돌없으면 다음 열 쏠 준비
            continue

        broken_block = bfs(row,col,copy_arr) #파괴할 부분갯수세고
        blocksort(copy_arr)# 맵 정렬한뒤
        dfs(cnt+1, remains-broken_block, copy_arr)# 구슬횟수증가, 남은 갯수-파괴할갯수, 정렬된 맵 넘겨주기

 
T = int(input())
 
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
 
    # 1. 최소 벽돌
    # 2. 현재 벽돌이 다 깨지면 더 이상 할 필요 없음. -> 현재 벽돌 수를 관리하자.
    # 3. N 번 굴리면 끝난다.
    #  - 0번부터 시작, N번 까지 반복
    #  - 무조건 모두 굴려보아야 정답이 나온다. (DFS)
    #  - 한 번 굴렸을 때 벽돌들이 연쇄로 깨진다
    #    - 현재 기준으로 퍼져나가면서 탐색한다 (BFS)
 
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_blocks = 1e9
    blocks = 0
    # 현재 벽돌 수 계산
    for row in arr:
        for el in row:
            if el:
                blocks += 1
 
    dfs(0, blocks, arr) # 안에 dfs,bfs,맵 정렬함수있음
    result = min_blocks
    print(f'#{tc} {result}')
