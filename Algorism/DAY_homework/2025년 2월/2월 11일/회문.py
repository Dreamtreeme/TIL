# # 입력
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50

# 다음 줄부터 테스트케이스의 첫 줄에 N과 M이 주어진다. 10≤N≤100, 5≤M≤N

# 다음 줄부터 N개의 글자를 가진 N개의 줄이 주어진다.
T= int(input())
for case in range(1, T+1):
    result=""
    N,M = list(map(int,input().split()))# N은 행길이, M은 글자숫자
    matrix=[]
    for i in range(N):
        row= input()
        matrix.append(row) # 행 한줄추가
    # N*N행렬 문자 다 채워짐
    
    for k in range(N):  # 모든 행과 열을 번갈아 가며 조회
        for i in range(N - M + 1):  # 행 또는 열에 대한 검사, 최소 1개 검사
            # 행 검사
            sub_s_row = ""
            for j in range(M):
                sub_s_row += matrix[k][i + j]  # 한글자씩 추가

            is_palindrome_row = True
            for j in range(M // 2):  # 부분 문자열의 절반만 비교
                if sub_s_row[j] != sub_s_row[M - 1 - j]:  # 시작과 끝 비교
                    is_palindrome_row = False
                    break

            if is_palindrome_row:
                result = sub_s_row
                break  # 회문을 찾았으면 더 이상 검사할 필요 없음

            # 열 검사
            sub_s_col = ""
            for j in range(M):
                sub_s_col += matrix[i + j][k]  # 한글자씩 추가

            is_palindrome_col = True
            for j in range(M // 2):  
                if sub_s_col[j] != sub_s_col[M - 1 - j]:  
                    is_palindrome_col = False
                    break

            if is_palindrome_col:
                result = sub_s_col
                break  
        if result: # 행 또는 열에서 회문을 찾았으면 다른 행/열 검사 불필요
            break

    print(f"#{case} {result}") 