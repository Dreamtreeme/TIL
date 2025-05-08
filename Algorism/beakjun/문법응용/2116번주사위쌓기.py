import sys

# 빠른 입력을 위해 sys.stdin.readline 사용
input = sys.stdin.readline

def solve():
    # 주사위 개수 N 입력
    n = int(input())

    # 각 주사위의 면 정보 입력 및 저장
    dice_data = []
    for _ in range(n):
        dice_data.append(list(map(int, input().split())))

    # 주사위 면의 반대편 인덱스 매핑
    # 입력 순서: a b c d e f
    # 반대편 쌍: (a,f), (b,d), (c,e)
    # 인덱스: (0, 5), (1, 3), (2, 4)
    opposite_idx = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}

    # 모든 경우를 통틀어 얻을 수 있는 최대 옆면 눈의 총합
    max_total_sum = 0

    # 첫 번째 주사위의 밑면이 될 수 있는 6가지 경우를 모두 시도
    # i는 첫 번째 주사위의 밑면이 될 면의 인덱스 (0부터 5까지)
    for start_face_idx in range(6):
        # 현재 시도하는 경우에서의 옆면 눈 총합
        current_total_sum = 0
        
        # 첫 번째 주사위의 현재 밑면 값 설정
        # dice_data[0]는 첫 번째 주사위의 면 정보 리스트
        current_bottom_val = dice_data[0][start_face_idx]

        # 주사위 스택을 위로 올라가며 시뮬레이션 (k는 주사위 인덱스 0부터 N-1까지)
        for k in range(n):
            # 현재 처리할 주사위의 면 정보 가져오기
            current_die = dice_data[k]

            # 현재 주사위에서 밑면 값의 인덱스 찾기
            # current_bottom_val은 이전 주사위의 윗면 값이므로 현재 주사위에 반드시 존재함
            bottom_idx = current_die.index(current_bottom_val)

            # 밑면 인덱스의 반대편 인덱스 (윗면 인덱스) 찾기
            top_idx = opposite_idx[bottom_idx]
            # 윗면 값 가져오기
            top_val = current_die[top_idx]

            # 현재 주사위의 옆면 눈 중 최댓값 계산
            # 주사위 눈은 1부터 6까지이며, 밑면과 윗면을 제외한 나머지 4개 눈이 옆면
            # 1부터 6까지 전체 눈의 집합에서 밑면 눈과 윗면 눈을 제외한 후 최댓값 찾기
            all_values = {1, 2, 3, 4, 5, 6}
            excluded_values = {current_bottom_val, top_val}
            side_values = list(all_values - excluded_values) # 옆면 눈들의 리스트
            max_side = max(side_values) # 옆면 눈들 중 최댓값

            # 현재 주사위의 옆면 최대값을 총합에 더함
            current_total_sum += max_side

            # 다음 주사위의 밑면은 현재 주사위의 윗면 값이 됩니다.
            # 다음 반복을 위해 current_bottom_val 업데이트
            # (k가 N-1일 때는 이 값이 다음 주사위에 사용되진 않지만, 루프 구조 유지를 위해 진행)
            current_bottom_val = top_val

        # 현재 시작 밑면 경우에 대한 시뮬레이션이 끝나면, 전체 최대 총합 업데이트
        max_total_sum = max(max_total_sum, current_total_sum)

    # 모든 시작 경우를 시도한 후 최종 최대 총합 출력
    print(max_total_sum)

# 함수 실행
solve()