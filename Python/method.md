## 자료구조

- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

### 매서드(method)

- 객체에 속한 함수 → 객체의 상태를 조작하거나 동작을 수행
- 매서드는 클래스 내부에 정의되는 함수
- 클래스는 파이썬에서 ‘타입을 표현하는 방법’ 이다
- str() 도 클래스였다

```python
def add(a,b):
    return a+b

class Calculator:
    def add(self, a,b):
        return a+b
    
#함수 호출
add(1,2)

#매서드 호출
a= Calculator()
a.add(1,2)
```

### find - 문자열 데이터를 순회하며 인자의 값을 찾아서 인덱스 번호를 리턴

```python
text = 'banana'
print(text.find('a'))
print(text.find('z')) #못찾으면 -1
```

### index - 인자의 첫 번째 위치를 반환 없으면 오류 발생

```python
# index - 인자의 첫 번째 위치를 반환 없으면 오류 발생
print(text.index('a'))
# print(text.index('z')) - 오류

```

## is로 시작하는 메서드들의 반환값은 Boolean 인게 대부분

### isupper - 문자열이 모두 대문자/소문자로 이루어져 있는지 확인

```python
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # true
print(string2.isupper())  # false
```

### islower, isalpha

```python
# islower
print(string1.islower())  # false
print(string2.islower())  # false

# isalpha
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # true
print(string2.isalpha())  # false
```

## 핵심 문자열 조작 메서드

### .replace(old, new[,count]) -대괄호 안에 있는건 선택적 옵션

```python
# replace- 새로운 문자열을 반환해줌
text = 'Hello, world! world world'
new_text1 = text.replace('world', 'Python')
new_text2 = text.replace('world', 'Python', 1)
print(new_text1)  # Hello, Python! Python Python
print(new_text2)  # Hello, Python! world world
print(text) # 원본은 불변
```

### .strip([chars]) - 문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거

```python
# strip
text = '  Hello, world!  '
new_text = text.strip()
print(new_text) # Hello, world!
```

### .split( sep=None, maxsplit= -1)

### 구분자를 문자열로 사용하여 문자열에 있는 단어들의 리스트를 반환

```python
# split
text = 'Hello, world!'
words1 = text.split(',') # 쉼표를 기준으로 나눔
words2 = text.split() #아무 인자도 없으면 공백기준으로 나눔
print(words1)  # ['Hello', ' world!']
print(words2)  # ['Hello,', 'world!']

```

### ‘separator’.join( iterable)

- iterable의 문자열을 연결한 문자열을 반환

```python
# join
words = ['Hello', 'world!',3 ,100]
new_text = '-'.join(words)
print(new_text)  # Hello-world!
```

### 

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8a49879-6cfd-4067-b244-5980cbb53e13/7116a74c-0d2b-4516-b16e-09bfc8432b48/image.png)

```python
# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!

# reversed
```

## 리스트 값 추가 및 삭제 메서드

- 시퀀스와 다르게 원본을 바꾼다 - 반환값이 없다

### L.append(x) - 리스트 마지막에 항목x를 추가

```python
# L.append(x) - 리스트 마지막에 항목x를 추가
my_list = [1, 2, 3]

print(my_list.append(4))  # [1, 2, 3, 4]
```

### L.extend(m) - iterable m 의 모든 항목들을 리스트 끝에 추가(+=과 같은기능)

```python
# extend
my_list = [1, 2, 3]
my_list.extend([4,5,6])
print(my_list)  # [1, 2, 3, 4, 5, 6]

# append와의 비교
my_list.append([4,5,6])
print(my_list)

# 반복 가능한 객체가 아니면 추가 불가
```

### L.insert(i, x) - 리스트 인덱스 i에 항목 x를 삽입

```python
# insert
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)  # [1, 5, 2, 3]
```

### remove - 리스트 가장 왼쪽에 있는 항목을 제거

```python
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)  # [1, 3, 2, 2, 2]
```

## L.pop - 리스트 가장 오른쪽에 있는 항목을 ✨반환 후 제거

```python
# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list.pop()
item2 = my_list.pop(0) # 인덱스 번호를 지정하면 인덱스i에 있는 항목 반환 후 제거

print(item1)  # 5
print(item2)  # 1
print(my_list)  # [2, 3, 4]
```

### L.clear() - 리스트 항목들 삭제

```python
# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # []
```

### index, count 함수

```python
# index
my_list = [1, 2, 3]
index = my_list.index(0)
print(index)  # 1

# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3
```

### L.reverse() - 리스트의 순서를 역순으로 변경( 정렬x )

```python
# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)  # [9, 1, 8, 2, 3, 1]
print(my_list.reverse())  #None
```

L.sort() - 리스트의 순서를 정렬

```python
# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
```

## 복사

### 변수 할당의 의미

