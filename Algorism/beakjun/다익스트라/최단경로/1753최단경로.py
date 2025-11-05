
import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(graph, start, vertex_count):
    distances = [INF] * (vertex_count + 1)
    distances[start] = 0
    priority_queue = [(0, start)]  # (거리, 정점)
    
    while priority_queue:
        current_dist, current_node = heapq.heappop(priority_queue)
        
        # 이미 처리된 정점이면 스킵
        if distances[current_node] < current_dist:
            continue
        
        # 인접 정점들 확인
        for next_node, weight in graph[current_node]:
            new_dist = current_dist + weight
            
            # 더 짧은 경로 발견시 갱신
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(priority_queue, (new_dist, next_node))
    
    return distances

# 입력
V, E = map(int, input().split())
start_vertex = int(input())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(V + 1)]

# 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 실행
distances = dijkstra(graph, start_vertex, V)

# 결과 출력
for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])

