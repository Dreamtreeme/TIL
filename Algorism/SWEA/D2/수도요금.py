# A사 1리터당 요금 P
# B사 기본요금 Q
# B사 종량리터 R
# B사 1리터 요금 S
# 한달 사용 리터 W

T=int(input())
for case in range(1,T+1):
    
    P, Q, R, S, W = list(map(int, input().split()))
    # A사 선택시 요금
    A_cost=P*W
    # B사 선택시 요금
    B_cost= Q if W<R else Q+(S*(R-W))
    if A_cost>B_cost:
        result=B_cost
    else:
        result=A_cost
    print(f'#{case} {result}')