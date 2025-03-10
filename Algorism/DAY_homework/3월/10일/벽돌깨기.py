# 벽돌깨기는 dfs랑 bfs를 이용해 푼다
# 처음 벽돌의 갯수를 계산후 현재 쏜 구슬횟수, 현재 벽돌수, 배열을 넘겨준다
# dfs는 트리를 생각하고 마지막에 함수를 호출하면 2번째 트리로 간다고 생각한다.
# bfs는 같은 차수 트리에서 확장되는 개념이라 생각한다. while q를 이용해 같은 차수에서 같은 배열을 이용해 푼다.

T= int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    min_block = 1e9 # 최대값으로 설정
    block=0
    for r in range(H):
        for c in range(W):
            if arr[r][c]: # 블록이 존재하면 추가
                block+=1
    dfs(0, min_block, arr)

    print(f'#{tc} {result}')