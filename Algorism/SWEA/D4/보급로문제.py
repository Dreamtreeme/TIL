# 100*100이라 경우의 수가 너무많다
# dp를 활용해 한칸씩 더하면서 가는 방법도있다

# 다익스트라 알고리즘으로 구현

# 힙큐라는 자료구조 사용
import heapq
dy = [1,-1,0,0]
dx = [0,0,1,-1]

# 함수만들기
def dijkstra(sy,sx,gy,gx,board,N):
  hq=[]
  heapq.heappush(hq, (0,sy,sx)) # 우선순위가 낮은 순부터 튀어나옴
  visited=[[0]*N for _ in range(N)]
  visited[sy][sx] = 1

  while hq:
    weight, ty, tx = heapq.heappop(hq)
    if ty ==gy and tx == gx: #골인하면 리턴
      return weight
    
    for i in range(4):
      ny = ty + dy[i]
      nx = tx + dx[i]
      if ny <0 or nx <0 or ny >=N or nx >=N:
        continue
      if visited[ny][nx]==1:
        continue
      visited[ny][nx]=1
      heapq.heappush(hq, (weight + board[ny][nx], ny, nx))

# 입력값부터 넣어보기
T = int(input())

for tc in range(1,T+1):
  N = int(input())
  board = [list(map(int,input()))for _ in range(N)]
  result = dijkstra(0,0,N-1,N-1,board,N)
  print(f'#{tc} {result}')
