# # M의 우측 N개를 확인할 예정
# def solution():
#     target = M
#     # N 번 확인한다.
#     for _ in range(N):
#         # 맨 우측 비트가 1인지 체크
#         # 0x1: 비트 연산이라는것을 명시하기 위해 사용
#         if target & 1 == 0:
#             return False
#         # 맨 우측 비트를 삭제
#         target = target >> 1
#     return True

# # 단순하게 하는 방법
# def solution():
#     # N 개의 1을 구함
#     mask = (1<<N)-1
#     result = (M& mask) == mask
#     return result
    
# T=int(input())

# for tc in range(1, T+1):
#     N, M =map(int, input().split())
#     result=solution()
#     print(f'#{tc} {result}')

hex_num = "0x1DB176C588D26EC"
binary_num = bin(int(hex_num, 16))[2:]
print(binary_num)