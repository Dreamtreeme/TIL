T = int(input())
for case in range(1,T+1):
    result=0
    N, M = map(int, input().split())
    num_li=list(map(int,input().split()))
    sum_li=[]
    for i in range(N-M+1):
        sum_li.append(sum(num_li[i:i+M]))
    result = max(sum_li)-min(sum_li)
    print(f'#{case} {result}')