#가로세로 9*9
# 안에 3*3 스토쿠가 9개 배치

T = int(input())

for test_case in range(1, T + 1):
    li =[[0]*9 for _ in range(9)]
    chk_li=[0]*10
    result =1
    inli=[[0]*3 for _ in range(3)]
    for i in range(9):
    # 입력 한줄씩 받기
        N= list(map(int, input().split()))
        chk_li[N[i]] += 1
        if chk_li[i+1] != 1:
            result = 0
            break
        else:
            chk_li =[0]*10
        
        col_li = li.copy()
        for j in range(9):
            li[i][j] = N[j]
            col_li[i][j] = li[j][i]
            chk_li[col_li[i][j]] += 1
        if chk_li[i+1] != 1:
            result = 0
            break
        else:
            chk_li =[0]*10
    for k in range(1,4):
        for l in range(1,4):
            m=(k-1)*3
            n=(l-1)*3
            chk_li[inli[k-1][l-1]] +=1
            if chk_li[i] != 1:
                result = 0
                break
    

    print(f'#{test_case} {result}')

