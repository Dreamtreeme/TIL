# CSS
웹 페이지의 디자인과 레이아웃을 구성하는 언어

구성

1. 선택자
2. 선언
    3. 속성
    4. 값

## 스타일 시트 방법
1. 인라인
태그 헤드에 쓰는 방식 선호X
2. 내부 스타일
헤드 영역에 쓰는법
3. 외부 스타일
외부 파일을 불러오는 방법

## CSS 셀렉터
HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

1. 기본 선택자
- 전체 * 선택자
    모든 요소 선택
- 요소(tag) 선택자
    지정한 모든 태그를 선택
- 클래스 선택자
    주어진 클래스 속성을 가진 모든 요소 선택, 재사용을 위해
- 아이디 선택자
    주어진 아이디 속성을 가진 요소
    문서에는 아이디를 가진 요소가 하나만 있어야함
- 속성 선택자

2. 결합자
- 자손결합자
" " 
    예시 p span -> p 안에 있는 모든 span을 선택
- 자식 결합자
">"
ul > li -> ul안에 모든 한단계 아래 li를 선택
부모 태그 안에 컨텐츠로 들어가야 자식임


3. 명시도
선택자에 가중치를 계산하여 우선순위가 높은 순으로 적용

    1. important
    Cascade의 구조를 무시하고 강제로 스타일 적용방식으로
    사용권장하지 않음
    2. 인라인 스타일
    3. 선택자
        id> class> 요소 -> 좁은 법위의 선택일수록 명시도 높음
    4. 소스 코드 선언 순서 

- 명시도 순서를 생각하는거보다 class선택자만 사용

### CSS 상속
부모 요소를 자식에게 상속해 재사용성을 높임

- 상속이 되는 속성
    text관련 요소
- 상속이 안되는 속성
    box model 관련요소
    position 관련요소

### CSS BOX Model
모든 요소를 지정하는 box영역

1. Block box: 아래로감
    항상 새로운 행으로 나뉨-> 오른쪽 구역을 다 차지
    요소: h1~h6, p, div
2. Inline box: 오른쪽으로감
    a, img, span, strong, em

MDN Web Docs 
    웹 기술에 대한 정보 제공
