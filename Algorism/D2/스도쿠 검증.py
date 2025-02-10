def check_sudoku(li):
    for i in range(9):
        row_count = [0] * 10  # 각 행의 숫자 개수 저장
        col_count = [0] * 10  # 각 열의 숫자 개수 저장
        for j in range(9):
            num_row = li[i][j]
            num_col = li[j][i]

            if row_count[num_row] > 0 or col_count[num_col] > 0:
                return 0  # 중복된 숫자 발견

            row_count[num_row] += 1
            col_count[num_col] += 1

    for i in range(3):
        for j in range(3):
            block_count = [0] * 10  # 각 3x3 부분 배열의 숫자 개수 저장
            for k in range(3):
                for l in range(3):
                    num = li[i*3 + k][j*3 + l]

                    if block_count[num] > 0:
                        return 0  # 중복된 숫자 발견

                    block_count[num] += 1

    return 1

T = int(input())

for test_case in range(1, T + 1):
    li = [list(map(int, input().split())) for _ in range(9)]
    result = check_sudoku(li)
    print(f'#{test_case} {result}')