# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만드려고 한다.

# 사용할 수 있는 연산이 +1,-1,*2,-10 라고할때 최소 몇번 연산해야하는가
# N이 M이 되기위해서 최소연산 구하기

# 예를 들어 N=2 , M=7인경우 (2+1)*2+1 이므로 최소 3번의 연산이 필요

"""
풀이방법
M이 최대 1000000까지니 최악의 경우 N=1일때 999999번해야함
당연히 dfs론 안됨. 결국 현재지점에서 4번의 연산결과를 비교하고 가장 근사치에 가까운 연산을 고름 dp로 풀면 dp1000000 을 만들고
1에 각 계산치 넣어놈
그중 M의 차이가 가장 적게 나는 놈을 고름

틀림
bfs를 사용했어야함
1. 깊이를 모르니 dfs불가
2. 100만 정도면 dfs가능

"""
from collections import deque

def bfs(N,M):
    # 큐 만들기
    queue = deque([(N,0)])
    # 방문기록- 이미 나왔던 결과로 돌아가지 않기위해
    visited = set([N])

    while queue:
        current, depth = queue.popleft()

        if current == M:
            return depth
        
        next_nums = [current+1,current-1,current*2,current-10]

        for num in next_nums:
            if num not in visited:
                visited.add(num)
                queue.append((num, depth+1))

T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    cnt=0
    cnt = bfs(N,M)
             

    print(f'#{tc} {cnt}')

