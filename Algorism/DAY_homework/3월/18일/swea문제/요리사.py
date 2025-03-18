def calculate_taste(group):
    taste = 0
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            taste += arr[group[i]][group[j]] + arr[group[j]][group[i]]
    return taste

def dfs(cnt, start, selected):
    global result
    if cnt == N // 2:  # A 요리에 N/2개의 식재료가 선택됨
        A = [i for i in range(N) if selected[i]]  # A 요리
        B = [i for i in range(N) if not selected[i]]  # B 요리
        taste_A = calculate_taste(A)
        taste_B = calculate_taste(B)
        diff = abs(taste_A - taste_B)
        result = min(result, diff)
        return

    for i in range(start, N):  
        if not selected[i]:
            selected[i] = True
            dfs(cnt + 1, i + 1, selected)
            selected[i] = False

# 입력 처리 및 실행
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  
    arr = [list(map(int, input().split())) for _ in range(N)]  
    result = 2**31  
    selected = [False] * N  # 선택 여부 배열
    dfs(0, 0, selected)  
    print(f'#{tc} {result}')