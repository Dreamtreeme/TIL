def bfs(s, V,V1): # 시작정점 s, 마지막 정점 V
    visited = [0] * (V1+1) # 방문지점 생성
    q = []                # 큐 생성
    q.append(s)           # 시작점 인큐
    visited[s] = 1        # 시작점 방문표시
    while q:              # 큐가 비워질 때 까지 반복, front != rear
        t = q.pop(0)# 디큐해서 t에저장
        
        for w in adj_l[t]:
            if visited[w] ==0: # t에 인접한 정점 w 중, 인큐되지 않은 정점이 있으면
                q.append(w) # 인큐, 인큐 표시
                visited[w] = visited[t]+1
                if w ==V:
                    return visited[w]-1
    return 0

T=int(input())
for tc in range(1, T+1):
    V, E= map(int, input().split()) #V개의 노드 개수와 방향성이 없는 E
    adj_l = [[]for _ in range(V+1)]
    edge_l=[]
    for _ in range(E):
        v1,v2 = map(int, input().split())
        edge_l.append((v1,v2))
    S,G = map(int, input().split()) #출발 노드 S와 도착 노드 G
    for v1,v2 in edge_l:
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)  
    ans =bfs(S,G,V)
    print(f'#{tc} {ans}')