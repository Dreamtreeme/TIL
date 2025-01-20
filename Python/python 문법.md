number = 10
double = 2* number
print(double)

number = 5
print(double)

## number가 뒤에 바뀌어도 double의 메모리 주소는 바뀌지 않는다
## 따라서 number의 첫째주소 *2를 한 값이 double에 할당되고 그 할당값은 다시 바뀌지 않는다.

### Data Types에 따라 연산에 결과가 달라진다

numeric 

int, float, complex

text Sequence type
str

Sequence types
list, tuple, range

Non-sequence types
set, dict

기타 
Boolean, None, Functions


## int

진수 표현
0b숫자 : 이진수
0o숫자 : 팔진수
0x숫자 : 16진수

## float 실수 자료형

d = 3.14
e = -2.7

# 314 * 0.01
number = 314e-2

# 3.14
print(number)

