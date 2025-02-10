T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N=int(input())
    M = list(map(int, input().split()))
    li =[]
    # for i in range(N):
        # 반복 시작 후 홀수면 최대값, 최대값2
        # 짝수면 최소값, 최소값2
    
    for i in range(N - 1):  # 기준위치(최소 값을 찾는 구간의 시작 인덱스)
        min_idx = i         # 최소값 인덱스 초기화, 구간의 맨 앞 원소를 최소로 가정
        for j in range(i+1, N):  # 실제 최소값인지 비교하는 위치
            if M[min_idx] > M[j]:
                min_idx = j
        M[i], M[min_idx] = M[min_idx], M[i]
    # 선택정렬로 리스트 정렬
    for i in range(10):
        if i%2==0:
            li.append(M[N-(i//2)-1])
        else:
            li.append(M[i//2])
    result = " ".join(map(str,li))
            
    print(f'#{test_case} {result}')

    # 또는 조건 1 조건2 설정후 계산
