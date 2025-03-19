T= int(input())
for tc in range(1, T+1):
    N = int(input())
    scadule=[]
    for _ in range(N):
        s,e = map(int, input().split())
        scadule.append((s,e))
    scadule.sort(key=lambda x:x[1])
    time =0
    cnt=0
    for i in range(N):
        if time>=24:
            break
        if scadule[i][0]>=time:
            time=scadule[i][1]
            cnt+=1
        
    print(f'#{tc} {cnt}')