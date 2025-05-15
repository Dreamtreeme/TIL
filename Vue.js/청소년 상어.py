import copy

# 8방향 (상, 좌상, 좌, 좌하, 하, 우하, 우, 우상)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 입력 처리
board = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        # 물고기 번호와 방향 저장 (방향은 0~7로 변환)
        board[i][j] = [data[2*j], data[2*j+1]-1]

# 물고기 이동 함수
def move_fish(board, shark_x, shark_y):
    for fish in range(1, 17):  # 물고기 번호 1~16
        # 물고기 위치 찾기
        x, y = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j] and board[i][j][0] == fish:
                    x, y = i, j
                    break
            if x != -1:
                break
        if x == -1:  # 물고기가 없으면(먹힘) 다음 물고기로
            continue
        
        dir = board[x][y][1]  # 현재 물고기 방향
        for _ in range(8):  # 최대 8번 회전
            nx, ny = x + dx[dir], y + dy[dir]
            # 이동 가능 여부 확인 (격자 안이고, 상어가 없는 위치)
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == shark_x and ny == shark_y):
                # 물고기 위치 교환
                board[x][y][1] = dir  # 현재 물고기 방향 업데이트
                board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                break
            dir = (dir + 1) % 8  # 45도 회전

# 상어 이동 가능 위치 찾기
def get_possible_moves(board, shark_x, shark_y, shark_dir):
    moves = []
    x, y = shark_x, shark_y
    # 상어 방향으로 쭉 이동
    while True:
        x += dx[shark_dir]
        y += dy[shark_dir]
        if 0 <= x < 4 and 0 <= y < 4:
            if board[x][y]:  # 물고기가 있으면 이동 가능
                moves.append((x, y))
        else:
            break
    return moves

# DFS로 최대 합 계산
def dfs(board, shark_x, shark_y, total):
    global max_total
    # 현재 상태 복사
    board = copy.deepcopy(board)
    
    # 상어가 현재 위치의 물고기 먹기
    if board[shark_x][shark_y]:
        fish_num, shark_dir = board[shark_x][shark_y]
        total += fish_num
        board[shark_x][shark_y] = None  # 물고기 제거
    else:
        return  # 물고기가 없으면 종료
    
    # 최대 합 갱신
    max_total = max(max_total, total)
    
    # 물고기 이동
    move_fish(board, shark_x, shark_y)
    
    # 상어 이동 가능 위치 탐색
    possible_moves = get_possible_moves(board, shark_x, shark_y, shark_dir)
    
    # 각 이동 위치에 대해 DFS
    for nx, ny in possible_moves:
        dfs(board, nx, ny, total)

# 메인
max_total = 0
dfs(board, 0, 0, 0)
print(max_total)