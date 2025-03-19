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