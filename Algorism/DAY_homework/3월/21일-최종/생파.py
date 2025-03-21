import heapq

# 다익스트라 함수: 시작점에서 모든 노드까지의 최단 경로 배열 반환
def daijkstra(start, graph):
    pq = [(0, start)]
    times = [21e8] * (N + 1)  # 각 정점까지의 최단 시간 저장
    times[start] = 0  # 시작 노드의 최단 시간

    while pq:
        current_time, node = heapq.heappop(pq)
        if times[node] < current_time:  # 이미 더 짧은 경로가 있다면 스킵
            continue
        for next_time, next_node in graph[node]:  # 다음 노드와 가중치
            new_time = current_time + next_time
            if new_time < times[next_node]:  # 더 짧은 경로 발견 시 갱신
                times[next_node] = new_time
                heapq.heappush(pq, (new_time, next_node))
    return times  # 모든 노드까지의 최단 시간 배열 반환

# 입력 및 처리
T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())  # 노드 수, 간선 수, 인수 집
    graph = [[] for _ in range(N + 1)]  # 정방향 그래프
    rev_graph = [[] for _ in range(N + 1)]  # 역방향 그래프

    # 그래프 생성
    for _ in range(M):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))  # 정방향: s -> e
        rev_graph[e].append((w, s))  # 역방향: e -> s

    # X에서 모든 집으로 가는 최단 경로 (정방향 그래프)
    come_cost = daijkstra(X, graph)
    # 모든 집에서 X로 오는 최단 경로 (역방향 그래프)
    go_cost = daijkstra(X, rev_graph)

    # 왕복 시간 계산 및 최대값 찾기
    result = 0
    for i in range(1, N + 1):
            total_cost = go_cost[i] + come_cost[i]
            result = max(result,total_cost)

    print(f'#{tc} {result}')


#     back = dijkstra(X, adj): 정방향 그래프를 사용
# go = dijkstra(X, rev_adj): 역방향 그래프를 사용
# 각 호출이 반환하는 distance 배열의 의미를 증명
# (1) back = dijkstra(X, adj)
# 그래프: adj (정방향 그래프)
# 시작 노드: X
# 의미: 노드 X에서 출발하여 정방향 간선(x → y)을 따라 각 노드까지의 최단 경로를 계산
# 결과: back[i]는 X에서 i로 가는 최단 거리, 즉 X → i의 최단 경로 길이
# (2) go = dijkstra(X, rev_adj)
# 그래프: rev_adj (역방향 그래프)
# 시작 노드: X
# 의미: 노드 X에서 출발하여 역방향 간선(y → x)을 따라 각 노드까지의 최단 경로를 계산
# 핵심: 역방향 그래프에서 X에서 i로의 경로는 정방향 그래프에서 i에서 X로의 경로와 동일
# 예: 역방향 그래프에서 X → a → b → i 경로가 존재한다면, 이는 정방향 그래프에서 i → b → a → X 경로가 존재함을 의미
# 가중치 방향성은 유지되므로, 역방향 그래프에서 X에서 i로의 최단 거리는 정방향 그래프에서 i에서 X로의 최단 거리와 같음
# 결과: go[i]는 역방향 그래프에서 X에서 i로의 최단 거리, 즉 정방향 그래프에서 i → X의 최단 경로 길이