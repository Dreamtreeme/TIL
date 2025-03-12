# 3개 주사위를 던져 나올수있는 중복 순열에 대해.
# 합이 10 이하가 나오는 경우는 총 몇가지

# 각 주사위는 독립시행-> 규칙성이 없어서 다 봐야함

d = []
result=0
def dice(cnt, total):
    global result
    if total >10:# 기저조건
        return
    if cnt==3 :
        
        result+=1
        print(*d)
        return
    
    
    for num in range(1, 7):
        d.append(num)
        dice(cnt+1, total+num)
        d.pop()


dice(0,0)
print(result)
