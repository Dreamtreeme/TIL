print(7&5)
print(7|5)
print(bin(7&5))
# 이진수로 변환
# 각 자리를 AND, OR 연산한다.



# 비트연산 응용
# 1. 부분집합의 수를 바로 구할 수 있다.
arr=[1,2,3,4,5,6]# 16개

# 부분집합의 수
print(1<<len(arr))

for i in range(1<<len(arr)):
    subset=[]
    total=0
    for idx in range(len(arr)):
        if i & (1<<idx):
            subset.append(arr[idx])
            total+= arr[idx]

    if total ==10:
        print(f'부분집합: {subset}')

# 마지막 비트가 모두 1인지 확인하는 방법

