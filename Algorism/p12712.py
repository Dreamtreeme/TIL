# 파리퇴치3
# N*N배열 안 파리 잡기 (5<=N<=15)
# M은 스프레이세기 (2<=M<=N)
# 파리는 30마리 이하

#완전탐색
#입력순서 1.테스트케이스, 2.N과 M, 3이후 N의1행부터 끝까지
T = int(input())
for _ in range(T):
 
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for i in range(n)]
 
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
 
    ti = [-1, 1, -1, 1]
    tj = [-1, 1, 1, -1]
 
    total = 0
    answer = 0
    for i in range(n):
        for j in range(n):
            cnt1 = li[i][j] # +모양 분사
            cnt2 = li[i][j] # x모양 분사
            for k in range(4): # 방향
                for l in range(1, m): # 분사 세기
                    a = i + di[k] * l
                    b = j + dj[k] * l
 
                    c = i + ti[k] * l
                    d = j + tj[k] * l
 
                    # 인덱스 범위 체크
                    if -1 < a < n and -1 < b < n:
                        cnt1 += li[a][b]
 
                    if -1 < c < n and -1 < d < n:
                        cnt2 += li[c][d]
 
            total = max(cnt1, cnt2)
            if answer < total: # 정답 갱신
                answer = total
 
    print(f"#{_ + 1}", answer)