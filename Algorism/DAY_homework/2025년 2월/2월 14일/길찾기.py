def solve():
    test_case_num, path_count = map(int, input().split())
    path_data = list(map(int, input().split()))

    adj_list = [[] for _ in range(100)] # 인접 리스트 초기화

    for i in range(0, len(path_data), 2):
        start_node = path_data[i]
        end_node = path_data[i+1]
        adj_list[start_node].append(end_node) # 출발 노드에서 도착 노드로 가는 길 추가

    def has_path(current_node, destination_node):
        if current_node == destination_node:
            return True
        for neighbor in adj_list[current_node]:
            if has_path(neighbor, destination_node):
                return True
        return False

    path_exists = has_path(0, 99) # A(0)에서 B(99)로 가는 길 탐색

    if path_exists:
        result = 1
    else:
        result = 0

    return f"#{test_case_num} {result}"

# input.txt 파일에서 입력 읽기 (필요한 경우)
# import sys
# sys.stdin = open("input.txt", "r")

# 출력 파일 output.txt에 쓰기 (필요한 경우)
# sys.stdout = open("output.txt", "w")


T = 10 # 총 10개의 테스트 케이스
for _ in range(T):
    output = solve()
    print(output)