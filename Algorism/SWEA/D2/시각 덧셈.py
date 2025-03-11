# 시 분으로 이루어진 시각 2개를 입력
# 더한 값을 시 분으로 출력하는 프로그램
# 시간은 12시간제로 표시
#입력
#T
#2month day 1month day

T= int(input())
for case in range(1,T+1):
    rh, rm, hh, hm = list(map(int,input().split()))
    hour= (rh+hh+((rm+hm)//60))%12
    minute = (rm+hm)%60

    print(f'#{case} {hour} {minute}')