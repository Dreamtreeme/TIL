def check_sudoku(li):
    # li = 9*9배열
    
    for i in range(9):
        # 각 숫자의 갯수 저장공간
        row_count = [0]*10
        col_count = [0]*10
        for j in range(9):
            num_row = li[i][j] # 각 숫자 저장
            num_col = li[j][i] #열 숫자
            if row_count[num_row]>0 or col_count[num_col]>0:
            #숫자 인덱스방에 1이 들어가있는 순간 중복
                return 0
            row_count[num_row]+=1
            col_count[num_col]+=1

    # 3*3 배열의 숫자도 확인
    for i in range(3):
        for j in range(3):
            arr_count = [0]*10
            for k in range(3):
                for l in range(3): # 각배열방 크기만큼 i와j에 곱해준값이 시작점
                    num_arr = li[3*i+k][3*j+l] 
                    if arr_count[num_arr]>0:
                        return 0
                    arr_count[num_arr]+=1

    
    return 1
T = int(input())

for test_case in range(1, T + 1):
    li = [list(map(int, input().split())) for _ in range(9)]
    result = check_sudoku(li)
    print(f'#{test_case} {result}')