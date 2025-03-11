T=int(input())
for tc in range(1,T+1):
    result = 0
    max_num=0
    input()
    N = list(map(int, input().split()))
    C = [0]*1000
    for num in N:
        C[num]+=1
    for i in range(len(C)):
        if max_num<=C[i]:
            max_num=C[i]
            result=i
    
    print(f'#{tc} {result}')