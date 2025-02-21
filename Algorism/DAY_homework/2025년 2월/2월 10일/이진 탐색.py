def binary_search(array, target):
    low = 0
    high = len(array) - 1
    counter = 0

    while low <= high:
        mid = (low + high) // 2  # 중간 값 계산
        counter+=1
        if array[mid] == target:
            return counter
        elif array[mid] > target:
            high = mid - 1  # 왼쪽 범위로 좁히기
        else:
            low = mid + 1  # 오른쪽 범위로 좁히기

    return -1 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N, A, B = list(map(int, input().split()))
    arr = [i for i in range(1, N+1)]
    if binary_search(arr, A)<binary_search(arr, B):
        result = 'A'
    elif binary_search(arr, A)>binary_search(arr, B):
        result = 'B'
    else:
        result = 0
    
            
    print(f'#{test_case} {result}')
