import sys
input = sys.stdin.readline

def solution(new_id):
    # 1단계: 소문자로 치환
    case1 = new_id.lower()
    
    lower = [chr(i) for i in range(ord('a'), ord('z')+1)]
    number = [str(i) for i in range(10)]
    case2 = ""   # case 변수명은 case2로 맞춰줌

    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 제외한 모든 문자 제거
    for i in case1:
        if i in lower or i in number or i in ["-", "_", "."]:
            case2 += i
    
    # 3단계: 마침표 2번 이상 연속된 부분 하나의 마침표로
    while ".." in case2:
        case2 = case2.replace("..", ".")
    
    case3 = case2
    
    # 4단계: 마침표가 처음이나 끝에 위치한다면 제거
    if len(case3) > 0 and case3[0] == ".":
        case3 = case3[1:]
    if len(case3) > 0 and case3[-1] == ".":
        case3 = case3[:-1]
    
    # 5단계: 빈 문자열이라면 "a" 대입
    if case3 == "":
        case3 = "a"
    
    # 6단계: 16자 이상이면 15자까지만 남기고 끝이 '.'이면 제거
    if len(case3) >= 16:
        case3 = case3[:15]
        if case3[-1] == ".":
            case3 = case3[:-1]
    
    # 7단계: 길이가 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복
    while len(case3) < 3:
        case3 += case3[-1]
    
    answer = case3
    return answer

new_id = input().strip()
print(solution(new_id))
