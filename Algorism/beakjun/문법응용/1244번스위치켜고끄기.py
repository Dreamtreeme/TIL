'''
8                   스위치 갯수
0 1 0 1 0 0 0 1     스위치 상태 1은 켜짐 0은 꺼짐
2                   학생수
1 3                 성별    받은 번호
2 3                 2는 여자
'''

switch_cnt = int(input())
switch_state = list(map(int, input().split()))
s_n = int(input())

for i in range(s_n):
    student = list(map(int, input().split()))
    num = student[1]
    if student[0] == 1 : #남학생일 경우 받은 배수면 그 스위치 번호 상태반전
        for j in range(1,switch_cnt+1):
            if j%num:
                continue
            switch_state[j-1] ^= 1

    else:               # 여학생일 경우 받은 숫자 상태 반전후, 좌우부터 대칭검사
        switch_state[num-1] ^= 1
        cnt=1
        while True:
            
            if (num-1+cnt)>=switch_cnt or (num-1-cnt)<0:
                break
            
            if switch_state[num-1-cnt] == switch_state[num-1+cnt]:
                switch_state[num-1-cnt] ^=1
                switch_state[num-1+cnt] ^=1
                cnt+=1
            else:
                break
for k in range(0, switch_cnt, 20):
    # switch_state 리스트에서 현재 줄에 해당하는 부분을 슬라이싱 
    line_of_switches = switch_state[k : k + 20]

    # 가져온 부분 리스트의 요소(정수)들을 문자열로 변환하고 공백으로 연결
    print(" ".join(map(str, line_of_switches)))

