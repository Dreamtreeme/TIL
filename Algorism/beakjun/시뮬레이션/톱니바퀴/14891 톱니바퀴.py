# 총 8개 톱니
# 톱니바퀴 4개
# 톱니는 N,S 둘중하나
# 톱니바퀴마다 1번부터 4번까지
# K번 회전 회전은 한칸
# 방향은 반시계 시계
# 맞물려있지않고 
# 맞은편이 다른극이면 회전시 방향 반대로 회전시킴
# 아니면 회전안함
# 12시방향부터 시계방향 순서대로 주어진다. 
# N극은 0, S극은 1로 나타나있다.
# 최종 톱니바퀴의 상태를 구하라
from collections import deque
import sys
input = sys.stdin.readline

# 톱니와 방향을 받았을때
def simul(t,d):
    global cogwheel
    # 회전 계획 (0=회전 없음)
    rot_dir = [0, 0, 0, 0]
    rot_dir[t] = d
    
    # 현재 맞물린 상태 저장 (회전하기 전에!)
    state = [(cogwheel[0][2], cogwheel[1][6]),
             (cogwheel[1][2], cogwheel[2][6]),
             (cogwheel[2][2], cogwheel[3][6])]

    # 왼쪽으로 전파
    cur_dir = d
    for i in range(t-1, -1, -1):
        if state[i][0] != state[i][1]:  # 맞물린 톱니 극이 다르면
            cur_dir *= -1               # 반대 방향으로 회전
            rot_dir[i] = cur_dir
        else:
            break                       # 같으면 더 이상 안 퍼짐

    # 오른쪽으로 전파
    cur_dir = d
    for i in range(t, 3):
        if state[i][0] != state[i][1]:
            cur_dir *= -1
            rot_dir[i+1] = cur_dir
        else:
            break

    # 실제 회전 수행
    for i in range(4):
        if rot_dir[i] != 0:
            cogwheel[i].rotate(rot_dir[i])
    return

# 우선 톱니바퀴들 4개를 받아서 상태저장
cogwheel = [deque(map(int, input().strip())) for _ in range(4)]
# 주의 1번톱니바퀴는 cogwheel[0]임

# 톱니바퀴 회전수
K = int(input())

# 회전수만큼 해당 시뮬 돌림
for _ in range(K):
    target, direction = map(int, input().split())
    simul(target-1,direction)

result = cogwheel[0][0] +(cogwheel[1][0]*2)+(cogwheel[2][0]*4)+(cogwheel[3][0]*8)
print(result)