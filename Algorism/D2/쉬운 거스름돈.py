T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = [0] * 8
    denominations = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    for i, denomination in enumerate(denominations):
        count = N // denomination
        result[i] = count
        N -= denomination * count

    result = " ".join(map(str, result))

    print(f'#{test_case}')
    print(result)