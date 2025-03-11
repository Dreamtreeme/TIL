# 숫자 N은 아래와 같다.

# N=2a x 3b x 5c x 7d x 11e

# N이 주어질 때 a, b, c, d, e 를 출력하라.


# [제약 사항]

# N은 2 이상 10,000,000 이하이다.


# [입력]

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.

# 입력

# 10  
# 6791400
# 1646400
# 1425600
# 8575
# 185625
# 6480
# 1185408
# 6561
# 25
# 330750

#출력

#1 3 2 2 3 1
#2 6 1 2 3 0
#3 6 4 2 0 1
#4 0 0 2 3 0
#5 0 3 4 0 1
#6 4 4 1 0 0
#7 7 3 0 3 0
#8 0 8 0 0 0
#9 0 0 2 0 0
#10 1 3 3 2 0

def factorize(n, divisor):
    count = 0
    while n%divisor == 0:
        n//divisor
        count+=1
    return count,n

t = int(input())
primes = [2, 3, 5, 7, 11]

for case in range(1, t + 1):
    num = int(input())
    factors = []
    for prime in primes:
        count, num = factorize(num, prime)
        factors.append(count)
    print(f'#{case} {" ".join(map(str, factors))}')
    
    