#                             완전 탐색          다이나믹프로그래밍                                그리디
# 속도                        아주 느림     <<      빠름                                      <<<<    매우 빠름
# 전역적인 해를 찾을 수 있는가     O                  O                                                 ?
# 수행방식                     모든 경우       큰문제->작은문제->조합(점화식)->최적해를 만들어나감        매 순간 최선의 선택을 함(지역적인 최적해는 찾을 수 있는데, 전역적으로 최적해인지 알수 없음)
 

# T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
# for test_case in range(1, T + 1):
#     txt = input()
#     result=0
#     top = 0
#     stack = [0] * 500000
#     li=[0]

#     for x in txt:
#         if x == '(': # (경우
#             top+=1
#         else:           # )인 경우
#             top-=1
#         li.append(top)
#     # 커트 지점을 기점으로 양 옆값 더함. 그리고 커트지점과 지점 사이의 요소들중 가장 낮은 요소를 뺌


#     cut_idx=[]
#     for i in range(len(txt)-1):
#         if txt[i]+txt[i+1] == "()":
#             cut_idx.append(i+1)
#             result += (li[i]+li[i+2])
#     for c in range(len(cut_idx)-1):

#         result -= min(li[cut_idx[c]:cut_idx[c+1]])

#     print(f'#{test_case} {result}')

#문제의 핵심 1차원 배열 인덱스를 얼마나 잘 다루나

T = int(input())

for tc in range(1, T+1):
    text = input().strip()
    cnt = 0
    pieces = 0
    for i in range(len(text)):
        c = text[i]
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1
            if text[i-1] == '(':
                pieces += cnt
            elif text[i-1] ==')':
                pieces += 1
    print(f"#{tc} {pieces}")
