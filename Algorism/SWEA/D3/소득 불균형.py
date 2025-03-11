T=int(input())
for tc in range(1,T+1):
    result=0
    N= int(input())
    N_li = list(map(int,input().split()))
    for i in range(N):
        if N_li[i]<=sum(N_li)//N:
            result+=1
    print(f'#{tc} {result}')