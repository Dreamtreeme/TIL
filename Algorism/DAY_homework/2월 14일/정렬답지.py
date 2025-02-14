def bubble_sort(arr): #버블정렬
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap

def selection_sort(arr): # 선택정렬
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap

def counting_sort(arr): #카운팅 정렬
    max_value = max(arr)
    count = [0] * (max_value + 1)
    for num in arr:
        count[num] += 1
    sorted_arr = []
    for i in range(max_value + 1):
        sorted_arr.extend([i] * count[i])
    return sorted_arr