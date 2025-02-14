def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1] = arr[j+1] ,arr[j]

def selection_sort(arr):
    n= len(arr)
    for i in range(n):
        min_idx=i
        for j in range(i,n-1):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i], arr[min_idx] = arr[min_idx] ,arr[i]

def counting_sort(arr):
    m_v= max(arr)
    counter = [0]*(m_v+1)
    for num in arr:
        counter[num] +=1
    new_list=[]
    for i in range(m_v+1):
        new_list.extend(i*counter[i])
    return new_list