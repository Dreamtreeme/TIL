import sys
sys.stdin = open("input.txt", "r")
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*(N*N+1) # 숫자가 1부터 시작하기에 

    # 현재 위치 숫자 기준 상하좌우 확인
    # 1큰곳이 있다면 visited 기록
    for r in range(N):
        for c in range(N):
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if not (0<=nr<N) or not (0<=nc<N):
                    continue
                if arr[nr][nc] == arr[r][c] +1:
                    # 현재숫자는 다음으로 이동이 가능하다
                    visited[arr[r][c]] = 1
                    break # 나머지 방향은 볼 필요 없음
    #연속된 1의 개수가 가장 긴 곳을 찾는다.
    # 가장 긴 곳, 현재 몇 개인지, 출발지
    max_cnt = cnt= start = 0
    for i in range(1, N*N+1):
        if visited[i] ==1:
            cnt+=1
        elif visited[i] == 0:
            if max_cnt<cnt:
                max_cnt=cnt
                start = i - cnt
            cnt = 0
    print(f'#{tc} {start} {max_cnt+1}')


    # #dp로 푸는법


# 방향 벡터: 상, 하, 좌, 우
# 이차원리스트, 델타배열+조건
# 숨겨진 규칙이 없으면 완전탐색
# 이차원 배열로만 생각하지말고 1차원 리스트로 펴보는 생각을 해본다
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
    
#     path = [[1] * N for _ in range(N)]
    
#     # 방의 숫자와 위치를 저장
#     rooms = [(arr[i][j], i, j) for i in range(N) for j in range(N)]
#     # 숫자 내림차순으로 정렬
#     rooms.sort(reverse=True, key=lambda x: x[0])
    
#     # DP 계산
#     for _, i, j in rooms:
#         for k in range(4):
#             ni = i + dr[k]
#             nj = j + dc[k]
#             if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j] + 1:
#                 path[i][j] = path[ni][nj] + 1
    
#     # 최대 경로 길이와 최소 시작 번호 찾기
#     max_path = 0
#     min_start = float('inf')
#     for i in range(N):
#         for j in range(N):
#             if path[i][j] > max_path:
#                 max_path = path[i][j]
#                 min_start = arr[i][j]
#             elif path[i][j] == max_path:
#                 min_start = min(min_start, arr[i][j])
#     print(f'#{tc} {min_start} {max_path}')