- 파이썬에서 변수 할당은 객체에 대한 참조를 생성하는 과정
    - 변수는 객체의  메모리 주소를 가리키는 Label 역할을 함
    - ‘=’ 연산자를 사용하여 변수에 값을 할당
    - 할당 시 새로운 객체가 생성되거나 기존 객체에 대한 참조가 생성됨

### 가변과 불면 메모리 관리 방식

- 가변 객체
    - 생성 후에도 그 내용을 수정할 수 있음
    - 객체의 내용이 변경되어도 같은 메모리 주소를 유지
    
- 불변 객체
    - 생성 후 그 값을 변경할 수 없음
    - 새로운 값을 할당하면 새로운 객체가 생성되고, 변수는 새 객체를 참조하게 됨

이유

1. 성능 최적화
    - 불변 객체는 변경이 불가능하므로, 여러 변수가 같은 객체를 안전하게 공유
    - 가변 객체는 새 객체를 생성하지 않고 직접 수정
2. 메모리 효율성
    - 동일한 값을 가진 여러 객체가 메모리를 공유
    - 가변 객체는 크기가 큰 데이터를 효율적으로 수정

### 얕은 복사

- 객체의 최상위 요소만 새로운 메모리에 복사하는 방법
- 내부에 중첩된 객체가 있다면 그 객체의 참조만 복사됨

```python
# ================================================
# 얕은 복사
# ================================================
print('\n얕은 복사 예시')

# 1차원 리스트
a = [1, 2, 3]
b = a[:]  # 슬라이싱
c = a.copy()  # copy() 메서드
d = list(a)  # list() 함수

b[0] = 100
c[0] = 999
d[0] = 8080
print(a)  # [1, 2, 3]
print(b)  # [100, 2, 3]
print(c)  # [999, 2, 3]
print(d)  # [8080, 2, 3]
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8a49879-6cfd-4067-b244-5980cbb53e13/c6bc2d9f-d3fd-4223-8340-17129615a546/image.png)

```python
# 다차원 리스트
print('\n다차원 리스트 얕은 복사의 한계')
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  #[1, 2, [3, 4, 5]]
print(b)  #[999, 2, [3, 4, 5]]

b[2][1] = 100
print(a)  #[1, 2, [3, 100, 5]]
print(b)  #[999, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  #True

```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8a49879-6cfd-4067-b244-5980cbb53e13/01bb5a26-9338-48bc-99ac-8eb00a60db61/image.png)

### 1차원 리스트는 얕은 복사로 해결 가능하지만

### 다차원 리스트는 안의 리스트 요소들까지 복사가 되지 않는다

### 깊은복사

- copy 모듈에서 제공하는 deepcopy() 함수를 사용

```python
# ================================================
# 깊은 복사
# ================================================
import copy

print('\n깊은 복사 예시')
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [1, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False
```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8a49879-6cfd-4067-b244-5980cbb53e13/faba8e8c-9b8e-4f90-9400-9f133955766e/image.png)

```python
# 복잡한 중첩 객체 예시
print('\n복잡한 중첩 객체 깊은 복사')
original = {
    'a': [1, 2, 3],
    'b': {
        'c': 4,
        'd': [5, 6],
    },
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  #{'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  #{'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f'original["b"]와 copied["b"]가 같은 객체인가? {original["b"] is copied["b"]}'
)  #False

```

![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/a8a49879-6cfd-4067-b244-5980cbb53e13/b44447f4-9579-4014-b30f-6775a1d83936/image.png)

### 메서드 체이닝

```python
# 문자열 메서드 체이닝
text = 'heLLo, woRld!'
new_text = text.swapcase().replace('l', 'z')
print(new_text)  # HEzzO, WOrLD!

# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1)  # HEllO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 한 줄로 실행하기 (위와 동일한 결과)
new_text = text.swapcase().replace('l', 'z')
print('최종 결과:', new_text)  # HEzzO, WOrLD!
```

### 주의점 - 반환값이 중간에 없는 매서드를 수행해버리면 뒤의 메서드가 안됨

```python
# 리스트 메서드 체이닝 예시

# 잘못된 체이닝 방식 1
numbers = [3, 1, 4, 1, 5, 9, 2]
result = numbers.copy().sort()
print(result)  # None (sort()는 None을 반환하므로 체이닝이 중단됨)
print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)

# 잘못된 체이닝 방식 2
result = numbers.append(7).extend([8, 9])  # AttributeError
```

```python
# 개선된 방식
# 리스트 조작에서 메서드 체이닝을 사용할 때는 각 메서드가 적절한 값을 반환하는지 확인하고,
# 필요한 경우 새로운 리스트 객체를 반환하는 함수를 사용하는 것이 좋음
sorted_numbers = sorted(numbers.copy())
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]
```