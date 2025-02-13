'''
( )( )((( )))
((( )((((( )( )((( )( ))((( ))))))
())
(()
)(
'''
txt = input()

top = -1
stack = [0] * 100

ans = 1 # 짝이 맞다고 가정
for x in txt:
    if x == '(':    # 여는 괄호 push  x in '[{(<'
        top += 1
        stack[top] = x
    elif x == ')':  # 닫는 괄호인 경우
        if top == -1:   # 스택이 비어있으면 (여는 괄호가 없으면 )
            ans = 0
        else:           # 여는 괄호 하나 버림
            top -= 1    # pop
if top != -1:   # 여는 괄호가 남아있으면
    ans = 0

print(ans)