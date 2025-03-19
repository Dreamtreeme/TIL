# 6개의 원소 1~6이 존재하는경우
# 1. 각 집합을 만들어주는 함수
def make_set(n):
    # 1~n 까지의 원소가 있다고 가정 -> 총 n개의 집합을 생성
    # 각 원소의 부모를 자신으로 초기화
    parents = [i for i in range(N+1)]
    ranks = [0] * (n+1) # rank를 0으로 초기화
    return parents, ranks

# # 경로 압축추가
# def find_set(x):
#     if parents[x] == x:
#         return x
#     # 경로 압축 path compression 을 통해
#     # x의 부모를 대표자로 변경
#     parents[x] = find_set(parents[x]) # 대표자를 찾아오는 재귀호출
#     return parents[x]

# 할때마다, 모든 노드의 대표자를 변경
def find_set(x):
    while parents[x] != x:
        parents[x] = find_set(parents[x]) # 대표자를 찾아오는 재귀호출
        x = parents[x]
    return parents[x]
def union(x,y): # union은 대표자들 검색이 우선
    # 대표자들끼리 병합
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면?
    if ref_x == ref_y:
        return #끝
    
    # 다른 집합이라면 합친다.
    # 문제에 따라 우선되는 집합으로 합쳐줌
    # if ref_x < ref_y:
    #     parents[ref_y] = ref_x
    # else:
    #     parents[ref_x] = ref_y
    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        # rank 가 같으면 한 쪽으로 병합하고, 대표자의 rank 증가
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


N = 6
parents, ranks = make_set(N)


union(1,3)
union(2,3)
union(5,6)
print(parents)

# 3과 5는 같은 집합인가요?>
if find_set(3) == find_set(5):
    print("같은 집합입니다.")
else:
    print("다른집합입니다.")