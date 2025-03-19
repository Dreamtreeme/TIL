# 수업에서 같은 조에 참여하고 싶은 사람끼리 두 사람의 출석 번호를 종이에 적어 제출하였다.

# 한 조의 인원에 제한을 두지 않았기 때문에, 한 사람이 여러 장의 종이를 제출하거나 여러사람이 한 사람을 지목한 경우 모두 같은 조가 된다.

# 예를들어 1-2번, 1-3번이 같은 조가 되고 싶다고 하면, 1-2-3번이 같은 조가 된다. 번호를 적지도, 다른사람에게 지목되지도 않은 사람은 단독으로 조를 구성하게 된다.

# 1번부터 N번까지의 출석번호가 있고, M장의 신청서가 제출되었을 때 전체 몇개의 조가 만들어지는지 출력하는 프로그램을 만드시오.
def make_set(x): # 1. 각 대표자들을 자기자신으로 만듦
    parents = [i for i in range(N+1)]
    return parents
def find_set(x): # 2. 대표자 찾기
    if parents[x] == x: # 이미 대표자가 자기자신이면 리턴
        return x
    return find_set(parents[x]) # 재귀호출로 타고 올라가서 대표자 찾기
def union(x,y): # 3. 병합하기
    global cnt
    ref_x = find_set(x)
    ref_y = find_set(y) # 우선 두 대표를 가져옴

    if ref_x == ref_y:
        return # 대표가 같으면 같은 집합이니 돌려보냄
    
    # 전체 몇개 조가 만들어지는지 확인하려면 병합되는 대표자조를 빼버리면됨
    if ref_x< ref_y: # 다르다면 어차피 병합이 이뤄지니 
        cnt-=1
        parents[ref_y]=ref_x
    else:
        cnt-=1
        parents[ref_x] = ref_y


T = int(input())
for tc in range(1, T+1):
    N,M = map(int, input().split())
    N_list = list(map(int, input().split()))
    parents = make_set(N) # 각 대표자들 설정
    cnt = N
    for i in range(M):
        s = N_list[2*i]
        e = N_list[(2*i)+1]
        union(s,e)
    print(f'#{tc} {cnt}')
