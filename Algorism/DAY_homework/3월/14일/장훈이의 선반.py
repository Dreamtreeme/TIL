T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    min_sum = float('inf')
    for i in range(1<<N):
        subset=[]
        total=0
        for idx in range(N):
            if i & (1<<idx):
                subset.append(arr[idx])
                total+= arr[idx]
        if total >=M:
            min_sum=min(min_sum,total)

        
    print(f'#{tc} {min_sum-M}')