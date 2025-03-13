arr = ["A", "B", "C", "D", "E"]
result = []

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
            result.append([arr[i], arr[j], arr[k]])

print(f"조합의 개수: {len(result)}")
print(f"조합 결과: {result}")


# 재귀 함수로 변화

def com(start, current_arr): # 함수 매개변수에 추가

    if len(current_arr) ==3:
        result.append(current_arr[:])
        return
    # 이전 재귀로부터 넘겨받아야하는 변수가 나오면
    for i in range(start, len(arr)):
        current_arr.append(arr[i])
        com(i+1, current_arr)
        current_arr.pop()

com(0,[])

# 중복 순열의 경우

def com(current_arr):

    if len(current_arr) ==3:
        result.append(current_arr[:])
        return
    
    for i in range(len(arr)):
        current_arr.append(arr[i])
        com(current_arr)
        current_arr.pop()

com(0,[])