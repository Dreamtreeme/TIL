#1. 분할: 리스트의 길이가 1일 때까지 분할
#2. 정복: 리스트의 길이가 1이 되면 자동으로 정렬됨

#3. 병합: 왼쪽 오른쪽 리스트중
#  작은 원소부터 정답 리스트에 추가하면서 진행

def merge(left, right):
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복

    while l< len(left) and r<len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l +=1
        else:
            result[l+r] = right[r]
            r +=1
    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l< len(left) :
        result[l+r] = left[l]
        l +=1
    # 오른쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while r< len(left) :
        result[l+r] = right[r]
        r +=1
    
    return result

def merge_sort(li):
    if len(li) ==1:
        return li
    # 1. 절반 씩 분할
    mid = len(li) //2
    left = li[:mid]    # 리스트의 앞쪽 절반
    right = li[mid:]   # 리스트의 뒤쪽 절반

    left = merge_sort(left)
    right = merge_sort(right)

    # 분할이 완료되면
    # 2. 병합
    merged_list = merge(left, right)
    return merged_list

arr = [69, 10, 30 ,2 ,16 ,8 ,31, 22]
sorted_arr = merge_sort(arr)

# 강사님 구현
L = [2,2,4,5,5]
R = [1,3,3,4,6]

arr=[0] * (len(L)+len(R))

# 병합하기 로직

# i,j,k = 0 으로 놓고 출발
# i: L배열의 가장 작은 원소를 가리키는 포인터
# j: R배열을 가리키는 포인터
# k: 합칠 배열의 원소를 가리키는 포인터

# i번째와 j번째를 비교해서 둘 중 작은 값을 적는다.

i,j,k=0

# i번째와 j번째를 비교하려면,
# 둘다 L,R배열의 인덱스 범위안에 있어야함.
while i< len(L) and j< len(R):
    if L[i] < R[j]:
        arr[k] = L[i]
        k+=1
        i+=1
    else:
        arr[k] = R[j]
        k+=1
        j+=1

# 두 배열중 하나는 i,j 가 범위를 벗어남

while i< len(L):
    arr[k] = L[i]  

while j< len(R):
    arr[k] = R[j]