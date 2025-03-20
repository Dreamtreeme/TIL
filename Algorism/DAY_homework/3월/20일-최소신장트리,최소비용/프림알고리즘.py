#Prim

# 특정 정점 기준으로 시작
# 갈 수 있는 노드들 중 가중치가 가장 작은 노드부터 고르자
# 그냥 큐가 아닌, 우선순위 큐를 활용하면 좋다.

import heapq

def prim(start_node):
    pq = [(0,start_node)] # 시작점은 가중치가 0이다.
    MST = [0] * V # visited랑 동일하다
    min_weight = 0 # 최소비용 저장

    while pq:
        weight , node = heapq.heappop(pq)

        # 이미 방문한 노드를 뽑았다면 continue
        if MST[node]:
            continue
        MST[node] =1 # 방문처리
        min_weight +=weight # 누적합 추가
        # 처리
        for next_node in range(V):
            # 갈 수 없으면 pass
            if graph[node][next_node] ==0:
                continue
            # 이미 방문했으면
            if MST[next_node]:
                continue

            heapq.heappush(pq,(graph[node][next_node], next_node))

    return min_weight

V,E = 7, 11
graph = [[0]* V for _ in range(V)] # 인접행렬 # 선택과제 인접리스트로

for _ in range(E):
    u,v,w=map(int, input().split())
    graph[u][v] = w
    graph[v][u] = w

result = prim(0)

print(f'최소비용 = {result}')