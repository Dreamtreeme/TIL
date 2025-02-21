# N은 오는사람 숫자
# M은 붕어빵제작시간
# K는 붕어빵 갯수

T = int(input())
for case in range(1, T+1):
    p='Possible'
    N, M, K = list(map(int,input().split()))
    N_list= list(map(int, input().split()))
    N_list.sort() # 오는 사람 시간 오름차순 변경
    bread=0
    if N_list[0]==0:
        print(f'#{case} Impossible')
        continue
     #손님마다 확인
    for i in range(1,N_list[-1]+1): #맨 나중 사람 초만큼 시간흐름
            #시간당 붕어빵의 갯수
        
        if i%M ==0: # 붕어빵이 만들어지면
            bread +=K # 굳이 수식쓰지말고 누적하자
        
        for j in N_list:
            if j == i: # 손님 도착시간이 되면
                bread-=1 # 빵 한개줌
            #다음 손님 왔을떄
        if bread<0: #빵이 없었다면
            p = "Impossible"
    print(f'#{case} {p}')

####
T = int(input()) # 테스트 케이스 수

for tc in range(1, T+1):
    N, M, K = list(map(int, input().split()))
    # N : 사람 수
    # M : M초마다
    # K : K개 빵을 생산
    times = list(map(int, input().split())) # N명의 사람의 도착 시간간


    # 매 초마다 사람의 수를 세는 카운팅 배열
    cnt = [0] * 11_112 # 0초 ~ 11_111초
    # cnt[t] : t초에 도착하는 사람의 수

    # 사람의 수 세기
    for time in times:
        cnt[time] += 1
    
    # 0초부터 11_111초까지 시뮬레이션
    # - M초마다 빵 생산
    # - 해당 t초에 도착하는 사람 수(cnt[t]) 만큼 재고에서 빼준다.
    #   - 만약 재고가 부족하면 Impossible
    # 시뮬레이션이 무리없이 끝나면 Possible

    ans = "Possible" # 일단 가능하다고 가정.
    breads = 0 # 빵 재고량
    for t in range(0, 11_112): # t = 0 ~ 11_111초까지 시뮬레이션
        if t != 0 and t % M == 0: # 0초가 아니면서 M초의 배수가 될 때마다
            breads += K # 재고가 K 만큼 증가
        if cnt[t] > breads: # 만약 사람 수가 재고보다 많다면
            ans = "Impossible" # 불가능
            break # for문 종료
        # 여기까지 왔다는 것은 재고 충분하다는 뜻
        breads -= cnt[t] # t초에 도착한 사람들에게 빵 나눠주기
    
    print(f"#{tc} {ans}")


