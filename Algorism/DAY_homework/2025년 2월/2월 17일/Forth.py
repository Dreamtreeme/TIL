def calculate_forth(code):
    stack = []
    tokens = code.split()
    for token in tokens:
            if token.isdigit():
                stack.append(int(token))
            elif token == '+':
                if len(stack) < 2:
                    return 'error'
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif token == '-':
                if len(stack) < 2:
                    return 'error'
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif token == '*':
                if len(stack) < 2:
                    return 'error'
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif token == '/':
                if len(stack) < 2:
                    return 'error'
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 // num2)
            elif token == '.':
                if len(stack) != 1:
                    return 'error'
                return stack.pop()
            else:
                return 'error'
    return 'error'  # '.' 없이 코드가 끝난 경우 또는 스택에 값이 남은 경우 ('.' 이후에 토큰이 있는 경우)

T = int(input())
for t in range(1, T + 1):
    code = input()
    result = calculate_forth(code)
    if result == 'error':
        print(f'#{t} error')
    else:
        print(f'#{t} {result}')