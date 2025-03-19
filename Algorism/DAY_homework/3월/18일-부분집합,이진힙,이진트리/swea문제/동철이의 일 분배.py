
# N의 크기
# N의 크기가 많이 크다 -> 완전탐색으로 불가능할 수도
# - 완전탐색 + 백트래킹 (많이 줄이지는 못함. 문제 마다 다름)
# - DP
# - 그리디

# 완전탐색 << DP <<<<<<<< 그리디
# DP
# - 최적화 문제
# - 큰 문제의 최적해를 바로 풀기는 어려움
# - 작은 문제의 최적해를 먼저 푼다
# - 작은 문제의 최적해를 조합해서 큰 문제의 최적해를 계산한다
# - dp[N]
# - dp[1], dp[2], dp[3], ...
# - dp[1] + dp[3] => dp[5]
# - dp[N-4] + dp[n-2] or dp[N-3] + dp[n-1] 최소값이 dp[N]
# 


def dfs(employee,percent):
    global result
    if employee==N: # 기저조건으로 깊이를 설정
        if result<percent:
            result = percent # 최소값 갱신
        return
    if percent <= result: 
        return
    
    for case in range(N):
        if select[case]: # 선택한 직원 패스
            continue
        p=percent*(arr[employee][case]/100)
        select[case] =True
        dfs(employee+1,p)
        select[case] =False


T = int(input())
for tc in range(1, T+1):
    result=0
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    select = [False]*N
    dfs(0,1)
    print(f'#{tc} {result*100:.6f}')

# ai 푼 dp+비트마스킹 방법
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    # DP 배열 초기화: 크기 1<<N, dp[0] = 1.0, 나머지 0.0
    dp = [0.0] * (1 << N)
    dp[0] = 1.0
    
    # 모든 가능한 mask에 대해 계산
    for mask in range(1 << N):
        # 현재 mask에 배정된 직원 수 k
        k = bin(mask).count('1')
        # k가 N이면 모든 작업이 배정된 상태이므로 더 이상 갱신 불필요
        # 하지만 mask 순회 방식상 자연스럽게 처리됨
        for j in range(N):
            # 작업 j가 mask에 포함되지 않았는지 확인
            if (mask & (1 << j)) == 0:
                new_mask = mask | (1 << j)
                # 새로운 상태의 최대값 갱신
                dp[new_mask] = max(dp[new_mask], dp[mask] * (arr[k][j] / 100.0))
    
    # 결과: 모든 작업이 배정된 상태의 값에 100을 곱해 백분율로
    result = dp[(1 << N) - 1] * 100
    print(f'#{tc} {result:.6f}')