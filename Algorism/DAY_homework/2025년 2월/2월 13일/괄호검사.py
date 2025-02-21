T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    txt = input()

    top = -1
    stack = [0] * 100

    ans = 1 # 짝이 맞다고 가정
    for x in txt:
        if x in '({[':    # 여는 괄호 push  x in '[{(<'
            top += 1
            stack[top] = x
        elif x in ')}]':  # 닫는 괄호인 경우
            if top == -1:   # 스택이 비어있으면 (여는 괄호가 없으면 )
                    ans = 0
            else  :       # 여는 괄호 하나 버림
                top -= 1    # pop
    if top != -1:   # 여는 괄호가 남아있으면
        ans = 0
    result=ans

    print(f'#{test_case} {result}')