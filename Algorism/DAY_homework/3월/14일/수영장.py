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