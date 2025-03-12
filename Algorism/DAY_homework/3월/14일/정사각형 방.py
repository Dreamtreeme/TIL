# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# def d(r, c, cnt, start_num):
#     global mcount, num
#     # 경로 길이가 더 크면 mcount와 num을 갱신
#     if cnt > mcount:
#         mcount = cnt
#         num = start_num
#     # 경로 길이가 같으면 더 작은 start_num으로 num 갱신
#     elif cnt == mcount:
#         num = min(num, start_num)
    
#     for k in range(4):
#         nr = r + dr[k]
#         nc = c + dc[k]
#         if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] - 1 == arr[r][c]:
#             visited[nr][nc] = True
#             d(nr, nc, cnt + 1, start_num)
#             visited[nr][nc] = False

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     mcount = 0
#     num = 2**31  # 초기값을 충분히 큰 수로 설정
#     for r in range(N):
#         for c in range(N):
#             visited = [[False] * N for _ in range(N)]
#             visited[r][c] = True
#             d(r, c, 1, arr[r][c])  # 시작 방 번호를 전달
#     print(f'#{tc} {num} {mcount}')


    # #dp로 푸는법
    # import sys

# 방향 벡터: 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solve():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # DP 테이블 초기화: 모든 방은 최소 1개(자기 자신)
    dp = [[1] * N for _ in range(N)]
    
    # 방의 숫자와 위치를 저장
    rooms = [(arr[i][j], i, j) for i in range(N) for j in range(N)]
    # 숫자 내림차순으로 정렬
    rooms.sort(reverse=True, key=lambda x: x[0])
    
    # DP 계산
    for _, i, j in rooms:
        for k in range(4):
            ni = i + dr[k]
            nj = j + dc[k]
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
                dp[i][j] = max(dp[i][j], dp[ni][nj] + 1)
    
    # 최대 경로 길이와 최소 시작 번호 찾기
    max_dp = 0
    min_start = float('inf')
    for i in range(N):
        for j in range(N):
            if dp[i][j] > max_dp:
                max_dp = dp[i][j]
                min_start = arr[i][j]
            elif dp[i][j] == max_dp:
                min_start = min(min_start, arr[i][j])
    
    return min_start, max_dp

T = int(input())
for tc in range(1, T + 1):
    num, mcount = solve()
    print(f'#{tc} {num} {mcount}')