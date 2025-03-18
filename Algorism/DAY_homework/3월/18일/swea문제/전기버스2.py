# 충전지 처음 장착
# 충전지마다 배터리 용량 다름
# 정류장과 충전지에 대한 정보가 주어질때, 목적지에 도착하는데
# 필요한 최소한의 교환회수 출력

# 풀이전략
# 처음 1번 번호 맞추기 위해 정류장수 +1 만큼의 배열 만듦
def dfs(cnt,current, next_range):
    global result
    if cnt>result:
        return
    if (current+next_range) >= N:
        result = cnt
        return
    
    for i in range(current+1, current+next_range+1):
        dfs(cnt+1,i,bus_stop[i])
T=int(input())
for tc in range(1, T+1):
    NandBs= list(map(int, input().split()))
    N = NandBs.pop(0)
    battery= NandBs
    bus_stop = [0]
    bus_stop+=battery
    result = 50
    dfs(0,1,bus_stop[1])
    
    print(f'#{tc} {result}')


T = int(input())


def go(idx, battery, cnt): 
    global min_cnt

    battery -= 1 

    if battery < 0: 
        return
    
    if cnt >= min_cnt: 
        return 
    if battery >= 0 and idx == N: 
        min_cnt = min(cnt, min_cnt) 
        return 
    go(idx+1, battery, cnt)

    go(idx+1, M[idx], cnt +1) 


for tc in range(1, T+1):
    N, *M = list(map(int, input().split()))
    M = [0] + M 
    min_cnt = 2**32 
    go(2, M[1], 0)

    print(f"#{tc} {min_cnt}")
