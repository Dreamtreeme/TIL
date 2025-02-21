# 그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.

# N개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.

# 주어진 정보에서 같은 색인 영역은 겹치지 않는다.

'''
10*10 격자 정보 주어짐
빨간색, 파란색 칠할부분 좌표 만들어야함
둘이 겹치는지 확인하는 방법은 칠하면 1증가 식으로 2이상이면 보라색
같은 색의 영역은 겹치지 않는다 = 먼저 빨간색 그리기, 어차피 안겹침
'''

T= int(input())
for case in range(1,T+1):
    result=0
    matrix = [[0]*10 for _ in range(10)]
    rec_kind=int(input())
    for _ in range(rec_kind):
        r1, c1 ,r2, c2, color= list(map(int, input().split()))
        print(color)

        if color==1: # 빨간색인경우
            for i in range(10): # 격자 100칸 전체 순회
                for j in range(10):
                    if r1 <= i <= r2 and c1 <= j <= c2:
                        matrix[i][j]+=color
        else: #파란색인 경우
            for i in range(10): # 격자 100칸 전체 순회
                for j in range(10):
                    if r1 <= i <= r2 and c1 <= j <= c2:
                        matrix[i][j]+=color
    
    for i in range(10):
        for j in range(10):
            if matrix[i][j] ==3:# 보라색인 경우
                result+=1


    print(f'#{case} {result}')
