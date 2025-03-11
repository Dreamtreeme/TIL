# N이 5일 경우,

# 1 – 2 + 3 – 4 + 5 = 3

# N이 6일 경우,

# 1 – 2 + 3 – 4 + 5 – 6 = -3
t= int(input())

def fun(num):
    if num <= 0:
        return 0  
    elif num % 2 == 1:
        result = num + fun(num - 1)
    else:  
        result = -num + fun(num - 1)
    return result  
for case in range(1, t+1):
    result = 0
    N= int(input())
    result = fun(N)
    print(f'#{case} {result}')

