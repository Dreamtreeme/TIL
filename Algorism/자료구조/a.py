#2개의 함수필요

#대각선 함수
def cross(mtx):
    cross_total_list=[]
    for i in range(len(mtx)):
        total=0
        for j in range(len(mtx[i])):
            if i==j or i+j==len(mtx[i])+1:
                total+=mtx[i][j]
                cross_total_list.append(total)
    return cross_total_list

# 행 함수
def row(mtx):
    row_total_list=[]
    for i in range(len(mtx)):
        total=0
        for j in range(len(mtx)):
            total+=mtx[i][j]
            row_total_list.append(total)
    return row_total_list

# 열 함수
def colum(mtx):
    colum_total_list=[]
    for i in range(len(mtx)):
        total=0
        for j in range(len(mtx)):
            total +=mtx[j][i]
            colum_total_list.append(total)
    return colum_total_list

#각 함수 해결 함수
def solve():
    matrix=[]
    result=[]
    for _ in range(3):  # 10개의 행 입력
        row_input = list(map(int, input().split()))
        matrix.append(row_input)
    result.extend(cross(matrix))
    result.extend(row(matrix))
    result.extend(colum(matrix))
    return max(result)
                
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result=solve()
    print(f'#{test_case} {result}')