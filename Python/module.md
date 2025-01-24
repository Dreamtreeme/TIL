## 모듈

다른 프로그래머가 이미 작성해 놓은 코드들을 활요하는것

```jsx
import math => 임포트를 사용해서 모듈을 불러옴

print(math.pi) # 3.141592...

print(math.sqrt(4)) # 2.0

from math import sqrt => 모듈 안의 함수 또는 변수를 가져오는 방법
```

### dot 연산자

- 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라

```jsx
module.function
```

### 주의사항

- 서로 다른 모듈이 같은 이름의 함수를  제공할 경우 문제 발생
- 마지막에 import 된 이름으로 대체됨
- 그렇기 때문에 모든 요소를 한번에 import 하는 * 표기는 권장하지 않음

### ‘as’키워드

- 별칭을 부여해 이름 충돌 해결

```jsx
from math import sqrt
from my_math import sqrt as my_sqrt
```

## 파이썬 표준 라이브러리

PSL

Python Standard Library

파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

### 패키지

연관된 모듈들을 하나의 디렉토리에 모아 놓은 것 (모듈<패키지<라이브러리)

### 외부 패키지🌟🌟

- pip를 사용하여 설치 후 import 필요

### Pip 파이썬 패키지 관리자

https://pypi.org/

### 패키지 설치

- 최신 버전 특정버전 최소버전을 명시하여 설치할 수 있음

```bash
$ pip install Pakage version
```

### requests 패키지

- 외부 API 서버로 요청

### 패키지 사용 목적

모듈들의 이름공간을 구분하여 충돌을 방지

모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할

## 제어문

코드의 실행 흐름을 제어하는데 사용되는 구문

조건에 따라 코드 블록을 실행하거나 반복적으로 코드를 실행

## 조건문 - 주어진 조건식을 평가하여 참일 경우에만 실행

if, elif, else

```bash
if 표현식:
		코드 블록
elif 표현식:
		코드 블록
else:
		코드 블록
		
```

조건식을 동시에 검사하는것이 아니라 순차적으로 비교

- 반복문 - 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
    
    for 특정 작업을 반복적으로 수행
    

```bash
for 임시변수 in 반복 가능한 객체:
		코드 블록

for item in items: # 뒷 변수는 여러개, 앞 변수는 단일객체, 단일객체가 반복된다고 생각하면 편함
		print(item)
```

for 문 작동원리

- 리스트 내 첫 항목이 실행되고 반복

```
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)

country = 'Korea'

for char in country:
    print(char)

my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])

numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)): # 알고리즘에서 활용
    numbers[i] = numbers[i] * 2

print(numbers)  # [8, 12, 20, -16, 10]

outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)

# 반복 충첩문은 [첫째중첩문, 둘째중첩문, ...]순으로 시작해서
# 뒷자리 부터 순서가 증가

elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print(elem)  # ['A', 'B'] ['c', 'd']

for elem in elements:
    for item in elem:
        print(item)  # A B c d

```

## while - 조건이 참이 동안 반복해서 실행

```bash
while a<3:
	print(a)
	a +=1
	
	# 3번 실행되는 이유는 종료 조건이 3회 이후 실행되기 때문
```

## while 문은 종료 조건이 꼭 필요

## 적절한 반복문 활용

- for
    - 반복 횟수가 명확하게 정해져 있는 경우
    - 예를 들어 리스트,튜플 문자열 등과 같은 시퀀스 형식 데이터 처리
- while
    - 사용자의 입력을 받는 경우

## 반복문 제어 키워드

- break
    - 제어문을 끝냄
- continue
    - 밑의 코드를 실행하지 않고 다음 반복을 실행
- pass
    - 아무 작업 안함
    - 구현해야 할 부분이 나중에 추가되야하면 미완성 부분에 pass를 입력
    - 조건문에서 아무런 동작을 수행하지 않아야 할때
    - 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행하는 방법

## 리스트 컴프리헨션 구조

```python
# 기존 방식
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2) # 리스트에 값 추가

# print(squared_numbers)

# 리스트 컴프리헨션
squared_numbers2 = [num**2 for num in numbers]

print(squared_numbers2)

# List Comprehension 활용 예시 - "2차원 배열 생성 시 (인접행렬 생성 시)"
data1 = [[0] * (5) for _ in range(5)]
print(data1)
# 또는
data2 = [[0 for _ in range(5)] for _ in range(5)]
print(data2)

"""
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
"""

# 리스트 컴프리헨션 with 조건문
# 기존 방식
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

print(evens)  # [0, 2, 4, 6, 8]

# 리스트 컴프리헨션
evens = [x for x in range(10) if x % 2 == 0]

# 코드의 길이가 줄어든다해서 가독성이 좋진않다
print(evens)  # [0, 2, 4, 6, 8]

```

### 모듈 내부 살펴보기

- 내장 함수 help를 사용해 모듈에 무엇이 들어있는지 확인 가능

### enumerate - 인덱스와 요소가진 튜플을 뱉어줌

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

"""
0 apple
1 banana
2 cherry
"""

for index, fruit in enumerate(fruits, 3):
    print(index, fruit)

"""
3 apple
4 banana
5 cherry
"""

```

- 파이썬이 어떤 폴더를 패키지로 인식하려면 폴더 안에 `__init__.py` 파일이 있어야 함(빈 파일이어도)