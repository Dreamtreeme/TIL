import heapq

def daijkstra(startnode):
    pq = [(0,startnode)] # 처음엔 가중치0
    dists = [21e8] * (V+1) # 각 노드에 대한 누적거리
    dists[startnode] = 0

    while pq:
        dist, node = heapq.heappop(pq)
        if node == V: # 끝 노드에 도달하면 리턴
            return dist

        if dists[node] < dist: # 최소거리가 누적거리보다 높으면 건너뜀
            continue
    
        for next_info in graph[node]:
            next_dist, next_node = next_info[0],next_info[1]

            new_dist = dist + next_dist

            if new_dist > dists[next_node]:
                continue
            dists[next_node] = new_dist

            heapq.heappush(pq, (new_dist, next_node))

    return
T=int(input())
for tc in range(1, T+1):
    V,E = map(int,input().split()) # V:마지막 노드번호,E: 도로갯수
    graph = [[] for _ in range(V+1)] # 노드가 0부터 시작하므로+1

    for _ in range(E):
        n1,n2,w = map(int,input().split())
        graph[n1].append((w,n2)) # 단방향이므로

    result = daijkstra(0)
    print(f'#{tc} {result}')