T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer =0
    n = list(map(int, input().split()))
    li =[]
    for i in n: # 핵심! 리스트에 포문을 사용하면 i는 각 리스트의 요소를 뜻한다
        if (i%2) ==1:
            li.append(i)
    answer =sum(li)
    print(f'#{test_case} {answer}') 
