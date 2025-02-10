# N x N 행렬이 주어질 때,

# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

def rotate90(matrix, n):
    
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[i][j] = matrix[n-1-j][i]
    return rotated
            

T=int(input())

for test_case in range(1, T + 1):
    N= int(input())
    matrix=[]
    for i in range(N):
        matrix.append(list(input().split()))
    matrix_90 = rotate90(matrix,N)
    matrix_180 = rotate90(matrix_90,N)
    matrix_270 = rotate90(matrix_180,N)
    print(f'#{test_case}')
    result = ""
    for i in range(N):
        row_90 = "".join(map(str, matrix_90[i]))  # 각 행의 요소들을 문자열로 연결
        row_180 = "".join(map(str, matrix_180[i]))
        row_270 = "".join(map(str, matrix_270[i]))
        result = f"{row_90} {row_180} {row_270}\n"
        print(f'{result}', end="")
   