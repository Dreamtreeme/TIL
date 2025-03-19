   
t = int(input())
for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    node_values = [0] * (n + 1)
    for _ in range(m):
        node, val = map(int, input().split())
        node_values[node] = val

    for i in range(n // 2, 0, -1): 
        current_sum = 0
        left_child = 2 * i
        right_child = 2 * i + 1

        if left_child <= n:
            current_sum += node_values[left_child]

        if right_child <= n:
            current_sum += node_values[right_child]

        node_values[i] = current_sum
    result= node_values[l]
    print(f"#{tc} {result}")
