def KFC(num):

    # 재귀 호출 중지
    # 특징 1. 종료조건과 함께함
    if num == 5:
        return
    # 재귀 호출 전 들어가야할 로직
    print(num ,end=' ')
    KFC(num+1)
    KFC(num+1)  # 트리 중위 순회처럼 작동한다
    # 돌아 오면서 해야 할 로직
    print(num ,end=' ')

KFC(0)
print("끝")