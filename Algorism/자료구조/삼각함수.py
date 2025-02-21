# import math
# # 공 A의 좌표 (x1,y1)
# # 공 B의 좌표 (x2,y2)
# x1,y1=(0,0)
# x2,y2=(4,7)

# # 삼각형의 형태를 구하려면
# def calculate_distance(x1, y1, x2, y2):
#   """두 점 사이의 거리를 계산하는 함수"""
#   return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# # 3좌표중 목적구, 홀, 흰공
# # 흰공과 홀의 거리 a
# # 흰공과 목적구 거리 c
# # 목적구와 홀의 거리 b

# # 흰공과 목적구 각도 = 
# # math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))
# a=5
# b=4
# c=3
# angle_degrees = math.degrees(math.acos((a**2 +b**2 -c**2))/(2*a*b))

# # 새로운 각도 계산
# new_angle_degrees = angle_degrees + 5.14

# # 라디안 단위로 변환
# new_angle_radians = math.radians(new_angle_degrees)

# # d 계산
# d = a * math.tan(new_angle_radians)

# # 결과 출력
# print("d:", d)
import math

a = 5
b = 4
c = 3

# 흰공과 목적구 사이의 각도 (계산된 값 활용)
angle_degrees = math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))

# 새로운 각도 계산
new_angle_degrees = angle_degrees + 5.14

# 라디안 단위로 변환
new_angle_radians = math.radians(new_angle_degrees)

# d 계산
d = a * math.tan(new_angle_radians)

# 결과 출력
print("d:", d)

# 1  좌표조정 -2.5씩 해놓기
# 2  선공후공 조건 달기 모든 좌표 선공후공 나눠놓기
# 3. 홀 정하기
# 4. 홀을 정했으면 세점에대한 공식 돌려보기
# 5. 최적의 각도가 나왔으면 구한 탄젠트값에
# 범위조정 4+-1 2, 조정
# 6. 만약 범위에 들어가면 쿠션 생각해보기
# 좌표 4분면에대해 모든 좌표 반전시키고 다시계산