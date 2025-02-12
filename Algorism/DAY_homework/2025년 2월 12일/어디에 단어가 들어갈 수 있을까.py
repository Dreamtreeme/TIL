T=int(input())
for case in range(1, T+1):
    result=0
    N, K = list(map(int, input().split()))
    matrix=[]
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    for i in range(N):
        counter=0
        counter_li=[]
        for j in range(N):
            if matrix[i][j] == 0:
                if counter!=0:
                    counter_li.append(counter)
                counter = 0
            else:
                counter+=1
        if counter > 0: # 수정: 외부 for문 끝난 후 조건 검사
            counter_li.append(counter)
        for i in counter_li:
            if K ==i:
                result += 1
    row_result=0
    row_result=result
    for k in range(N):
        counter = 0
        counter_li = []
        for l in range(N):
            if matrix[l][k] == 0:
                if counter != 0:
                    counter_li.append(counter)
                counter = 0
            else:
                counter += 1
        if counter > 0: # 수정: 외부 for문 끝난 후 조건 검사
            counter_li.append(counter)
        for i in counter_li:
            if K ==i:
                result += 1
    print(f"#{case} {result}")