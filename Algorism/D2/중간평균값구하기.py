
T=int(input())
for tc in range(1, T+1):
    N= list(map(int,input().split()))
    result = round((sum(N)-(max(N)+min(N)))/(len(N)-2))
    print(f'#{tc} {result}')