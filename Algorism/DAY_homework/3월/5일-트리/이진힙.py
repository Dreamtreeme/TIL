import heapq

def get_ancestors(heap):
    if not heap:
        return []
    
    ancestors = []
    index = len(heap) - 1  # 마지막 노드의 인덱스
    
    while index > 0:
        parent_index = (index - 1) // 2
        ancestors.append(heap[parent_index])
        index = parent_index
    
    return ancestors

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    heaplist = list(map(int, input().split()))
    min_heap = []
    for num in heaplist:
        heapq.heappush(min_heap, num)
    # 조상 노드 구하기
    ancestors = get_ancestors(min_heap)
    
    # 조상 노드의 합 계산
    result = sum(ancestors)
    
    print(f'#{tc} {result}')