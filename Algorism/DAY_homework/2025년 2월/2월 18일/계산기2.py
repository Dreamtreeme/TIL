T=10
for tc in range(1, T+1):
    N = int(input())
    exp = input().strip() # 중위표현식 문자열

    # 1. 중위표현식 -> 후위표현식
    # 연산자를 우선순위에 따라 정렬 => 연산자 스택 사용

    # 규칙
    # exp를 왼쪽부터 한 문자씩 검사 : 한문자를 c라 할때
    # 1. c가 피연산자라면 그대로출력
    output = ""
    # 2. c가 연산자라면
    #   2.1 스택이 비어있다면 => 그대로 넣기
    #   2.2 스택이 비어있지 않다면=> 스택의 top과 비교
    #       2.2.1 top의 우선순위가 낮다면 스택에 넣고 top+=1
    #       2.2.2 같다면 top-=1 하고 출력한다음 c를 다시 푸쉬
    #       2.2.3 높다면 높은 것들을 모두 pop해서 출력

    # 3. 마지막에 연산자 스택 전부 비워줌
    stack=[] # 높은 순위의 연산자가 먼저 나와야함
    for c in exp:
        if c == "*": # 높거나 
            if not stack or stack[-1] == "+": #비어있다면
                stack.append(c)
            else:
                while stack and stack[-1] == "*": 
                    output += stack.pop() #나보다 스택에 우선순위가 같거나 높은것들을 전부 출력
                stack.append(c)

        elif c == '+': # 낮거나
            while stack:
                output +=stack.pop()
            stack.append(c)

        else: #같거나
            output += c

    while stack:
        output+= stack.pop()

    # 2. 후위표현식 계산
    # -숫자 스택 사용
    stack2 = []
    for c in output:
        if '0' <= c <= '9': # 만약에 숫자라면
            stack2.append(int(c))
        elif c == "+":
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1+num2)
        elif c == "*":
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1*num2)
    print(f"#{tc} {stack2.pop()}")

