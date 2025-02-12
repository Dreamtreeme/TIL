T=int(input())
for case in range(1,T+1):
    M1, D1, M2, D2 = list(map(int,input().split()))
    md={}
    n=[4,6,9,11]
    for i in range(1,13):
        if i in n:
            md.update({i:30})
        elif i ==2 :
            md.update({i:28})
        else:
            md.update({i:31})
    
    day1=D1
    day2=D2
    for i in range(1,M1+1):
        if M1==1:
            continue
        day1 += md[i]
    for j in range(1,M2+1):
        day2 += md[j]
    result=day2-day1+1
    
    print(f'#{case} {result}')