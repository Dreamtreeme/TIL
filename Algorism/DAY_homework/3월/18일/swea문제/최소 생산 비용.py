# A사는 여러 곳에 공장을 갖고 있다. 봄부터 새로 생산되는 N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려고 한다.

# 각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램을 만드시오.

# 예를 들어 3개의 제품을 생산하려는 경우 각 공장별 생산비용은 다음과 같이 주어진다..
'''
[제품1:[공장A:73, 공장B:21 공장C:21]
제품2:[공장A:11, 공장B:59 공장C:40]
제품3:[공장A:24, 공장B:31 공장C:83]
]
'''
# 이때 1-C, 2-A, 3-B로 제품별 생산 공장을 정하면 생산 비용이 21+11+31=63으로 최소가 된다.


# 풀이
# N종 제품을 깊이로 설정
# 깊이 만큼 들어갈때 총합을 구해놓고 최소값갱신
# 갱신된 최대보다 크면 실행 X

def dfs(row,cost):
    global result
    if row==N: # 기저조건으로 깊이를 설정
        if result>cost:
            result = cost # 최소값 갱신
        return
    
    for i in range(N):
        if select[i]: # 선택한 공장 패스
            continue
        if (cost + arr[row][i])>=result: # 이미 구한 총합보다 크면 가지치기
            continue
        select[i] =True
        dfs(row+1,cost + arr[row][i])
        select[i] =False


T = int(input())
for tc in range(1, T+1):
    result=2**31
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    select = [False]*N
    dfs(0,0)
    print(f'#{tc} {result}')