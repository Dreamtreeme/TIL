T=int(input())
for case in range(1, T+1):
    N= int(input())
    li = list(map(int,input().split()))
    mx=0
    mi=1000000
    for i in range(N):
        if mx<li[i]:
            mx=li[i]
        if mi>li[i]:
            mi=li[i]
    result=mx-mi
    print(f"#{case} {result}") 