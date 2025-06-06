#문제읽기
'''
고등학교 학생들이 학교에서 수련회를 갔다. 수련회에 간 학생들은 친구들과 음주가무를 즐기다가 밤 12시가 되자 조교들의 눈을 피해 자기방으로 돌아가려고 한다.

제 시간에 자기방으로 돌아가지 못한 학생이 한 명이라도 발견되면 큰일나기 때문에 최단 시간에 모든 학생이 자신의 방으로 돌아가려고 한다.

숙소는 긴 복도를 따라 총 400개의 방이 다음과 같이 배열되어 있다.

 

모든 학생들은 현재 위치에서 자신의 방으로 돌아가려고 하는데, 만약 두 학생이 자기방으로 돌아가면서 지나는 복도의 구간이 겹치면 두 학생은 동시에 돌아갈 수 없다.

예를 들어 (방1 -> 4) 와 (방3 -> 6) 은 복도 구간이 겹치므로 한 사람은 기다렸다가 다음 차례에 이동해야 한다. 이동하는 데에는 거리에 관계없이 단위 시간이 걸린다고 하자.

각 학생들의 현재 방 위치와 돌아가야 할 방의 위치의 목록이 주어질 때, 최소 몇 단위시간만에 모든 학생들이 이동할 수 있는지를 구하시오.
'''

# 자료구조
'''
1. 테스트케이스 T
2. 학생 수 N
3. 학생마다 위치한방, 돌아갈 방 리스트
'''

# 알고리즘
'''

시간복잡도
N명마다 N-1씩 비교로 하니 O(N^2)의 반절정도 8000
'''
# def dfs(li):
#     global cnt
#     if cnt>N or li==[]:
#         return
#     new_li=[]
#     load = [0]*200
#     for i in li:
#         if i[0]>i[1]:
#             i[0],i[1]=i[1],i[0]
#         if i[0]%2==1:
#             idx =i[0]-1
#             if i[1]%2==1:
#                 endidx = i[1]-1
#             else:
#                 endidx = i[1]-2
#         elif i[0]%2==0:
#             idx =i[0]-1
#             if i[1]%2==0:
#                 endidx = i[1]-2
#             else:
#                 endidx = i[1]-1
#         for j in range(idx, endidx+1,1):
#             if load[j]:
#                 new_li.append(i)
#                 break
#             load[j]=1
#     cnt+=1
#     dfs(new_li)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = [tuple(map(int, input().split())) for _ in range(N)]
    
    # 복도 구간별 사용 횟수
    corridor = [0] * 200
    for a, b in li:
        start = (min(a, b) - 1) // 2
        end = (max(a, b) - 1) // 2
        for i in range(start, end + 1):
            corridor[i] += 1
    
    # 최대 중첩 수 = 필요한 최소 시간
    result = max(corridor)
    print(f'#{tc} {result}')


