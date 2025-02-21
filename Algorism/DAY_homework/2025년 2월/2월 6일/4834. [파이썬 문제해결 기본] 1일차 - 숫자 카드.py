# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.

# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

# [입력]


# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )

# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )

# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

# [출력]

# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

'''
풀이추론:
N장의 카드가 주어지고 카드들중 중첩된 숫자 카드의 종류와 갯수를 구하기
정수인 숫자만 주어지기 때문에
카운팅 정렬의 1단계인 중첩갯수와 종류를 구하는 방식을 이용가능
'''

T = int(input())
for case in range(1,T+1):
    li_len = int(input())
    num = input()
    li = list(map(int, num))
    
    mav_v = li[0]
    for i in li[1:]:
        if mav_v<i:
            mav_v=i
    count = [0]*(mav_v+1)

    for i in range(li_len):
        count[li[i]] += 1
    
    # count 에는 각 인덱스마다 카운트된 숫자가 기록
    max_count = count[0]
    max_num = 0
    for i in range(1, mav_v+1): # 카운트 인덱스 순회
        if max_count<=count[i]: # 임의의 요소보다 다음요소가 크면
            max_count=count[i] # 요소를 바꿔라
            max_num = i # 그리고 그 인덱스 번호를 넣어라
            


    print(f'#{case} {max_num} {max_count}')