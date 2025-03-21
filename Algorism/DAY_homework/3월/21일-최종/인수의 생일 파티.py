# 오후 3시 11분시작

# N개 집이 있고, 각 집에는 한명의 사람

# 다른집으로 이동이 가능한 단방향 간선, 이동시간이 있음(가중치,양수)

# 모든 집들 간에 이동이 가능(완전그래프)

# 인수의 집은 X번

# 각 사람들은 자신의 집에서 X번 집으로 오는데 최단 시간으로 이동

# 각 사람들이 인수집까지 왔다가 자신집으로 돌아가는 시간중 최대를 구하라

# 결국 다익스트라를 써야함(단방향,한집에서 다른집으로 향하는 최소시간)

import heapq

def daijkstra(start,end):
    pq = [(0,start)]
    times = [21e8]*(N+1) # 각 정점까지의 최단시간 저장
    times[start] = 0 # 시작노드 최단시간


    while pq: # 우선순위 큐가 존재하면
        current_time, node = heapq.heappop(pq) # 현재시간과 노드를 뱉어라
        if end == node: # 만약 끝지점에 도달했으면
            return current_time # 누적시간을 리턴
        if times[node] < current_time: # 최소시간이 현재시간보다 작다면 굳이 또 할 필요가없음
            continue

        for next_info in graph[node]: # 노드리스트에 저장된 여러 간선정보
            next_time = next_info[0]
            next_node = next_info[1]

            new_time = current_time + next_time # 현재 누적시간에 다음 가중치 더해줌

            if new_time>= times[next_node]: # 만약 새로운 시간이 이미 저장된 시간보다 크면
                continue
            times[next_node] = new_time
            heapq.heappush(pq,(new_time,next_node))



T= int(input())
for tc in range(1,T+1):
    N,M,X = map(int,input().split()) # N 노드의 갯수, M간선의 갯수, X, 인수의 집
    graph = [ [] for _ in range(N+1)] # 노드번호는1번부터 N번까지 만듦
    for _ in range(M):
        s, e, w = map(int,input().split())
        graph[s].append((w,e))
    result = 0
    for i in range(1,N+1): # 모든 집에서 인수집까지, 그리고 인수집에서 모든 집까지 거리 구하기
        go_cost = daijkstra(i,X) # i번부터 X까지
        come_cost = daijkstra(X,i) # X번부터 i까지
        if (go_cost+come_cost)>result:
            result = (go_cost+come_cost)

    print(f'#{tc} {result}')