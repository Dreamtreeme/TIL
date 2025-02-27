## 그리드시스템

-목적: 반응형 디자인을 지원해 웹 페이지를 모바일,태블릿,데스크탑등 다양한 기기에 적절하게 표시할 수 있게 하는기술

-부트스트랩의 그리드 시스템
    웹 페이지의 레이아웃을 조정하는 데 사용되는
    12개의 컴럼으로 구성된 시스템(약수가 젤 많은 수)

### 그리드 시스템 기본요소

1. Container
    Column들을 담고있는 공간

2. Column
    - 실제 컨텐츠를 포함하는 부분

3. Gutter
    - 컬럼과 컬럼 사이의 여백 영역

4. row 
    1개의 row안에 12개의 column영역이 구성
    ex)
    <div class="container">
    <div class="row">
      <div class="col-3">
        <div class="box">col</div>
      </div>
      <div class="col-3">
        <div class="box">col</div>
      </div>
      <div class="col-3">
        <div class="box">col</div>
      </div>
      <div class="col-3">
        <div class="box">col</div>
      </div>
    </div>
  </div>

  gutter는 좌우는 padding, 상하는 margin으로 민다
    거터에 대한 조정은 행에서 조정
    gx-숫자 = 좌우에 대한 조정
    gy-숫자 = 상하에 대한 조정
    g-숫자 = 좌우상하 전부

### Responsive Web Design
디바이스 종류나 화면 크키에 상관없이 어디서든 일관된 레잉아웃 및 사용자 경험을 제공하는 디자인 기술

각 breakpoint 마다 설정된 최대 너비 값 "이상으로"
화면이 커지면 grid system 동작이 변경됨

사용예시
<div class="col-사이즈-숫자">


