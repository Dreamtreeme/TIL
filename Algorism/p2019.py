# 더블더블
# 부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.

#주어질 숫자는 30을 넘지 않는다.

t = int(input())
answer =[]
num = 1
answer.append(num)
for i in range(t):
    num *= 2
    answer.append(num)
print(*answer)

