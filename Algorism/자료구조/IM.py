'''
봉사동아리에서 교육 봉사를 나가는데 학생들 N명을 대상으로 교육을 실시할 예정입니다. 
학생이 많기 때문에 세개의 그룹으로 나누어 진행을 하고자 합니다.
(우수/보통/부진)
분반을 나누는 기준은 학생들이 미리 제출한 점수를 토대로
socre1, score2를 임의로 선정하여 나누려고 합니다.

score2 이상: 우수 분반/ score1이상 2미만 보통, 나머지 분반

각 분반은 원활한 교육을 위해 최소 인원 이상, 최대인원 이하를 만족해야 합니다
양질의 교육을 위해서 각 스코어 별로 임의로 3개의 분반을 나누었을때 
학생이 가장 많은 분반과 적은 분반의 학생 수 차의
최솟값을 구하세요

만약 분발 별 최소,최대 인원을 만족하는 기준인
1,2가 없다면 -1을 출력하세요

입력
TC
N min max-> 학생수 최소인원,최대인원
(5<=N<=1000, 1<=어학점수<=100)
N명의 점수가 한줄로 입력

입력예시   출력예시
5           #1 2
5 1 4
3 5 5 4 5
1
5 1 4
3 5 5 4 5'''

# 핵심 무조건 점수 분포를 봤을때 최소인원은 만족해야함
# 어떤 점수를 기준으로 나눠도 상관없음. 다만 분반 3개에
# 할당되는 학생수의 최대 최소인원 차이가 최소가 되야함
# 임의 의 수 score1, score2를 정해봄

# 방향성
# 카운터정렬 카운트

T=int(input())
for tc in range(1,T+1):
    N, Mi, Ma = map(int, input().split())
    N_li=list(map(int, input().split()))
    N_num=[]
    counter=[0]*(max(N_li)+1)
    for i in range(N):
        counter[N_li[i]]+=1
    for r in range(len(counter)):
        if counter[r]==0:
            continue
        N_num.append(r)
    sorted(N_num)
    result=-1    
    differ=[]
    for i in range(len(N_num)):
        for j in range(1,len(N_num)):
            a,b,c=0,0,0
            if i==j:
                continue
            for k in range(N):
                if N_li[k]<N_num[i]:
                    a+=1
                elif N_num[i]<=N_li[k]<N_num[j]:
                    b+=1
                else:
                    c+=1
            if Ma>=a>=Mi and Ma>=b>=Mi and Ma>=c>=Mi:
                differ.append(max(a,b,c)-min(a,b,c))
            
    if differ:
        result=min(differ)

    print(f'#{tc} {result}')

T = int(input())
for tc in range(1, T + 1):
    N, Mi, Ma = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort()  # 점수를 오름차순 정렬
    
    # 모든 가능한 score1, score2 쌍을 탐색
    result = -1
    min_diff = float('inf')
    
    for k in range(N):  # score1 기준 인덱스
        for m in range(k + 1, N):  # score2 기준 인덱스
            a = k  # score1 미만 (0 ~ k-1)
            b = m - k  # score1 이상 score2 미만 (k ~ m-1)
            c = N - m  # score2 이상 (m ~ N-1)
            
            # 각 그룹이 최소/최대 인원 조건을 만족하는지 확인
            if Mi <= a <= Ma and Mi <= b <= Ma and Mi <= c <= Ma:
                diff = max(a, b, c) - min(a, b, c)
                min_diff = min(min_diff, diff)
    
    # 조건을 만족하는 경우가 있으면 최솟값, 없으면 -1
    if min_diff != float('inf'):
        result = min_diff
    
    print(f'#{tc} {result}')
