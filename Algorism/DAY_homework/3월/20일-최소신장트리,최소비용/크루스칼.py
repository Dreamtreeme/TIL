def find_set(x):
    if x == parents[x]:
        return x
    
    # return find_set(parents[x]) # 이렇게 하면 원소수가 많아지면 힘듬
    parents[x] = find_set(parents[x])
    return parents[x]
def union(x,y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y: # 사이클 방지
        return False
    
    # 일정한 규칙으로 연결하자.
    if ref_x < ref_y:
        parents[ref_y] =ref_x
    else:
        parents[ref_x] =ref_y
    return True


V,E = 7, 11

edges = [] #간선정보를 저장

for _ in range(E):
    s,e,w = map(int,input().split())
    edges.append((s,e,w))

edges.sort(key=lambda x: x[2]) #가중치 기준으로 오름차순
parents = [i for i in range(V)] #대표자는 일단 정점들 번호로

# 언제까지? N-1개를 선택할 때 까지
cnt=0
result=0

for u,v,w in edges:
    if union(u,v):
        cnt+=1
        result += w

    if cnt == V-1:
        break

print(result)
