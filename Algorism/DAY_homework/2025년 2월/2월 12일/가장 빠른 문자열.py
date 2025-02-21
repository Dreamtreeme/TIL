# # 입력
# 2 테스트갯수
# banana bana # //A=”banana”, B=”bana”
# asakusa sa	# //A=”asakusa”, B=”sa”
# 일치 갯수 구하는 문제
# def brute_force_string_search(text, pattern):
#     n = len(text)
#     m = len(pattern)
#     counter=0
#     for i in range(n - m + 1): # 중복되기 때문에 안됨
#         j = 0
#         while j < m and text[i+j] == pattern[j]:
#             j += 1
#         if j == m:
#             counter+=1
#     return n - (m * counter) + counter  
T=int(input())
for case in range(1, T+1):
    result=0
    A,B= input().strip().split()
    i=0
    while i <= len(A) - len(B):
        if A[i:i+len(B)] == B:
            result+=1
            i += len(B)
        else:
            i +=1
    result = len(A) - (len(B) - 1) * result
    print(f"#{case} {result}") 