import heapq
dr = [1,-1,0,0]
dc = [0,0,1,-1]


def dijkstra():
  global visited, N, board
  hq = []
  heapq.heappush(hq,(board[0][0], 0 , 0))
  
  while hq:
    weight, r, c = heapq.heappop(hq)

    if r==N-1 and c==N-1:
      return weight
    
    
    for k in range(4):
      nr = r+dr[k]
      nc = c+dc[k]
      if not (0<=nr<N) or not (0<=nc<N):
        continue
      if visited[nr][nc]:
        continue
      visited[nr][nc]=1
      heapq.heappush(hq, (board[nr][nc]+weight, nr, nc))

# 입력값부터 넣어보기
T = int(input())

for tc in range(1,T+1):
  N = int(input())
  board = [list(map(int,input()))for _ in range(N)]
  visited = [[0]*N for _ in range(N)]
  result = dijkstra()
  print(f'#{tc} {result}')
