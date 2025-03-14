T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    min_sum = float('inf')
    for i in range(1<<N):
        subset=[]
        total=0
        for idx in range(N):
            if i & (1<<idx):
                subset.append(arr[idx])
                total+= arr[idx]
        if total >=M:
            min_sum=min(min_sum,total)

        
    print(f'#{tc} {min_sum-M}')


## dfs버전
def recur(cnt,total_height):
    global answer
    # 기저조건 가지치기
    # 탑이 더 높은 정답은 필요 없다
    if total_height >= M:
        answer = min(answer, total_height)
        return
    if cnt == N:
        return
    
    recur(cnt+1, total_height + heights[cnt]) # 탑에 포함 시키는 경우
    recur(cnt+1 , total_height) # 탑에 포함 안시키는 경우

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    heights = list(map(int, input().split()))
    answer = 2**31
    recur(0, 0)
    print(f'#{tc} {answer - M}')

