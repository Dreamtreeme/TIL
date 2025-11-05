import sys
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
robot_r, robot_c, direction = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# 방향: 북(0), 동(1), 남(2), 서(3)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def turn_left(d):
    """반시계방향 90도 회전"""
    return (d - 1) % 4

def clean_room():
    cleaned_count = 0
    r, c, d = robot_r, robot_c, direction
    
    while True:
        # 1. 현재 칸이 청소되지 않은 경우 청소
        if room[r][c] == 0:
            room[r][c] = 2  # 청소 완료 표시
            cleaned_count += 1
        
        # 2. 주변 4칸 중 청소되지 않은 빈 칸 찾기
        found_clean_spot = False
        
        for _ in range(4):
            d = turn_left(d)  # 왼쪽으로 회전
            nr = r + dr[d]
            nc = c + dc[d]
            
            # 청소되지 않은 빈 칸이 있으면 이동
            if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
                r, c = nr, nc
                found_clean_spot = True
                break
        
        # 3. 청소할 곳이 없으면 후진
        if not found_clean_spot:
            # 후진 방향 계산 (현재 방향의 반대)
            back_r = r - dr[d]
            back_c = c - dc[d]
            
            # 후진 가능하면 후진
            if 0 <= back_r < n and 0 <= back_c < m and room[back_r][back_c] != 1:
                r, c = back_r, back_c
            else:
                # 후진 불가능하면 작동 종료
                break
    
    return cleaned_count

print(clean_room())