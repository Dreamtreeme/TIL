T=int(input())
for case in range(1, T+1):
    N= int(input())
    start=[0]*(N+1)
    end=[0]*(N+1)
    for i in range(1,N+1):
        start[i],end[i] = list(map(int,input().split()))
    P= int(input())
    stations=[] 
    results=[0] * P 
    for _ in range(P): 
        stations.append(int(input()))

    for j in range(P): 
        for k in range(1, N+1): 
            if start[k]<=stations[j]<=end[k]: 
                results[j]+=1

    results_str = " ".join(map(str,results)) 
    print(f"#{case} {results_str}")