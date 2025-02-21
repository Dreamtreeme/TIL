import math

RADIUS = 5.73
h = [ # 홀 좌표 (h, hole positions)
    (2,2), # 좌하단
    (127,2), # 중앙하단
    (252,2), # 우하단
    (2,125), # 좌상단
    (127,125), # 중앙상당
    (252,125) #우상단
]
def cal_di(t1,t2):
  """두 점 사이의 거리를 계산하는 함수"""
  x1,y1=t1
  x2,y2=t2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def trans(c): # 문자열 -> 튜플 리스트 변환 함수 (trans, transform string to tuple list func)
    """
    'x/y/x/y/...' 형태 문자열 -> 좌표 튜플 리스트 변환.
    '-1/-1' 좌표는 (-1, -1) 튜플로.

    Args:
        c: 'x/y/x/y/...' 형태 좌표 문자열 (c, coordinate string).

    Returns:
        list: 좌표 튜플 리스트 (list).
    """
    cl = c.split('/') # 좌표 문자열 리스트 (cl, coordinate list)
    tl = [] # 튜플 리스트 (tl, tuple list)
    for i in range(0, len(cl), 2):
        xs = cl[i] # x 좌표 문자열 (xs, x string)
        ys = cl[i+1] # y 좌표 문자열 (ys, y string)
        x = int(xs) # x 좌표 (x)
        y = int(ys) # y 좌표 (y)
        tl.append((x, y))
    return tl

def cal_d(a, c, 사이각_degrees):
  사이각_radians = math.radians(사이각_degrees)
  d_squared = a**2 + c**2 - 2 * a * c * math.cos(사이각_radians)
  d = math.sqrt(d_squared)
  return d

def get_angle_degrees(hole_x, whiteball_x, hole_y, whiteball_y):
  """
  흰 공 좌표와 목적 홀 좌표 사이의 각도를 degree 단위로 계산합니다.

  Args:
      hole_x: 목적 홀의 x 좌표
      whiteball_x: 흰 공의 x 좌표
      hole_y: 목적 홀의 y 좌표
      whiteball_y: 흰 공의 y 좌표

  Returns:
      각도 (degree)
  """
  dx = hole_x - whiteball_x
  dy = hole_y - whiteball_y
  탄젠트_값_라디안 = math.atan2(dy, dx)
  각도_degree = math.degrees(탄젠트_값_라디안)
  return 각도_degree

player =0
ex_s = "64/64/250/120/-1/-1/10/120/-1/-1/-1/-1" # '-1/-1' 포함 예시 문자열 (ex_s, example string)
conv_t = trans(ex_s) # 변환된 튜플 (conv_t, converted tuple)

if player==0:
    whiteball=conv_t[0]
    target =[conv_t[1],conv_t[3],conv_t[5]]
    non_target = [conv_t[2],conv_t[4]]
else:
    whiteball=conv_t[0]
    non_target =[conv_t[1],conv_t[3]]
    target = [conv_t[2],conv_t[4],conv_t[5]]

conv_t.pop(0)

next_target= target.pop(0)

b=cal_di(whiteball,next_target)
min_di =1000000
loca={}
h_di=[]
for i in h:
    di = cal_di(next_target,i)
    h_di.append(di)
    loca.update({di:i})

c= min(h_di)
a= cal_di(whiteball,loca[min(h_di)])
atan = (loca[min(h_di)])[0]-whiteball[0]

# 홀 목적구 각도 = 
angle_degrees = math.degrees(math.acos((c**2 + a**2 - b**2) / (2 * c * a)))

c1= RADIUS+c
d=cal_d(a,c1,angle_degrees)









    