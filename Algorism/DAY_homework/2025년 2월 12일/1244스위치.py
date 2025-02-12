# 입력
# 8 스위치 개수
# 0 1 0 1 0 0 0 1 스위치 상태
# 2 학생수
# 1 3 학생 번호, 주어진 번호
# 2 3 여학생, 주어진번호
# 출력
# 1 0 0 0 1 1 0 1 최종 스위치 상태

sc= int(input())
s_li= list(map(int,input().split()))
case = int(input())
counter=0
for _ in range(case):
    s, num = list(map(int,input().split()))
    if s==1:# 남자부분
        for i in range(1,sc+1):
            if i % num==0:# 배수 비교 부분
                s_li[i-1] = 1 - s_li[i-1]
        
    else: # 여자부분
        idx = num -1
        s_li[idx] = 1 - s_li[idx]
        l, r =idx -1 , idx +1
        while l>=0 and r <sc: # 대칭비교 부분
            if s_li[l] == s_li[r]:
                s_li[l] = 1-s_li[l]
                s_li[r] = 1-s_li[r]
                l -= 1
                r += 1
            else:
                break
# 출력 부분
chunksize=20    
result_count = sc//chunksize
for i in range(result_count+1):
    
    chunk= s_li[chunksize*i:(chunksize*i)+chunksize]
    print(*chunk)