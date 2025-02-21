import math
# 공 A의 좌표 (x1,y1)
# 공 B의 좌표 (x2,y2)
x1,y1=(0,0)
x2,y2=(4,7)

# 삼각형의 형태를 구하려면
def calculate_distance(x1, y1, x2, y2):
  """두 점 사이의 거리를 계산하는 함수"""
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)