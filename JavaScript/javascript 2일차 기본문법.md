## 기본 문법

### 변수선언

let : block scope 영역 내부에서만 동작,재할당 가능, 재선언 불가능

const : block scope 영역 내부에서만 동작,재할당 불가능, 재선언 불가능

<!-- var 는 호이스팅 현상 때문에 제어할 자신이 없으면 안쓰는게 좋다-->

### 데이터 타입

1. 원시 자료형(Primitive type)
    변수에 값이 직접 저장되는 자료형(불변, 값이 복사)

    - Number
        정수 또는 실수형 숫자
    - String
        - '+' 연산자를 사용해 문자열끼리 결합
        - 뺄셈 곱셈 나눗셈 불가능

        Template literals
            - 백틱(``)을 이용하며, 여러줄에 걸쳐 문자열을 정의,
            변수를 문자열 안에 바로 연결할 수있음
            - '$' 와 중괄호로 표기
            예시) `홍길동은 ${age}세 입니다.`
    - Boolean
        true, false
        null
        undefined 항상 false
        Number 0,-0, NaN false
        String '' 만 false
    - null
    - undefined

2. 참조 자료형(Reference type)
    객체의 주소가 저장되는 자료형(가변, 주소가 복사)

    objects(object, Array, Function)


### 연산자
- 동등연산자(==): 
두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
암묵적 타입 변환을 통해 타입을 일치시킨후 같은 값인지 비교

- 일치연산자(===):
두 피연산자의 값과 타입이 모두 같은 경우 true를 반환


### 조건문
 const name = 'customer'

    if (name === 'admin') {
      console.log('관리자님 환영해요')
    } else if (name === 'customer') {
      console.log('고객님 환영해요')
    } else {
      console.log(`반갑습니다. ${name}님`)
    }

### 삼항연산자
A?true:false
조건 A를 확인하고 true면 왼쪽 false는 오른쪽 값을 반환

### 반목문 종류

- while
    while (조건문){

    }

- for -> let을 씀
    for ([초기문]; [조건문]; [증감문]){

    }

- for of -> const 를 씀
    반복 가능한 객체(배열 문자열에)대해 반복
    // for...of
    const numbers = [0, 1, 2, 3]

    for (const number of numbers) {
      console.log(number) // 0, 1, 2, 3
    }

    const myStr = 'apple'

    for (const str of myStr) {
      console.log(str) // a, p, p, l, e
    }


- for in -> const씀
    for (variable in object){
        variable =...
        객체의 열거 가능한 속성 에 대해 반복
    }

### 함수
참조 자료형에 속하며 모든 함수는 Function object

- 선언식
    함수를 선언하는 방법
    호이스팅 현상이 일어날 수 있다.

- 표현식
    익명함수
    // 함수 표현식
    const sub = function (num1, num2) {
      return num1 - num2
    }

    // 나머지 매개변수 (가변 인자)
    const myFunc = function (num1, num2, ...restArgs) {
      return [num1, num2, restArgs]
    }

- 화살표 함수 표현식

    const arrow1 = function (name) {
      return `hello, ${name}`
    }
    // 1. function 키워드 삭제 후 화살표 작성
    const arrow2 = (name) => { return `hello, ${name}` }

    // 2. 인자의 소괄호 삭제 (인자가 1개일 경우에만 가능)
    const arrow3 = name => { return `hello, ${name}` }

    // 3. 중괄호와 return 삭제 (함수 본문이 return을 포함한 표현식 1개일 경우에만 가능)
    const arrow4 = name => `hello, ${name}`