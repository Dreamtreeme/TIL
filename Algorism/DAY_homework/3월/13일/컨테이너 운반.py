# 화물이 실려있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반
# 트럭당 한개의 컨테이너를 운반, 트럭의 적재용량을 초과하는 컨테이너 운반X
# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로
# 최대 M대의 트럭이 편도로 한번만 운행
# 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면
# 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램

# 화물을 싣지 못한 트럭이 있을 수 도 있고, 남는 화물이 있을 수 도 있다.
# 컨테이너를 한개도 옮길 수 없는 경우 0을 출력

#테스트케이스 50개, 컨테이너수,트럭수 최대 100개, 적재용량 최대 50톤

T = int(input())
for tc in range(1,T+1):
    N , M = map(int,input().split())
    W=list(map(int,input().split()))
    T=list(map(int,input().split()))

    T.sort()
    W.sort() # 각 화물별 트럭별 오름차순 정렬
    select = [] # 선택된 화물 인덱스 번호 모음
    result=0
    for i in range(M): # 트럭마다
        con = 0
        for j in range(N) : # 컨테이너의 화물 크기를 재봄
              
            if j in select: # 전에 선택되었으면 점프
                continue
            if T[i]>=W[j] : # 만약 화물적재량을 만족하면
                con = (W[j],j) # 계속갱신
                continue
        if con==0: # 적재량을 만족하는 화물이 없다면
            continue
        # 만족하는 화물이 있다면
        select.append(con[1]) # 화물 인덱스 번호 추가
        result +=con[0]
        
    print(f'#{tc} {result}')