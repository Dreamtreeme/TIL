T = int(input())
for t in range(1, T + 1):
    for x in susik:
        if x not in '+-/*': # 피연산자면...
            top += 1            # push(x)
            stack[top] = int(x)
        else:
            op2 = stack[top]  # pop() 오른쪽, 피연산자
            top -= 1
            op1 = stack[top]  # pop() 왼쪽 피연산자
            top -= 1
            if x=='+':  # op1 + op2
                top += 1                # push()
                stack[top] = op1 + op2
            elif x=='-':
                top += 1
                stack[top] = op1 - op2
            elif x=='/':
                top += 1
                stack[top] = op1 / op2
            elif x=='*':
                top += 1
                stack[top] = op1 * op2

    
    print(f'#{t} {result}')
