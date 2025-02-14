#                             완전 탐색          다이나믹프로그래밍                                그리디
# 속도                        아주 느림     <<      빠름                                      <<<<    매우 빠름
# 전역적인 해를 찾을 수 있는가     O                  O                                                 ?
# 수행방식                     모든 경우       큰문제->작은문제->조합(점화식)->최적해를 만들어나감        매 순간 최선의 선택을 함(지역적인 최적해는 찾을 수 있는데, 전역적으로 최적해인지 알수 없음)
 

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    txt = input()
    result=0
    top = 0
    stack = [0] * 500000
    li=[0]

    for x in txt:
        if x == '(': # (경우
            top+=1
        else:           # )인 경우
            top-=1
        li.append(top)
    # 커트 지점을 기점으로 양 옆값 더함. 그리고 커트지점과 지점 사이의 요소들중 가장 낮은 요소를 뺌


    cut_idx=[]
    for i in range(len(txt)-1):
        if txt[i]+txt[i+1] == "()":
            cut_idx.append(i+1)
            result += (li[i]+li[i+2])
    for c in range(len(cut_idx)-1):

        result -= min(li[cut_idx[c]:cut_idx[c+1]])

    print(f'#{test_case} {result}')

#문제의 핵심 1차원 배열 인덱스를 얼마나 잘 다루나

T = int(input())

for tc in range(1, T+1):
    text = input().strip() # 쇠막대기 문자열
    cnt = 0 # 열린 괄호의 갯수
    pieces = 0 # 조각의 갯수

    # 같은 (라도 뒤(i+1)에 뭐가 오는지에 따라 해석이 다름
    # 같은 )라도 앞(i-1)에 뭐가 오는지에 따라 해석이 다름.
    for i in range(len(text)): # 인덱스 i가 필요
        c = text[i] # i번째 현재 문자
        if c == '(': # 여는 괄호라면
            cnt += 1 # 여는 괄호의 갯수를 1 증가시킴
        elif c == ')': # 닫는 괄호라면
            cnt -= 1 # 여는 괄호 -> 그동안 쌓인 막대기 수
            if text[i-1] == '(': # 이전 문자가 여는 괄호 => 레이저
                pieces += cnt # 그동안 쌓인 막대기만큼 조각 발생
            elif text[i-1] ==')': # 이전 문자가 닫는 괄호 => 순수하게 막대기의 끝
                pieces += 1 # 하나의 막대가 끝나서 한 조각만 증가
    
    print(f"#{tc} {pieces}")
