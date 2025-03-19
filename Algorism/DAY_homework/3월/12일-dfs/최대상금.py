# 정해진 숫자, 횟수
# 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.

def d(cnt, lis, visited):
    global max_num
    if cnt == M:
        result = int("".join(map(str, lis)))
        if max_num < result:
            max_num = result
        return

    current_num_str = "".join(lis)
    if (cnt, current_num_str) in visited:
        return
    visited.add((cnt, current_num_str))

    for i in range(len(lis) - 1):
        for j in range(i + 1, len(lis)):
            lis[i], lis[j] = lis[j], lis[i]
            d(cnt + 1, lis, visited)
            lis[j], lis[i] = lis[i], lis[j] 

T = int(input())
for tc in range(1, T + 1):
    N, M = input().split()
    M=int(M)
    N_list = list(N)
    max_num = 0
    visited = set() 
    d(0, N_list, visited)

    print(f'#{tc} {max_num}')