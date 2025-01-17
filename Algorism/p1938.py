#아주 간단한 계산기
# 입력 받기 (두개의 숫자가 공백을 띄고 주어짐)

nums = list(map(int, input().split()))
# input(): 주어진 "8 3" 받기
# input().split() : 문자열을 공백단위로 쪼갬
# map, int: 각각의 문자열을 숫자로 바꿈
# list로 모으기: [8,3]

a, b = nums #각 리스트 원소를 꺼내서 a b에 각각 배정
calculate(a,b)
def calculate(num1, num2):
    Add = max(num1, num2) + min(num1, num2)
    Subtraction  = max(num1, num2) - min(num1, num2)
    Multiplication = max(num1, num2) * min(num1, num2)
    Division = max(num1, num2) / min(num1, num2)

    print(Add)
    print(Subtraction)
    print(Multiplication)
    print(Division)
    