def make_num(idx, result, plus, minus, multiply, divide):
    global max_value, min_value

    if idx == N:
        max_value = max(max_value, result)
        min_value = min(min_value, result)
        return

    if plus:
        make_num(idx + 1, result + nums[idx], plus - 1, minus, multiply, divide)
    if minus:
        make_num(idx + 1, result - nums[idx], plus, minus - 1, multiply, divide)
    if multiply:
        make_num(idx + 1, result * nums[idx], plus, minus, multiply - 1, divide)
    if divide:
        make_num(idx + 1, int(result / nums[idx]), plus, minus, multiply, divide - 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    oper = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    max_value, min_value = float("-inf"), float("inf")
    make_num(1, nums[0], oper[0], oper[1], oper[2], oper[3])
    ans = max_value - min_value

    print(f"#{tc} {ans}")



# 강사님 코드
def cal(num1, num2, oper_idx):
    if oper_idx == 0:
        return num1 + num2

    if oper_idx == 1:
        return num1 - num2

    if oper_idx == 2:
        return num1 * num2

    if oper_idx == 3:
        if num1 < 0:  # 음수처리
            return -(abs(num1) // num2)
        return num1 // num2


# 재귀 설계
# 시작점: 첫 번째 숫자
# 끝점: 모든 수(연산자)를 사용할 때 까지
# 파라미터: 특정 시점에서 계산된 결과값
def dfs(level, total):
    global min_result, max_result

    if level == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return

    # 4개의 연산자를 확인
    for i in range(4):
        if opers[i] == 0:  # 남은 연산자가 없으면 통과
            continue

        opers[i] -= 1
        dfs(level + 1, cal(total, numbers[level], i))
        opers[i] += 1


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_result = 1e9
    max_result = -1e9

    dfs(1, numbers[0])
    print(f'#{tc} {max_result - min_result}')
