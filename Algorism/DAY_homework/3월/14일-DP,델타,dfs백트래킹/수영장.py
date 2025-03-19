# 테스트 케이스 수 입력
T = int(input())

for t in range(1, T + 1):
    # 이용권 가격 입력: [1일권, 1달권, 3달권, 1년권]
    prices = list(map(int, input().split()))
    # 이용 계획 입력: 1~12월 (0월은 0으로 추가)
    plan = [0] + list(map(int, input().split()))  # i-1 인덱스를 위해 0월 추가
    
    # dp[i]: 1월부터 i월까지의 최소 비용
    dp = [0] * 13  # 0월부터 12월까지 (인덱스 0~12)
    
    # 1월부터 12월까지 최소 비용 계산
    for i in range(1, 13):
        # 1일권: 이전 달 최소 비용 + 이번 달 이용일수 * 1일권 가격
        cost1 = dp[i-1] + plan[i] * prices[0]
        # 1달권: 이전 달 최소 비용 + 1달권 가격
        cost2 = dp[i-1] + prices[1]
        # 3달권: 3개월 전 최소 비용 + 3달권 가격
        if i >= 3:
            cost3 = dp[i-3] + prices[2]
        else:
            cost3 = prices[2]  # 3개월 전 데이터가 없으면 3달권 가격만
        
        # 세 옵션 중 최소값 선택
        dp[i] = min(cost1, cost2, cost3)
    
    # 1년권과 비교하여 최종 최소 비용 결정
    result = min(dp[12], prices[3])
    
    # 출력 형식: "#테스트케이스번호 최소비용"
    print(f"#{t} {result}")

# 규칙을 찾아 풀어봤으나 풀리지 않음.
# ai에선 dp활용
# 그리디는 맞는거 같은데;; -> 아니었음. 작은 문제로 나눠서 재활용하는 DP활용
# 이전값들을 이후값이 변경시키지 않는다면 DP고려

# 풀이 생각법
# 1일치 다본다
# 1달이 더 싼 경우는 없나?
# 3달이 더 저렴?
# 1년이 더 저렴? -> 다본다. 완전탐색
# 만약 입력이 주어져야할때 2월 조심, 28일까지 밖에 없음

# level: 12월 
# branch: 4개(1일,1달,3달,1년)
def recur(month, total_cost):
    global min_answer
    if min_answer<total_cost:
        return
    if month >12:
        min_answer = min(min_answer,total_cost)
        return
    
    # 1일 다사는경우
    recur(month+1,total_cost+(days[month]*cost_day))
    # 1달 사는경우
    recur(month+1,total_cost+cost_month)
    # 3달 사는경우
    recur(month+3,total_cost+cost_3month)
    # 1년 사는 경우
    recur(month+12,total_cost+cost_year)


T = int(input())

for tc in range(1, T + 1):
    # 이용권 가격들
    cost_day, cost_month, cost_3month, cost_year =map(int, input().split())
    days = [0] + list(map(int,input().split()))
    min_answer = 2**31
    recur(1,0) # 1월부터 시작
    print(f'#{tc} {min_answer}')


# dp로 푸는법
T = int(input())

for t in range(1, T + 1):
    # 이용권 가격 입력: [1일권, 1달권, 3달권, 1년권]
    prices = list(map(int, input().split()))
    # 이용 계획 입력: 1~12월 (0월은 0으로 추가)
    plan = [0] + list(map(int, input().split()))  # i-1 인덱스를 위해 0월 추가
    
    # dp[i]: 1월부터 i월까지의 최소 비용
    dp = [0] * 13  # 0월부터 12월까지 (인덱스 0~12)

    dp[1] = min(days[1] * cost_day,cost_month)
    dp[2] = dp[1]+ min(days[1] * cost_day,cost_month)
    # 1,2월까지는 직접 넣어줌

    # 3월~12월은 반복계산

    for month in range(3, 13):
        # 3월의 최소 비용 후보
        # 1. N-3월에 3개월 이용권을 구입한 경우
        # 2. 2월의 최소비용 +1일권
        # 3. 2월의 최소비용 + 1달권 구매
        dp[month] = min(dp[month-3] + cost_3month, dp[month-1] + (days[month] * cost_day), dp[month-1] + cost_month)


    # 12월의 누적 최소 금액vs1년권
    answer = min(dp[12], cost_year)
    print(f'#{tc} {answer}')