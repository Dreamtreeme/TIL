def f(i, N, s, used_cols, arr):  # 함수 파라미터에 used_cols, p, arr 추가
    global min_v
    if i == N:  # 모든 행을 다 선택했을 때
        if min_v > s:
            min_v = s
    elif s >= min_v: # 중간 합계가 최소합보다 크거나 같으면 가지치기 (최소합보다 작아야 가지치기 조건 성립)
        return
    else:
        for j in range(N): # 각 열을 순회 (p 배열 사용 안하고 모든 열 탐색)
            if not used_cols[j]: # j 열이 아직 사용되지 않았으면
                used_cols[j] = True # j 열 사용 표시
                f(i+1, N, s + arr[i][j], used_cols, arr)  
                used_cols[j] = False


T=int(input())
for case in range(1, T+1):
    N = int(input()) 
    arr = [list(map(int, input().split()))for _ in range(N)]
 
    min_v = 10000 
    used_cols = [False] * N # used_cols 배열 초기화: 각 열 사용 여부 추적
    f(0,N, 0, used_cols, arr) 

    print(f"#{case} {min_v}") 