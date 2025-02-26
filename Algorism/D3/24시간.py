T=int(input())
for tc in range(1,T+1):
    result=0
    A,B = map(int, input().split())
    result = (A+B)%24
    print(f'#{tc} {result}')