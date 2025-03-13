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