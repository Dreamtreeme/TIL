T = int(input())
for case in range(1,T+1):
    result=0
    N= int(input())
    L = 0 # 현재위치
    ts = 0 # 현재 차의 속도
    for i in range(N):
        GS = list(map(int, input().split()))
        if GS[0]==1: # 가속일때
            ts+=GS[1]
        elif GS[0]==2: # 감속일때
            if (ts-GS[1])<0:
                ts=0
            if ts!=0:
                ts-=GS[1]
        L+=ts
    result = L

    print(f'#{case} {result}')