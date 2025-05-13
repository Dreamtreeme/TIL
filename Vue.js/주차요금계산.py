import math

def trans_time(time_str):
    h, m = map(int, time_str.split(':'))  # 시간:분을 직접 분리
    return h * 60 + m

def solution(fees, records):
    entry_times = {}  # 차량별 입차 시간 저장
    parking_times = {}  # 차량별 총 주차 시간 저장

    for r in records:
        time_str, car, action = r.split()
        minutes = trans_time(time_str)

        if action == 'IN':
            entry_times[car] = minutes
        else:  # 'OUT'
            duration = minutes - entry_times.pop(car, minutes)
            parking_times[car] = parking_times.get(car, 0) + duration

    # 23:59까지 주차된 차량 처리
    end_day = trans_time('23:59')
    for car, entry in entry_times.items():
        parking_times[car] = parking_times.get(car, 0) + (end_day - entry)

    # 차량 번호순으로 요금 계산
    base_time, base_fee, unit_time, unit_fee = fees
    return [
        base_fee + max(0, math.ceil((time - base_time) / unit_time)) * unit_fee
        for _, time in sorted(parking_times.items())
    ]

# fee = [기본시간, 기본요금, 단위시간, 단위요금]
# records = [ "차량1의 '시각 차량번호 내역'"]
# 시각 = "HH:MM" -> 00:00~23:59 잘못된 시각은 입력X
# 차량번호 = "0000"
# 내역 = "IN" or "OUT"
# records의 원소들은 시각을 기준으로 오름차순 정렬
# 마지막 시각에 입차되는 경우 입력으로 주어지지 않는다.
# 입력값 예시
# [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]


