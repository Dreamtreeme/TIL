T = int(input())
for case in range(1, T+1):
    N= int(input())
    li = list(map(int , input().split()))
    result=0
    for i in range(N-1):
        min_idx=i
        for j in range(i+1, N):
            if li[min_idx]>li[j]:
                min_idx=j
        li[i], li[min_idx] = li[i], li[min_idx]
    result = " ".join(map(str,li))
    print(f"#{case} {result}")