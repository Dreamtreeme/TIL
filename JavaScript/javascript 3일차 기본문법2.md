## 객체
키로 구분된 데이터 집합을 저장하는 자료형

- 중괄호{}를 이용해 작성
- 중괄호 안에는 key: value 쌍으로 구성된 속성을 여러개 작성가능
- key는 문자형만 허용
- value 는 모든 자료형 허용

const user = {
      name: 'Alice',
      'key with space': true,
      greeting: function () {
        return 'hello'
      }
    }
- .(chaining operator) 또는 []로 객체 요소 접근

    console.log(user.name)

- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

    console.log(user['key with space'])

- 객체는 이름을 const로 설정하면 이름자체는 변경할수없지만
    객체.value 로 안에있는 값들은 재할당 가능하다

### this keyword

const person = {
      name: 'Alice',
      greeting: function () {
        return `Hello my name is ${this.name}`
      },
    }

함수 자기자신을 지칭

// 1.1 단순 호출
    const myFunc = function () {
      return this
    }
    console.log(myFunc()) // window

    // 1.2 메서드 호출
    const myObj = {
      data: 1,
      myFunc: function () {
        return this
      }
    }
    console.log(myObj.myFunc()) // myObj

단순 호출은 전역변수의 this이기 때문에 window가 호출
메소드 호출은 메소드의 this이기 때문에 바로 위의 부모인 객체를 호출

### 객체 문법

1. 단축 속성
    const name = 'Alice'
    const age = 30

    const user = {
      name, age
    }

    키:밸류 형태로 정의 안해도 변수만 써도 됨.


const userInfo = {
      firstName: 'Alice',
      userId: 'alice123',
      email: 'alice123@gmail.com'
    }

    // const firstName = userInfo.name
    // const userId = userInfo.userId
    // const email = userInfo.email

    // const { firstName } = userInfo
    // const { firstName, userId } = userInfo
    const { firstName, userId, email } = userInfo

객체에 담겨있는 해당 키값을 이름으로 갖는 변수를 선언하면
한번에 구조 분해 할당됨.

### optional-chaining
// console.log(user.address.street) // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
    console.log(user.address?.street) // undefined

    // console.log(user.nonMethod()) // Uncaught TypeError: user.nonMethod is not a function
    console.log(user.nonMethod?.()) // undefined

    console.log(user.address && user.address.street) // undefined

    console.log(myObj?.address) // Uncaught ReferenceError: myObj is not defined

    // 위 예시 코드 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
    // user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문
- 즉 DB에 null,빈값허용만 ?를 사용하고 나머지 필수값은 사용안해도됨

### JSON

JavaScript Object Notation

JSON은 형식이 있는 문자열

- Object JSON 변환하기

// Object -> JSON
    const objToJson = JSON.stringify(jsObject)
    console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
    console.log(typeof objToJson)  // string

    // JSON -> Object
    const jsonToObj = JSON.parse(objToJson)
    console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
    console.log(typeof jsonToObj)  // object

### 콜백함수
다른 함수에 인자로 전달되는 함수

// 1
    const numbers1 = [1, 2, 3]
    numbers.forEach(function (num) {
      console.log(num)
    })

    // 2
    const numbers2 = [1, 2, 3]
    const callBackFunction = function (num) {
      console.log(num)
    }

    numbers.forEach(callBackFunction)

    둘은 같은 함수

## 주요 Array Method

- forEach 
    - 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출
    - 반환 값이 없음

    arr.forEach(callback(item[, index[, array]]))

    - 콜백함수는 3가지 매개변수로 구성
    1. item: 처리할 배열의 요소
    2. index: 처리할 배열 요소의 인덱스
    3. array: forEach를 호출한 배열


### forEach

 // 일반 함수 표기
    names.forEach(function (name) {
      console.log(name)
    })

    // 화살표 함수 표기
    names.forEach((name) => {
      console.log(name)
    })

    // 활용
    names.forEach(function (name, index, array) {
      console.log(`${name} / ${index} / ${array}`)
    })

### map
/ 1.2 map
    const result2 = persons.map(function (person) {
      return person.name
    })
    console.log(result2)


    // 2. 화살표 함수 표기
    const names = ['Alice', 'Bella', 'Cathy']

    const result3 = names.map(function (name) {
      return name.length
    })

    const result4 = names.map((name) => {
      return name.length
    })

    console.log(result3) // [5, 5, 5]
    console.log(result4) // [5, 5, 5]

map은 반환값을 배열에 모아서 반환해줌