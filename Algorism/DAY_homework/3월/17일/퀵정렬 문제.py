def quicksort(lft, rgt):
    
    if lft < rgt: 
        pivot_idx = partition(lft,rgt)

        quicksort(lft, pivot_idx - 1)
        quicksort(pivot_idx + 1, rgt)

def partition(lft, rgt):
    global arr
    
    pivot = arr[lft]
    i = lft + 1
    j = rgt

    while i <= j:
        while i <= rgt and arr[i] <=pivot:
            i+=1
        
        while arr[j] > pivot:
            j -=1
        
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    arr[lft],arr[j] = arr[j], arr[lft]

    return j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    quicksort(0,N-1)
    print(f'#{tc} {arr[N//2]}')