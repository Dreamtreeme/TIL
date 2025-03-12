# [0,1,2] 3개의 카드가 존재
# 2개를 뽑을 예정

path = [] # 뽑은 카드를 저장하는 변수
# cnt = 재귀호출 마다 누적되어서 전달되어야 하는 값
used = [False]*7


# 조금 더 어려운 문제의 경우
# 딕셔너리,셋 이런 자료구조로 해결
def recur(cnt):
    
    # 종료조건
    if cnt ==3:
        # 종료시 해야할 로직들 구성
        print(*path)
        return
    
    for num in range(1,7):
        # 이미 num을 뽑앗다면 뽑지마라
        # if num in path:
        #     continue
        if used[num] is True:
            continue

        used[num] = True
        path.append(num)# 1. 1개의 카드를 뽑는다
        recur(cnt +1)# 2. 다음 재귀 호출 (뽑은 카드가 1개 추가됨)
        path.pop()
        used[num] = False
    
    
    # 제일 처음 호출 할 때 
    # 초기 값을 전달하면서 시작
recur(0)