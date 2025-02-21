from collections import deque

T=int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N 숫자갯수, M번
    nums = list(map(int,input().split()))
    #강사님 쓴거
    q = deque() #큐만들기 데큐못쓰면 리스트로
    q.extend(nums) # num리스트에 모든 원소를 큐에추가

    # M번 이동
    for _ in range(M):
        q.append(q.popleft()) # 삭제후 뒤로 삽입
    result = q.popleft()
    print(f'#{tc} {result}')

#내가쓴거
# arr = [0]*2000
#     front=rear=-1
#     
#     for i in num:
#         rear+=1
#         arr[rear]=i
        
#     for t in range(M):
#         front+=1
#         rear+=1
#         arr[rear]=arr[front]
#     result = arr[front+1]