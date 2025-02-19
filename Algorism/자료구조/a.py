T = 10 # 테스트 케이스 10개 고정
for tc in range(1, T+1):
    N = int(input()) # 문자열의 길이
    exp = input().strip() # 중위표현식 문자열
    out = '' # 변환된 문자열을 저장할 변수

    stack = [] # 연산자를 저장할 스택 # 높은 순위의 연산자가 먼저 나와야 함

    # 1.중위표현식 -> 후위표현식
    #  - 연산자를 우선순위에 따라 정렬 => 연산자 스택 사용

    # 규칙
    # exp를 왼쪽부터 한 문자씩 검사 : 한 문자를 c라고 할 때
    # 1. c가 피연산자라면 => 그대로 출력
    # 2. c가 연산자라면
    #    2.1. 스택이 비어있다면 => 그대로 넣기
    #    2.2. 스택이 비어있지 않다면 => 스택의 top과 문자 c를 비교
    #        2.2.1. top의 우선순위가 낮다면 => c를 스택에 넣는다
    #        2.2.2. top의 우선순위 == c의 우선순위 => top을 빼서 출력, c를 push
    #        2.2.3. top의 우선순위가 높다면 => 높은 것들을 모두 pop해서 출력
    #               (같은것과 만날 때까지, 같은 것을 만나면 2.2.2처럼)
    # 3. 마지막에 연산자 스택을 다 비워준다.

    for c in exp: # exp에서 한 문자씩 왼쪽에서 오른쪽으로 검사
        if c == '*': # 우선 순위가 높은 연산자
            # if stack: # 스택이 비어있지 않다면
            if not stack or stack[-1] == '+': # 스택이 비어있거나, top의 우선순위가 낮다면 
                stack.append(c) # 우선순위가 높은 연산자를 그 위에 추가
            else:
                while stack and stack[-1] == '*': # 스택이 비어 있지 않고, top의 우선순위 == c 의 우선순위라면 
                    out += stack.pop() # 일단 스택에 있는 것들을 전부 출력 
                stack.append(c) # c를 넣어준다.

        elif c == '+': # 낮은 연산자
            while stack: # stack이 비어있지 않다면 
                out += stack.pop() # 일단 모두 출력한 후에 넣는다.
            stack.append(c) # stack이 비어있다면 그냥 넣고 
        
        else: # 피연산자
            out += c # 피 연산자라면 그대로 출력
    
    # 스택을 전부 비운다.
    while stack:
        out += stack.pop()


    # 2.후위표현식 계산
    #  - 숫자 스택 사용

    stack2 = [] # 숫자의 스택, 숫자를 두개씩 꺼내서 계산 후 다시 스택에 push
    for c in out: # 변환된 후위 표현식을 왼쪽부터 차례로 본다
        if '0' <= c <= '9': # 만약에 숫자라면
            stack2.append(int(c)) # 정수로 변환해서 스택에 push
        elif c == '+': # + 연산자라면
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1 + num2)
        elif c == '*':
            num1 = stack2.pop()
            num2 = stack2.pop()
            stack2.append(num1 * num2)
    
    print(f"#{tc} {stack2.pop()}")
