"""
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7  노드의 수와 간선의 수가 들어온다
"""

def dfs(node):
    # 보통 그래프 문제들에서
    # K개의 노드 방문했다면 종료
    # N개를 모두 방문했다면 경로출력
    # if 종료시 해야할것들 or 가지치기:
    # return
    print(node, end=" ")

    # 내가 갈수있는 후보들을 모두 확인하면서, 한 군데로 진행
    for next_node in graph[node]:
        # 이미 방문했다면 가지마라
        if visited[next_node]:
            continue
        visited[next_node] =1
        dfs(next_node)
N,M = map(int, input().split())
# 1. 그래프를 저장하기
# - 비어있는 그래프를 생성한다
# - 그래프 정보를 입력받아 넣는다.
graph = [[0]*(N+1) for _ in range(N+1)] # 인접행렬(N*N 의 배열)


# 인접 리스트
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e) # 방향이 존재한다면 여기서 끝
    graph[e].append(s) # 양방향이라면 뒤집어서 저장해줘야함

visited = [0]*(N+1)
visited[1]=1
dfs(1)