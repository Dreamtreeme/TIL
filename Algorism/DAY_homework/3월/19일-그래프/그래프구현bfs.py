# bfs는 정점부터 인접 노드들을 모두 방문한 후 다음 노드로 넘어감

def bfs(start_node):
    q= [start_node] # 시작점 넣은 상태로 출발
    # q에 들어가는 노드들의 의미: 다음에 방문해야할 대기열
    while q:
    # 1. 가장 앞에 있는 노드를 뽑느다.
    # 2. 해당 노드에서 갈 수 있는 노드들을 큐에 넣는다.
        now = q.pop(0)

        print(now, end=" ")
        for next_node in graph[now]:
            # 이미 방문했다면 가지마라
            if visited[next_node]:
                continue
            visited[next_node] =1
            bfs(next_node)


N,M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)] # 인접행렬(N*N 의 배열)
# 인접 리스트
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e) # 방향이 존재한다면 여기서 끝
    graph[e].append(s) # 양방향이라면 뒤집어서 저장해줘야함

visited = [0]*(N+1)
visited[1] =1
bfs(1)