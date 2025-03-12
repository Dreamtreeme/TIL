# 배터리 사용량 표가 주어짐
# 모든 구역을 방문해야함


T = int(input())

def perm(idx, cost):
    global visited, out, N, min_cost, adj
    if idx == N:
        
        cost += adj[out[N-1]][out[0]] 
        min_cost = min(min_cost, cost)
        return

    if cost >= min_cost:
        return

    for i in range(1, N):
        if not visited[i]:
            visited[i] = True
            out[idx] = i
            perm(idx+1, cost + adj[out[idx-1]][i])
           
            visited[i] = False

for tc in range(1, T+1):
    N = int(input()) 
    adj = [list(map(int, input().split())) for _ in range(N)] #

    visited = [False] * N 
    out = [0] * N 
    visited[0] = True
    out[0] = 0
    min_cost = 2**31 
    perm(1, 0)

    print(f"#{tc} {min_cost}")
