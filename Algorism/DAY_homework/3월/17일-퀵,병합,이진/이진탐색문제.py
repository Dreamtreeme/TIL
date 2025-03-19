def binary_search(A, target):
    l, r = 0, len(A) - 1
    directions = []  # 선택한 방향을 저장하는 리스트
    
    while l <= r:
        m = (l + r) // 2
        if A[m] == target:
            # target을 찾았을 때 조건 확인
            if len(directions) == 0:  # 첫 번째 시도에서 찾음
                return True
            if len(directions) == 1:  # 한 번 선택 후 찾음
                return True
            # 두 번 이상 선택했고 방향이 바뀐 경우 확인
            if any(directions[i] != directions[i+1] for i in range(len(directions)-1)):
                return True
            return False
        elif A[m] < target:
            directions.append('R')  # 오른쪽 구간 선택
            l = m + 1
        else:
            directions.append('L')  # 왼쪽 구간 선택
            r = m - 1
    return False  # target이 A에 없음

# 입력 처리 및 메인 로직
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = 0
    for target in B:
        if binary_search(A, target):
            count += 1
    
    print(f"#{t} {count}")