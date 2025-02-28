'''
삼성전자는 수원삼성 구단의 홍보를 위해 축구장에 4행, n열 크기의 LED 디스플레이를 설치하였다
디스플레이의 각 픽셀은 1과 0의 2가지 상태를 가지며 일정한 주기로 다음과 변한다
픽셀 i+j+1이 시간k의 배수이면 다른 상태로 바뀐다

시간 k=0일때 각 픽셀은 0으로 초기화 되어있다

가로크기 n과 시간 k가 주어질때, 1상태에 있는 픽셀의 숫자를 구하라
입력
4
5 3
35 39
93 70
569 138
출력
#1 10
#2 20
#3 123
#4 1175
'''

T= int(input())
for tc in range(1,T+1):
    result=0
    #행의 갯수
    r=4
    #열의 갯수와 시간값
    c, k= map(int, input().split())

    #0으로 이루어진 배열생성
    display=[[0]*c for _ in range(4)]
    #k번 돌아야함.. 많이도 돈다
    for t in range(1,k+1):

        # k초당 디스플레이 배열 바꿈
        for i in range(4):
            for j in range(c):
                if (i+j+1)%t==0:
                    display[i][j]=1-display[i][j]
    # 최종 정렬된 배열의 1값 다 더하기
    for i in range(4):
        result+=sum(display[i])
    print(f'#{tc} {result}')
