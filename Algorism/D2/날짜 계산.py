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
    day1=0
    day2=0
    
    for i in range(1,M1+1):
        if i== M1:
            day1+=D1
            break
        day1 += md[i]
    for i in range(1,M2+1):
        if i== M2:
            day2+=D2
            break
        day2 += md[i]
    result = day2-day1+1
         
    print(f'#{case} {result}')
