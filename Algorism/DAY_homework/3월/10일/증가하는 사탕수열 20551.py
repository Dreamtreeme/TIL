T = int(input())
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())
    if A < 1 or B < 2 or C < 3:
        print(f'#{tc} -1')
        continue
    eat_count = 0

    if B >= C:
        eat_c = B - (C - 1)
        eat_count += eat_c
        B = C - 1

    if A >= B:
        eat_b = A - (B - 1)
        eat_count += eat_b
        A = B - 1
    result = eat_count
    print(f'#{tc} {result}')