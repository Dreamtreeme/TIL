# 파리퇴치3
# N*N배열 안 파리 잡기 (5<=N<=15)
# M은 스프레이세기 (2<=M<=N)
# 파리는 30마리 이하

#완전탐색
#입력순서 1.테스트케이스, 2.N과 M, 3이후 N의1행부터 끝까지
def solve():
    N, M = list(map(int, input().split()))
    matrix = []
    for i in range(0,N-1):
        row = list(map(int, input().split()))
        matrix.extend(row)
    
    udlr = create_directions(M)
    cross = create_directions_cross(M)

    for i in range(0, N-1):
        for j in range(0, N-1):
            total += matrix[]

def calculate_flies(board, x, y, N):
    
    total = board[x][y]  # 중심 좌표의 값을 먼저 더함
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 상, 하, 우, 좌
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            total += board[nx][ny]
    return total

def create_directions(m): #상하좌우 뿌리는경우
    directions = []
    for i in range(1, m+1):
        directions.extend([(0, i), (0, -i), (i, 0), (-i, 0)])  # 상하좌우 i만큼 이동
    return directions

def create_directions_cross(m):

    directions_cross = []
    for i in range(1, m+1):
        # 대각선
        directions_cross.extend([(i, i), (-i, i), (-i, -i), (i, -i)])
    return directions_cross


T= int(input())
for case in range(1, T):
    answer=solve()
    print(f'{case} {answer}')
