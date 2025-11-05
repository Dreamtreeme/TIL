def solution(numbers, hand):
    #엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 
    #키패드 이동 한 칸은 거리로 1에 해당합니다.
    keypad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    keypad_xy={}
    answer = ''
    for i in range(4):
        for j in range(3):
            keypad_xy[keypad[i][j]] = (i,j)
    
    # 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락
    left_finger ="*"
    #오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락
    right_finger = "#"
    
    # 답 추가 + 손가락 위치 갱신을 한 번에
    def press(side, num):
        nonlocal answer, left_finger, right_finger
        answer += side
        if side == "L":
            left_finger = num
        else:
            right_finger = num

    for next_num in numbers:
        if next_num in (1, 4, 7):
            press("L", next_num)
        elif next_num in (3, 6, 9):
            press("R", next_num)
        else:
            left_now_xy = keypad_xy[left_finger]
            right_now_xy = keypad_xy[right_finger]
            next_xy = keypad_xy[next_num]

            left_dist  = abs(left_now_xy[0]-next_xy[0]) + abs(left_now_xy[1]-next_xy[1])
            right_dist = abs(right_now_xy[0]-next_xy[0]) + abs(right_now_xy[1]-next_xy[1])

            if left_dist < right_dist or (left_dist == right_dist and hand == "left"):
                press("L", next_num)
            else:
                press("R", next_num)

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))