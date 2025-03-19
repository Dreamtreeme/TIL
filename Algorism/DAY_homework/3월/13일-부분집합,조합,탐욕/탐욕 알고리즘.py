coin = [ 500, 100, 50, 10] # 큰 동전부터 앞으로 작성

target = 1730
cnt = 0

for i in coin:
    possible_cnt = target//i
    cnt += target//i          # 정답에 더해줌
    target = i * possible_cnt # 금액을 뺴준다


## 화장실 문제

people = [15,30,50,10]
n = 4

# 접근법, 최소 시간인 사람부터 화장실로 들어가자

people.sort() # 오름 차순 정렬

total_time = 0 
remain_people = n-1 #대기인원수

for i in range(n):
    total_time+=(people[i]*remain_people)
    remain_people-=1

print(total_time)
