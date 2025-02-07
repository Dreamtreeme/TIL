# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 
# 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

# 해당하는 부분집합이 없는 경우 0을 출력한다. 
# 모든 부분 집합을 만들어 답을 찾아도 된다.

# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

T= int(input())
for case in range(1,T+1):
    N,M= list(map(int,input().split()))
    result=0
    A = [a for a in range(1, 13)] # 집합 A리스트
    for i in range(1 << 12): # 1부터 2^12-1 까지 반복
        s = 0 # 부분집합의 합
        subset = 0 # 부분집합에 포함된 원소갯수
        for j in range(12): # 각 원소에 대해 포함 여부 확인
            if (i >> j) & 1: # i =0 일때 이진수는 0000 0000 0000 j=1일때 마지막 숫자 확인, 1이면 {1}이포함, 아니면 X
                subset += 1 # 원소갯수 추가
                s += A[j] # 원소값 연산
        if subset == N and s == M:
            result +=1
    


    print(f'#{case} {result}')