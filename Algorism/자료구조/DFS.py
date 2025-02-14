'''
노드갯수, 이어진 선 수
7 8
그래프 인접 연결 정보
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(v, N):
    visited = [0]*(N+1)
    stack = []

    while True:
        if visited[v] == 0:
            visited[v] = 1
            print(v)
        for w in adj_list[v]:   # v에 인접하고 방문안한 w가 있으면
            if visited[w] == 0:
                stack.append(v) # 현재 정점 push
                v = w
                break
        else:
            if stack:
                v= stack.pop()
            else:
                break # while True
V, E = map(int, input().split())
graph = list(map(int, input().split()))
adj_list= [[] for _ in  range(V+1)]

for i in range(E):
    # 인접 연결정보 건너뛰며 읽기
    v, w = graph[i*2], graph[i*2+1] 

    adj_list[v].append(w)
    adj_list[w].append(v)
    # 각 노드(행)마다 인접한 노드 번호 저장

dfs(1,V)
