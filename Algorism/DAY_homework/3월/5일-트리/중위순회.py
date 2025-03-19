
def in_order(node_num):
        global result_word
        if node_num:
            in_order(left_child[node_num])
            result_word += chars[node_num]
            in_order(right_child[node_num])
        return result_word

T = 10
for tc in range(1, T + 1):
    N = int(input())
    chars = [0] * (N + 1)
    left_child = [0] * (N + 1)
    right_child = [0] * (N + 1)

    for _ in range(N):
        num, char, *child = input().split() # 변수 언패킹
        vertex_num = int(num)
        chars[vertex_num] = char
        left_child[vertex_num] = int(child[0]) if child else 0 # 조건 표현식
        right_child[vertex_num] = int(child[1]) if len(child) > 1 else 0 # 조건 표현식

    result_word = ""
    answer=in_order(1)
    print(f'#{tc} {answer}')
    