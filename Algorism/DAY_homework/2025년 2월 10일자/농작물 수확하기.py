
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    li =[]
    for _ in range(N):
        li.append(list(input()))
    start = N // 2
    end = N // 2
    total = 0
    for i in range(N):
        for j in range(start, end + 1):
            total+= int(li[i][j])
        if i < N // 2:
            start -= 1
            end += 1
        else:
            start +=1
            end -=1

    print(f'#{test_case} {total}')

# 별찍기 풀이


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [[int(num) for num in input()] for _ in range(N)]
    sum_val =0
    mid = N//2 #중앙의 좌표
    for r in range(mid+1): # 가운데 줄까지 반복
         start = mid -r
         end = mid +r
         for c in range(start,end + 1):
             sum_val += arr[r][c]

    # 아래 삼각형
    for r in range(mid+1, N):
        start = mid - (N-1 -r)
        end = mid + (N-1+r)
        sum_val += arr[r][c]
        
    print(f'#{test_case} {total}')