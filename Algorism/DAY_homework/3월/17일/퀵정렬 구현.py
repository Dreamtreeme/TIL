# 퀵정렬
# 피벗 제일 왼쪽 요소
def partition(left,right):
    pivot = arr[left]

    i = left +1
    j = right
    while i<= j:
        # i = 큰 값을 검색하면서 오른쪽으로 진행
        while i <=j and arr[i] >= pivot:
            i +=1        
        # j = 작은 값을 검색하면서 왼쪽으로 진행
        while i <= j and arr[j] >= pivot:
            j -= 1
        # SWAP
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
        
        arr[left],arr[j] = arr[j], arr[left]

    return j
# left, right : 작업 범위
def quick_sort(left, right):
    if left < right :
        # pivot 을 정렬시킨다.
        pivot = partition(left,right)
        # 왼쪽 진행
        quick_sort(left, pivot-1)
        # 오른쪽 진행
        quick_sort(pivot+1, right)
arr =  [3,2,4,6,9,1,8,7,5]



# 강사님 구현
pivot = arr[0]

i = 0 # 왼쪽 포인터
j = len(arr) -1 # 오른쪽 포인터

while i < j : #크로스가 발생하지 않을때까지
    while arr[i] < pivot: # i 는  pivot보다 큰수를 찾아야함, 작은수는 건너뜀
        i +=1
    # while문을 빠져나오면 i는 pivot보다 큰수를 가리킴
    while arr[j] > pivot: # j는 pivot보다 작은수를 찾아야함. 큰수는 건너뜀
        j -=1
    
    if i < j:
        arr[i],arr[j] =arr[j],arr[i]

# pivot을 정렬된 위치에 놓아야함
arr[0], arr[j] = arr[j], arr[0]