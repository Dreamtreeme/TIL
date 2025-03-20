import heapq

def prim(start_node):
    pq = [(0, start_node)]
    visited = [False] * (V + 1)  
    min_weight = 0      # 3. 우선순위큐에 가중치,시작노드 넣고 방문여부 ,최소변수 설정

    while pq:
        weight, node = heapq.heappop(pq) # 항상 가중치가 낮은 순부터 나옴(최소힙 보장)

        if visited[node]: # 방문여부 확인
            continue

        visited[node] = True
        min_weight += weight # 방문여부 확인후 최소치 더해줌

        for next_w, next_n in graph[node]: # 리스트 안에 있는 모든 간선에 대해 실행
            if not visited[next_n]:
                heapq.heappush(pq, (next_w, next_n)) # 다음 노드번호에 방문하지 않았다면 추가

    return min_weight

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E): #1. 간선의 갯수만큼 실행
        n1, n2, w = map(int, input().split())
        graph[n1].append((w, n2))
        graph[n2].append((w, n1)) # 2. 인접리스트에 양방향으로 추가해줌

    result = prim(0)
    print(f'#{tc} {result}')