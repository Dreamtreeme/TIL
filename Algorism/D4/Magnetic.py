#1. n 극은 밑에 s극은 위에뭐 다른거 있나 확인
#2. 위나 밑 둘다없으면 없어짐.
#3. 있다면 그게 n,s인지 확인 
T=10
for tc in range(1, T+1):
    result=0
    input()
    m = [list(map(int,input().split())) for _ in range(100)]

    # n극붙는 자석 제거
    for i in range(100):
        q=[]
        for j in range(100):
            if m[j][i]==1:
                q.append(1)
            elif m[j][i]==2:
                q.append(2)
        if len(q)==1:


    print(f'#{tc} {result}')
