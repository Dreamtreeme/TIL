def recur(cnt,sumnum):
    global result
    if sumnum ==K:
        result +=1
        return
    if cnt==N:
        return
    
    recur(cnt+1, sumnum+arr[cnt])
    recur(cnt+1, sumnum)
T=int(input())
for tc in range(1, T+1):
    result=0
    N, K = map(int, input().split())
    arr = list(map(int,input().split()))
    recur(0,0)
    print(f'#{tc} {result}')