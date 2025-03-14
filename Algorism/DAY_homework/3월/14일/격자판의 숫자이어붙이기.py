dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_numbers(cnt, current_number, r, c):
    global result, arr
    if cnt == 7:
        result.add(current_number) # set 자료형에 추가 (중복 자동 제거)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            find_numbers(cnt + 1, current_number + str(arr[nr][nc]), nr, nc)
            # current_number를 문자열로 관리

T = int(input())
for tc in range(1, T + 1):
    result = set() # set 자료형으로 중복제거
    arr = [list(map(int, input().split())) for _ in range(4)]
    for r in range(4):
        for c in range(4):
            find_numbers(1, str(arr[r][c]), r, c) 
    print(f'#{tc} {len(result)}') 


# 다 출발시켜보고, 델타배열쓰고, 까진 맞음. 
# level과 branch 의 갯수를 트리그림으로 그려보고 세봄
# set을 생각해내야함!!!!!!!!!!! 중복안됨 특징

# 접근법 
# 시작 지점: 전체 다 보아야한다.
# 재귀돌리면서 숫자를 붙인다
# 숫자가 7자리가 되면, set에 넣는다
def recur(r,c,number):
    if len(number) ==7: #7자리가 되면 종료
        result.add(number)
        return
    
    for k in range(4): #상하좌우 확인
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < 4 and 0 <= nc < 4:
            recur(nr,nc,number + matrix[nr][nc])
T= int(input())
for tc in range(1,T+1):
    matrix = [input().split() for _ in range(4)]
    result = set()
    for r in range(4):
        for c in range(4):
            recur(r,c,matrix[r][c])
    print(f'#{tc} {len(result)}')