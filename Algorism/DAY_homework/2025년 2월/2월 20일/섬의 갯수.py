def bfs(r,c,h,w):
    #섬 조건
    dr=[-1,-1,0,1,1,1,0,-1] # 12시부터 시계방향
    dc=[0,1,1,1,0,-1,-1,-1]
    q=[]
    
    for k in range(8):
        nr, nc = r+dr[k],c+dc[k]
        if 0<=nr<h and 0<=nc<w :
            q.append()
            visited[nr][nc]=True
            if earth[nr][nc]==1:
                bfs(nr,nc,h,w)
result = 0
while True:
    w,h = map(int, input().split())
    if w==0 and h==0:
        break
    earth =[]
    for _ in range(h):
        earth.append(list(map(int, input().split())))
    for r in range(h):
        visited = [[False]*h for _ in range(w)]
        for c in range(w):
            if earth[r][c]==1 and visited[r][c]!=True:
                result+=1
                bfs(r,c,h,w)
        
print(result)

