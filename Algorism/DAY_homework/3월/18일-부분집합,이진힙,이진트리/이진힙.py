import heapq

arr = [20, 15, 19, 4, 13, 11]

## 1. 기본 리스트를 heap으로 만들기
# heapq.heapify(arr) # 최소힙으로 바뀐다.
# # 디버깅 시에 이진 트리로 그림을 그려야한다!
# # 정렬이 안된것 처럼 보임
# print(arr)


# 2. 하나씩 데이터를 추가
min_heap = []
for num in arr:
    heapq.heappush(min_heap,num)
print(min_heap)

# 최대힙만들기
max_heap = []
for num in arr:
    heapq.heappush(max_heap,-num) # 일단 음수로넣음

while max_heap:
    pop_num = heapq.heappop(max_heap)
    # 나올때 양수로 바꿈
    print(-pop_num, end=' ')
