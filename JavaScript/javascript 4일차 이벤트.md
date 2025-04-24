## event handler
특정 이벤트가 발생했을 때 실행되는 콜백함수
보통 addEventListener 를 통해 DOM요소에 등록

### 등록방법

// 이벤트 핸들러
    const handleClick = function () {
      window.alert('버튼이 클릭 되었습니다!')
    }

    // addEventListener 메서드를 이용해 버튼에 이벤트 핸들러를 등록
    button.addEventListener('click', handleClick)

1. 클릭시 실행될 함수 선언후 변수에 집어넣음
2. 실행 객체에 button.addEventListener('실행동작 이벤트', 함수)로 등록

함수자체를 인자로 넘기는 이유는 click 되었을때 함수가 실행되어야 하기때문


### 버블링
- 한 요소에 이벤트가 발생하면, 이요소에 할당된 핸들러가 동작하고, 이어서 부모 요소의 핸들러가 동작하는 현상

- 가장 최상단 조상 요소를 만날때까지 반복되면서 각 요소에 할당된 핸들러가 동작

### 갭처링
- 이벤트가 하위 요소로 전파되는 단계
