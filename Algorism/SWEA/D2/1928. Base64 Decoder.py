t = int(input())

base64 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for case in range(1, t + 1):
    # 1. 입력받은 문자를 십진수 숫자로 받기
    # 입력 받은 문자는 모두 base64에 포함된 기호다
    # 그리고 base64는 인덱스번호대로 써져있기때문에 인덱스번호 = 해당하는 십진수 숫자이다
    # 그렇기 때문에 입력받은 문자를 일단 받는다
    input_string = input()
    # 그리고 이진수를 넣어둘 공간을 만들어 놓는다
    binary_list =""
    # input_string 안의 문자들을 반복하기 위해선 시퀸스 문자 반복 생각
    for char in input_string:
        index_num = base64.find(char)
        # 인덱스 번호를 bin()을 사용해 이진수로 바꾸면
        # ob01010 이렇게 나오기 때문에 슬라이싱을 이용해 컷
        # 문제에 "버퍼의 위쪽부터 6비트씩 잘라 그 값을 읽고"
        # 지문으로 보아 64 숫자까지 표현할 수 있는 자리인 6자리까지 0을 채운다
        # zfill을 이용하면 왼쪽에 6자리 될때까지 넣어줌
        binary_num = bin(index_num)[2:].zfill(6)
        # binary_num엔 이제 100100 형식으로 이진수가 들어가있다.
        # 이 문자열을 전부 더해준다
        binary_list += binary_num
    
    # decoded_string 처럼 디코딩된 문자열을 넣어놀 공간을 만든다
    result = ""
    # 이제 binary_list에 들어있는 이진수들을 10진수로 변환하고
    # 다시 아스키 코드 값으로 변환해야한다.
    # 반복을 돌려서 0부터8까지 9부터 16까지 식으로 해야함
    # range문의 (첫째 인덱스, 마지막 인덱스, 몇칸씩 건너뛸건지)를 이용
    for i in range(0, len(binary_list), 8):
        byte = binary_list[i:i+8] # i번째부터 i+8전까지
        decimal = int(byte, 2) # byte숫자를 2진수형식으로 인식 10진수로
        result += chr(decimal)
    print(f'#{case} {result}')