# 6개의 원소 1~6이 존재하는경우
N=6
# 1. 각 집합을 만들어주는 함수
def make_set(n):
    # 1~n 까지의 원소가 있다고 가정 -> 총 n개의 집합을 생성
    # 각 원소의 부모를 자신으로 초기화
    parents = [i for i in range(N+1)]
    return parents

def find_set(x):
    # 자신 == 부모노드 -> 해당 집합의 대표자
    if parents[x] == x:
        return x
    # x의 부모노드를 기준으로 다시 대표자를 검색
    return find_set(parents[x])
def union(x,y): # union은 대표자들 검색이 우선
    # 대표자들끼리 병합
    ref_x = find_set(x)
    ref_y = find_set(y)

    # 만약 이미 같은 집합이라면?
    if ref_x == ref_y:
        return #끝
    
    # 다른 집합이라면 합친다.
    # 문제에 따라 우선되는 집합으로 합쳐줌
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y

parents = make_set(N)

union(1,3)
union(2,3)
union(5,6)
print(parents)

# 3과 5는 같은 집합인가요?>
if find_set(3) == find_set(5):
    print("같은 집합입니다.")
else:
    print("다른집합입니다.")