## DOM

### JavaScript 탄생(1995)
Brendan Eich 는 웹 동적 기능 개발이라는 회사의 요구사항을 넘어 Mocha언어를 개발, 이후 LiveScript로 변경했으나 JavaScript로 변경

Netscape Navigator 2.0에 탑재되어 웹페이지에 동적기능을 추가하는데 사용됨

### ECMA Script 출시 1997
- javaScript의 파편화를 막기위해 ECMA 에서 ECMAScript 표준 언어 정의

### Chrome 브라우저 2008

ECMAScript를 가장 잘 지켰고 가장 빠른 성능을보여 호환성이 높아지고 일관된 웹 페이지를 볼 수 있게됨.

### ECMAScript 와 JavaScript

- JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
- ECMAScript의 명세를 기반으로 하여 웹브라우저나 Node.js같은 환경에서 실행됨

- ES6에서 가장 중요한 버전으로 평가됨 2015

### 식별자(변수명) 작성 규칙
- 반드시 문자, 달러($) 또는 밑줄로 시작
- 대소문자를 구분
- 예약어 사용 불가
    - for, if , function 등

### Naming case

- 카멜케이스camelCase
    - 변수, 객체, 함수에 사용

- 파스칼 케이스
    - 클래스, 생성자에 사용

- 대문자 스네이크 케이스(SNAKE_CASE)
    - 상수(constants)에 사용

### 변수
1. let
    - 재할당 가능 -> 선언하는 시점에 값이 할당 안되도 됨.
    - 재선언 불가능
2. const
    - 재할당 불가능 -> 선언하는 시점에 값이 할당이 되야함
    - 재선언 불가능

### 블록스코프(block scope)

- if , for, 함수 등의 중괄호 내부를 가리킹
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

### const를 기본으로 사용해야 하는 이유
- 코드의 의도 명확화
    - 해당 변수가 재할당되지 않을 것임을 명확히 표현
    - 개발자들에게 변수의 용도와 동작을 더 쉽게 이해할 수 있게 해줌

- 버그 예방
    - 의도치 않은 변수 값 변경으로 인한 버그를 예방
    - 큰 규모의 프로젝트나 팀 작업에서 중요

### document 객체
웹 페이지의 최상위 객체

### DOM tree
- HTML 태그를 나타내는 elements의 node는 문서의 구조를 결정

### DOM 핵심
문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API