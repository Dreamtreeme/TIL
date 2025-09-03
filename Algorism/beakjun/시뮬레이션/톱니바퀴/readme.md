📝 코테 회고 – 톱니바퀴에서 막힌 3가지

1. 톱니 전파
   ❌ 틀린 코드
   def simul(t, d):
   cogwheel[t].rotate(d) # 그냥 돌려버림

문제: 옆 톱니 상태가 바뀌면서 잘못된 전파 결과 발생

✅ 수정한 코드
def simul(t, d):
rot_dir = [0,0,0,0]
rot_dir[t] = d

    # 회전 전에 접점 상태 저장
    state = [(cogwheel[0][2], cogwheel[1][6]),
             (cogwheel[1][2], cogwheel[2][6]),
             (cogwheel[2][2], cogwheel[3][6])]

    # 왼쪽 전파
    cur = d
    for i in range(t-1, -1, -1):
        if state[i][0] != state[i][1]:
            cur *= -1
            rot_dir[i] = cur
        else: break

    # 오른쪽 전파
    cur = d
    for i in range(t, 3):
        if state[i][0] != state[i][1]:
            cur *= -1
            rot_dir[i+1] = cur
        else: break

    # 동시에 회전
    for i in range(4):
        if rot_dir[i]:
            cogwheel[i].rotate(rot_dir[i])

🎯 결과

상태 저장 → 계획 작성 → 동시에 적용

옆 톱니 연쇄 회전이 정확히 동작

2. 입력 처리
   ❌ 틀린 코드
   cogwheel = [deque(map(int, input().split())) for _ in range(4)]

문제: "10101111" 같은 입력이 deque(['10101111']) → deque([10101111]) 꼴로 들어감

✅ 수정한 코드
cogwheel = [deque(map(int, input().strip())) for _ in range(4)]

🎯 결과

원하는 형태 deque([1,0,1,0,1,1,1,1])로 저장

rotate() 동작 검증 가능

3. 톱니 번호
   ❌ 틀린 코드
   target, direction = map(int, input().split())
   simul(target, direction)

문제: 입력 번호는 14, 인덱스는 03 → 한 칸씩 밀려서 잘못 회전

✅ 수정한 코드
target, direction = map(int, input().split())
simul(target-1, direction)

🎯 결과

문제 번호와 배열 인덱스 맞춤

정확히 원하는 톱니 회전

✨ 최종 교훈

전파는 “저장 후 동시 적용”

입력은 split vs strip 구분

인덱스는 1-based vs 0-based 보정
