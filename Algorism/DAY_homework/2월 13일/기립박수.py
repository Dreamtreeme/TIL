T = int(input())

for test_case in range(1, T + 1):
    N= input()
    counter=[]
    needPeople=0
    needPeoples=[]
    for i in range(len(N)):
        counter.append(int(N[i]))
    num=counter[0]
    for idx in range(1,len(N)):
        if num<idx: # 숫자 모잘랄때
            needPeople=idx-num #필요한인원
            needPeoples.append(needPeople) # 담번에 또 필요하니
            num+= needPeople # 담단계 진행을 위해 더함
        num+=counter[idx] # 조건과 상관없이 항상 사람수 기립박수 한다 가정
    result = sum(needPeoples)
    print(f'#{test_case} {result}')