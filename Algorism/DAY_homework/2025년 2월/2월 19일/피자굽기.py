from collections import deque
# N개의 피자를 동시에 구울 수 있는 화덕이 있다.
# 피자는 치즈가 모두 녹으면 화덕에서 꺼내며, 치즈 양은 피자마다 다르다
# 1번 부터 M번까지 M개의 피자를 순서대로 화덕에 넣을때
# 치즈 양에 따라 녹는 시간이 다르기 때문에 꺼내지는 순서는 바뀔 수 있다.
# 화덕에 가장 마지막까지 남아있는 피자 번호를 알아내라

'''
조건 1 피자는 1번위치에서 넣거나 뺄 수 있다

조건 2 화덕 내부의 피자받침은 천천히 회전해서
1번에서 잠시 꺼내 치즈를 확인하고 다시 같은자리에 넣을 수 있다.
- 치즈확인 중간에 가능

조건 3 M개의 피자에 처음 뿌려진 치즈의 양이 주어지고
화덕을 한바퀴 돌때
녹지않은 치즈의 양은 반으로 줄어듬
이전 치즈의 양을 C라고 하면 다시 꺼냇을때 C//2로 줄어듬

조건4 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은
피자를 순서대로 넣는다
'''
T=int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N화덕크기,M피자갯수
    C = list(map(int, input().split()))
    oven = deque([None] * N)
    pizza = deque()

    for i in range(M):
        pizza.append({'num':i+1, 'c':C[i]})
    for i in range(N):
        if pizza:
            oven[i] = pizza.popleft()
    
    result =0
    rotacount=0
    
    while oven:
        oven.append(oven.popleft())

        rotacount +=1
        if rotacount ==N:
            rotacount = 0
            for i in range(N):
                if oven[i] is not None:
                    oven[i]['c']//=2
                    if oven[i]['c'] == 0:
                        result = oven[i]['num']
                        oven[i] = None
        
        if oven[0] is None and pizza:
            oven[0] = pizza.popleft()

        if not any(oven):
            break
    
    print(f'#{tc} {result}')