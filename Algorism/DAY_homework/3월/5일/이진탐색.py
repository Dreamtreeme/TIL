def fill_tree(node, value):
        if node > N:
            return value
        
        # 왼쪽 서브트리
        value = fill_tree(node * 2, value)
        
        # 현재 노드에 값 배치
        tree[node] = value
        value += 1
        
        # 오른쪽 서브트리
        value = fill_tree(node * 2 + 1, value)
        
        return value

T=int(input())
for tc in range(1, T+1):
    N= int(input())
    
   # N+1 크기의 배열 생성 (인덱스 1부터 사용)
    tree = [0] * (N + 1)
    
    # 1부터 시작하여 트리 채우기
    fill_tree(1, 1)
    
    root_value = tree[1]
    half_node_value = tree[N // 2]
    

    print(f'#{tc} {root_value} {half_node_value}')