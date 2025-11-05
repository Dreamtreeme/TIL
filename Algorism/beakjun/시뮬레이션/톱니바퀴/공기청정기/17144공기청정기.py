import sys
input = sys.stdin.readline

# 입력 처리
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치 (항상 2개)
air = []
for r in range(R):
    if board[r][0] == -1:
        air.append((r, 0))

# 방향 (상, 우, 하, 좌)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# -------------------------
# 1. 확산 단계
# -------------------------
def spread():
    temp = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:  # 먼지가 있는 칸만
                spread_amount = board[r][c] // 5
                if spread_amount == 0:
                    continue
                cnt = 0
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if not (0 <= nr < R and 0 <= nc < C):
                        continue
                    if (nr, nc) in air:  # 공기청정기 칸
                        continue
                    temp[nr][nc] += spread_amount
                    cnt += 1
                board[r][c] -= spread_amount * cnt

    # 확산된 먼지 반영
    for r in range(R):
        for c in range(C):
            board[r][c] += temp[r][c]


# -------------------------
# 2. 공기청정기 순환 단계
# -------------------------
def build_top_path(top):
    # 반시계 방향 경로
    path = []
    path += [(top, c) for c in range(1, C)]                # →
    path += [(r, C-1) for r in range(top-1, -1, -1)]       # ↑
    path += [(0, c) for c in range(C-2, -1, -1)]           # ←
    path += [(r, 0) for r in range(1, top)]                # ↓
    return path

def build_bottom_path(bottom):
    # 시계 방향 경로
    path = []
    path += [(bottom, c) for c in range(1, C)]             # →
    path += [(r, C-1) for r in range(bottom+1, R)]         # ↓
    path += [(R-1, c) for c in range(C-2, -1, -1)]         # ←
    path += [(r, 0) for r in range(R-2, bottom, -1)]       # ↑
    return path

def shift_along(path):
    vals = [board[r][c] for (r, c) in path]
    new_vals = [0] + vals[:-1]  # 맨 앞은 깨끗한 공기
    for i in range(len(path)):
        r, c = path[i]        # path에서 좌표 꺼내기
        v = new_vals[i]       # new_vals에서 같은 위치의 값 꺼내기
        board[r][c] = v       # 보드에 반영

def air_clean():
    top, _ = air[0]
    bottom, _ = air[1]
    shift_along(build_top_path(top))
    shift_along(build_bottom_path(bottom))


# -------------------------
# 3. 시뮬레이션
# -------------------------
for _ in range(T):
    spread()
    air_clean()

# -------------------------
# 4. 남은 먼지 양 계산
# -------------------------
ans = 0
for r in range(R):
    for c in range(C):
        if board[r][c] > 0:
            ans += board[r][c]

print(ans)
