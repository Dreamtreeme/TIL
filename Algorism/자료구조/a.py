T= int(input())
for case in range(1, T+1):
    N,M =list(map(int, input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if N>M:
        A, B, N, M = B, A, M, N
    max_v=0
    
    for i in range(M-N+1):
        result=0
        for j in range(N):
            result +=A[j]*B[i+j]
        if max_v<result:
            max_v=result
    result = max_v
    print(f"#{case} {result}") 