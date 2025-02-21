T = int(input())

for test_case in range(1, T + 1):

    N, K = list(map(int,input().split()))
    # 총점 =중간고사35퍼+기말고사45퍼+과제20퍼
    # 평점 N/10 명 동일평점
    total_list=[]
    for i in range(N):
        mid, end, hw = map(int, input().split())
        total = (mid*0.35)+(end*0.45)+(hw*0.2)
        if i+1==K:
            answer= total,i
        total_list.append(total)
        li2 = total_list.copy()
        sorted(li2)
        li2.reverse()
        t= N//10
        A2=li2[t]
        A1=li2[2*t]
        A0=li2[3*t]
        if answer>A2:
            result = 'A+'
            break
        elif answer>A1:   
            result = 'A0'
            break
        elif answer>A0:   
            result = 'A-'
            break



    print(f'#{test_case} {result}')