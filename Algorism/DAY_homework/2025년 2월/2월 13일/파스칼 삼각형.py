def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def pascal(n):
    result=[]
    for i in range(n+1):
        result.append(factorial(n) // (factorial(i) * factorial(n - i)))
    
    return " ".join(map(str,result))
T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')
    N= int(input())
    for i in range(N):
        print(pascal(i))