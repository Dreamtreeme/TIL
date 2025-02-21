# 그래프 경로

# 그래프
# -정점과 간선으로 이루어진 자료구조
# - 저장 방법: 1. 인접행렬, 2. 인접리스트, 3. 간선리스트
def find_path(adj, visited, start, end):
    visited[start] = 1  # 시작 노드 방문 표시

    if start == end:  # 현재 노드가 도착 노드와 같으면 경로 존재
        return 1

    # 현재 노드에서 갈 수 있는 다음 노드 탐색
    for next_node in range(1, len(adj)):
        if adj[start][next_node] == 1 and visited[next_node] == 0:
            # 간선이 있고, 방문하지 않은 노드인 경우 재귀 호출
            if find_path(adj, visited, next_node, end) == 1:
                return 1 # 경로가 존재하면 1 반환

    return 0 # 경로가 없으면 0 반환

T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    # V: 정점갯수
    # E: 간선갯수

    # 1. 인접행렬 만들기
    # v*v 크기의 2차원행렬 만들기
    # 1 ~ V 까지의 정점 번호를 사용하려면, 배열의 크기는?
    # V+1의 크기로 만들고 0번 인덱스는 사용하지 않는다
    adj = [[0]*(V+1) for _ in range(V+1)]

    # E개 줄에 걸쳐서 간선이 들어옴
    for _ in range(E):
        v1, v2 = list(map(int, input().split()))
        adj[v1][v2] = 1
        # 무향 그래프라면
        # adj[v2][v1] = 1
    S, G = list(map(int, input().split()))
    # 2. DFS 탐색으로 경로 찾기
    visited = [0] * (V + 1)
    result = find_path(adj, visited, S, G)


    print(f'#{tc} {result}')

    # ## 2.인접리스트
    # # 1차원 리스트가 : v개 있어야함
    # # adj[1] ~ adj[V] 까지 사용
    # adj = [[] for _ in range(V+1)]

    # for _ in range(E):
    #     v1, v2 = list(map(int, input().split()))
    #     adj[v1].append(v2)
    #     # 만약 무향 그래프라면
    #     # adj[v2].append(v1)

    # # 리스트의 딕셔너리로 만들어서 하는 방법
    # # adj[1] ~ adj[V]
    # # adj = {}
    # # for i in range(1, V+1):
    # #     adj[i] = []