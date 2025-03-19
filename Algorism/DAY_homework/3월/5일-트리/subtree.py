def dfs(node, tree):
    cnt = 1
    for child in tree[node]:
        cnt += dfs(child, tree)
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    # 트리의 크기를 필요한 만큼만 설정 (노드 번호가 가장 큰 값 + 1)
    tree_size = max(arr) + 1  
    tree = [[] for _ in range(tree_size)]  

    # 리스트 인덱싱을 사용하여 O(E)로 트리 구성
    for i in range(E):
        parent = arr[2 * i]
        child = arr[2 * i + 1]
        tree[parent].append(child)

    result = dfs(N, tree)

    print(f'#{tc} {result}')
