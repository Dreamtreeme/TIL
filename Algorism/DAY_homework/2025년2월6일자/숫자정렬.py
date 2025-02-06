# 제약 조건
# N은 5이상 50이하
# 모든 숫자는 양의 정수이다

T = int(input())
for case in range(1,T+1):
    N =int(input()) #len 함수 대신 입력받은 길이 설정
    result= [0]*N # 입력받은 길이만큼 정답 리스트 만들어두기
    li = list(map(int, input().split())) # 입력 리스트 만들기
    max_v=li[0] # 입력 리스트의 최대값 임의 설정
    for i in li[1:]: # 최대값 찾는 반복문
        if max_v<i:
            max_v=i
    count_len =max_v+1 #카운팅 리스트 길이 설정, 입력 리스트 요소의 최대값+1
    count = [0]*count_len # 카운팅 리스트 생성

    for i in range(N): # 입력 리스트 길이만큼 반복, 리스트내 중첨 요소 갯수 확인
        count[li[i]] +=1 # 카운트 리스트 인덱스 번호에 입력리스트 요소값 사용, 그 후 더하기1

    for i in range(1, count_len): # 누적합 구하는 반복문, 카운트 인덱스1번부터 끝까지
        count[i] += count[i-1] # 전의 카운트 요소값+현재 카운트 요소값

    for i in range(N-1, -1, -1): # 정렬 반복문, 입력 인덱스 길이-1 번째부터, 거꾸로, -1씩 감소, 
        count[li[i]] -=1 #카운트 리스트에서 입력리스트 숫자 만나면 -1
        result[count[li[i]]] = li[i] # 입력 리스트의 숫자위치가 저장된 카운팅 리스트의 숫자를 결과값 인덱스 번호로 사용
    result = " ".join(map(str, result))

    print(f'# {case} {result}')