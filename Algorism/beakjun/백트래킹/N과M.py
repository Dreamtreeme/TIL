def backtrack(sequence, visited, N, M):
    # 수열의 길이가 M에 도달하면 출력
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return
    
    # 1부터 N까지의 숫자를 순회하며 순열 생성
    for i in range(1, N + 1):
        if not visited[i]:  # 중복 선택 방지
            visited[i] = True  # 선택 표시
            sequence.append(i)  # 수열에 추가
            backtrack(sequence, visited, N, M)  # 다음 숫자 탐색
            sequence.pop()  # 백트래킹: 선택 취소
            visited[i] = False  # 백트래킹: 선택 해제

# 입력 처리
N, M = map(int, input().split())

# 방문 여부를 체크하는 리스트 (인덱스 1부터 사용)
visited = [False] * (N + 1)

# 백트래킹 시작
backtrack([], visited, N, M)