def cut(arr, N):
    if N == 2:
        player1 = arr[0][1]
        player2 = arr[1][1]
        if (player1 == 1 and player2 == 2) or \
           (player1 == 2 and player2 == 3) or \
           (player1 == 3 and player2 == 1):
            return arr[1] 
        else:
            return arr[0]  
    elif N == 1:
        return arr[0] 

    elif N > 2:
        winner = []
        mid = N // 2
        arr1 = arr[:mid]
        arr2 = arr[mid:]

        winner1 = cut(arr1, len(arr1)) 
        winner2 = cut(arr2, len(arr2)) 

        winner.append(winner1)
        winner.append(winner2)

        return cut(winner, 2) 

T= int(input())
for case in range(1, T+1):
    N = int(input())
    input_arr = list(map(int,input().split()))

    arr = []
    for index, value in enumerate(input_arr):
        arr.append([index, value])

    result = cut(arr,N)
    result_index = result[0]+1
    print(f'#{case} {result_index}')

#######
T= int(input())
for case in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int,input().split()))


    print(f'#{case} {result_index}')