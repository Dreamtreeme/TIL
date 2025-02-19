from collections import deque
A=10
for _ in range(A):

    T=int(input())
    N = list(map(int,input().split()))
    anigma = deque()
    for i in N:
        anigma.append(i)
    flag=True
    while flag:
        for i in range(1,6):
            if anigma[0]-i <= 0:
                flag=False
                a=anigma.popleft()
                anigma.append(0)
                break
            else:
                a=anigma.popleft()
                anigma.append(a-i)
    print(f'#{T}')
    print(*anigma)
    