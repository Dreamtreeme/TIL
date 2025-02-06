
# 가로 길이는 항상 100으로 주어진다.

# 모든 위치에서 상자의 높이는 1이상 100이하로 주어진다.

# 덤프 횟수는 1이상 1000이하로 주어진다.

T = 10 # 테스트케이스
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    Dump = int(input()) # 덤프 횟수
    li = list(map(int, input().split())) # 최고점 높이
    for _ in range(Dump):
    # 일단 최고점과 최저점을 찾아야함
        max_h=0
        min_h=101
        for i in range(100):
            if max_h<=li[i]:
                max_h=li[i]
                max_h_idx=i
            if min_h>=li[i]:
                min_h=li[i]
                min_h_idx=i
        # 최고점 최저점 갱신완료지점
        # 이제 최고점인덱스에 -1을 최저점인덱스에 +1을한다
        li[min_h_idx]+=1
        li[max_h_idx]-=1
        

        if max_h-min_h<=1: # 최고점 최저점 역전시점이 더이상 평탄화X
            result = 0
            break
    # 한번더 찾기
    max_h=0
    min_h=101
    for i in range(100):
        if max_h<=li[i]:
            max_h=li[i]
            max_h_idx=i
        if min_h>=li[i]:
            min_h=li[i]
            min_h_idx=i
    result = max_h-min_h


        

    print(f'#{test_case} {result}')