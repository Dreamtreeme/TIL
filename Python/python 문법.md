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

# 리스트 표현
# 0개 이상의 객체를 포함 , 데이터 목록을 저장
# 대괄호로 표기
# 데이터는 어떤 자료형도 저장 할 수 있음.


# 튜플 표현
- 0개 이상의 객체를 포함, 데이터 목록을 저장
- () 소괄호로 표기
- 단일 요소 튜플을 만들 때 반드시 후행쉼표를 넣어야함
- 않넣으면 기본자료형으로 됨

## 튜플 시퀀스 특징
- 인덱싱, 슬라이싱, 길이는 똑같다
### 튜플은 불변!!
- 불변 특성을 사용하여 내부동작과 안전한 데이터 전달에 사용됨
- 다중 할당, 값 교환, 그룹화, 함수 다중 반환 값등

## range
- 연속된 정수 시퀀스를 생성
### range(시작값, 끝 값, 증가 값)
#### range(n)
- 0부터 n-1까지 1씩 증가
#### range(n,m)
- n부터 m-1까지의 1씩증가
#### range(n,m,step)
- n부터 m-1까지 step만큼 증가


## dict 딕셔너리
- key 와 value로 이루어져있음
- 순서와 중복이 없는 변경 가능한 자료형
- {}중괄호로 표기
- 해시 테이블로 구성됨

# list/dict 가장중요-> 알고리즘, API활용
- list 는 순서별로 알고리즘 풀이를 저장
- dict는 json파일같은 형태로 데이터를 받음

---
# 형변환

## 암시적인 형변환
- 파이썬이 자동으로 수행
- 자료형이 높은 쪽으로 형변환
- ex boolean<int<float

## 명시적 형변환
- str -> int : 형식에 맞는 숫자만 가능
- int -> str: 모두 가능

# 단축평가

a and b => b까지 가서 실행
b and a => b에서 끝

## 뒤에를 안보는 케이스가 생긴다

## 시퀀스형 연산
- +는 결합 *는 반복

