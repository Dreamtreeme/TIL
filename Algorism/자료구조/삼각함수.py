import math
# 공 A의 좌표 (x1,y1)
# 공 B의 좌표 (x2,y2)
x1,y1=(0,0)
x2,y2=(4,7)

# 삼각형의 형태를 구하려면
def calculate_distance(x1, y1, x2, y2):
  """두 점 사이의 거리를 계산하는 함수"""
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 3좌표중 목적구, 홀, 흰공
# 흰공과 홀의 거리 a
# 흰공과 목적구 거리 c
# 목적구와 홀의 거리 b

# 흰공과 목적구 각도 = 
# math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
a=3
b=4
c=5
math.degrees(math.acos((a**2 +b**2 -c**2))/(2*a*b))