하태오 삼성전자 DS AI 제조

### 객체 검출 알고리즘

이미지에서 객체를 검출하는 알고리즘

1. 각 객체가 어떤 class 에 속하는지 판단하는 classification

2. 각 객체의 위치가 어디에 있는지 판단하는 localization

딥러닝에서 학습이란?
원하는 y값을 얻기 위해서 w값을 튜닝하는 과정

loss함수
- x를 넣었을때 지금의 y와 원하는 y값이 차이가 얼마인지 나타낸값

MSE (y-y)^2

객체 검출 알고리즘의 평가지표

IoU intersection over union

진짜 구역(ground truth box)과 예측구역(bounding box)가 얼마나 일치하는지 

precision정밀도 : 예측을 p로 한 대상중에 실제로p인 비율
recall재현율: 실제 값이 p인 대상 중에 예측도 p로 나온 비율

Confidence
- 객체 검출이 얼마나 신뢰할 수 있느냐에 대한 값
- confidence의 Threshold를 설정하여 그 이상의 값을 가지는 객체만 output으로 출력하게됨

threshold를 처음엔 모두 보다 학습이 진행되고 어느정도 신뢰도가 있다고 판단될때 높이면 될듯?


### YOLO 넌 하나만 봐라

- 기존의 고전적인 객체탐지
    범주화와 범위화를 따로따로 풀었음

- 욜로가 한번만 보는이유
    한번에 품
    실시간으로 객체 탐지가 가능

- 빠르면서도 정확한 객체 탐지를 할 수 있다.

### YOLO의 동작방식

1. CNN network input size에 맞게 이미지 크기 조정
2. CNN 네트워크 동작
3. Non-max suppression
    추출된 바운딩박스에서 신뢰도가 높은 바운딩 box만 남김

1. s*s의 grid cell로 나눔

2. 각 그리드 셀에 대해 상대좌표로 바운딩 박스 후보추출

3. 각각의 그리드 셀은 어떤 물체 class에 속할지 확률을 계산

- 학습 loss
 - 각 박스별 바운딩박스 위치 정확도
 - 예측된 신뢰도의 정확도
 - 예측된 클래스의 정확도


### DETR 모델

- 트랜스포머 모델

바운딩 박스를 실체 물체 개수만큼 출력하면 안되나
NMS의 한계
겹쳐있는 물체를 잘 인식하지 못함

DETR의 특징
기존 CNN기반보다 더 적은 수의 바운딩박스만 출력하고 NMS를 사용하지 않음

loss
N 개의 output을 M개의 실제 객체와 매칭시켜중(헝가리안 알고리즘)

각 쌍이 얼마나 fit하게 맞아 떨어지는지 계산해줌

class에 대한 loss도 계산해줌

### pyTorch

Linux환경추천
python 3.7
cuda 9.2
pytorch 1.8 이상

MMDetection 설치

에러가 난경우

pip install wheel 을 하고 다시 설치
혹은 torch를 1.13.0 버전 이하로 설치




