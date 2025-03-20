
def kruskal(node):
    def find_set(x):
        if x == parents[x]:
            return x
        
        parents[x] = find_set(parents[x])
        return parents[x]
    def union(x,y):
        ref_x = find_set(x)
        ref_y = find_set(y)

        if ref_x == ref_y:
            return
        
        if ref_x<ref_y:
            parents[ref_y] = ref_x
        else:
            parents[ref_x] = ref_y
    # 총 해저터널의 갯수는 N(N-1)/2 임
    # 왜냐하면 첫번째에서 n-1개 두번째에서 n-2개...마지막 섬에선 1개만 안겹치는 경로이기 때문
    edges=[]
    for start_node in range(N):
        for end_node in range(start_node+1,N):
            eco_fee = E*(((X_list[end_node]-X_list[start_node])**2)+((Y_list[end_node]-Y_list[start_node])**2))
            edges.append((start_node,end_node,eco_fee))
    
    # 환경부담금 순으로 정렬
    edges.sort(key=lambda x : x[2])

    parents = [i for i in range(N)] # 각 노드번호 대표자 설정

    tunel=0
    result=0
    for s,e,eco_fee in edges:# 순번대로 나오는 환경부담금은 오름차순으로 정렬되었기 때문에 최소 비용부터 나옴
        if find_set(s) != find_set(e):# 아직 해저터널이 연결 안되있을때 최소비용으로 건설할 수 있는 섬과 섬을 연결
            union(s,e)
            tunel+=1
            result+=eco_fee
        if tunel == N-1: # 터널이 섬갯수-1이면 최소 터널 완공
            break
    result =int(round(result,0)) # 소수점 첫째짜리에서 반올림하고 정수형으로 바꿈
    return result

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    X_list = list(map(int,input().split()))
    Y_list = list(map(int,input().split()))
    E = float(input())
    result = kruskal(N)
    print(f'#{tc} {result}')