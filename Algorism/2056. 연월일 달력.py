# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
 



# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면

# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,

# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.


# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며

# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
 


# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)

t= int(input())
for case in range(1,t+1):
    ymd = input()
    year = int(ymd[:4])
    month = int(ymd[4:6])
    day = int(ymd[6:])
    oddmonth = [1,3,5,7,8,10,12]
    evenmonth = [4,6,9,11]
    result = ymd[:4]+"/"+ymd[4:6]+"/"+ymd[6:]
    

    if year<1 :
        result = -1
    if not 0<month<13 :
        result = -1
    if month in oddmonth:
        if not 0<day<32:
            result = -1
    if month in evenmonth:
        if not 0<day<31:
            result = -1
    if month == 2:
        if not 0<day<29:
            result = -1
    print(f'#{case} {result}')