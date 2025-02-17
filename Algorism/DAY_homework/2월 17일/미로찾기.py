# 상, 하, 좌, 우로 이동하는 덧셈 값 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 탐색 함수
def bfs(maze, N):
    # 출발지 찾기
    start = None
    end = None
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':  # 출발지
                start = (r, c)
            elif maze[r][c] == '3':  # 도착지
                end = (r, c)
    
    # 큐를 이용한 BFS 탐색 (여기서는 리스트를 큐처럼 사용)
    queue = [start]
    visited = [[False] * N for _ in range(N)]
    visited[start[0]][start[1]] = True
    
    while queue:
        current_pos = queue.pop(0)  # 큐에서 첫 번째 원소를 꺼냄
        
        # 목적지에 도달하면 1을 리턴
        if current_pos == end:
            return 1
        
        # 상, 하, 좌, 우로 이동
        for dr, dc in directions:
            next_row, next_col = current_pos[0] + dr, current_pos[1] + dc
            if 0 <= next_row < N and 0 <= next_col < N:
                if maze[next_row][next_col] != '1' and not visited[next_row][next_col]:
                    if maze[next_row][next_col] == '0' or maze[next_row][next_col] == '3':
                        visited[next_row][next_col] = True
                        queue.append((next_row, next_col))

    return 0

# 테스트 케이스 개수 입력
T = int(input())

for t in range(1, T + 1):
    # 미로 크기 입력
    N = int(input())
    
    # 미로 입력
    maze = []
    for _ in range(N):
        line = input()  # 각 줄을 입력받고
        maze.append(list(line))  # strip 없이 그 자체로 리스트에 추가

    # BFS로 경로 찾기
    result = bfs(maze, N)
    
    # 결과 출력
    print(f'#{t} {result}')
