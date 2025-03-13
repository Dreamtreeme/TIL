# 주사위 눈금 N개를 던져서 나올 수 있는 모든 조합

dice = [1,2,3,4,5,6]
path = []
n=3
def d(cnt, start):
    if cnt == n:
        print(path)
        return
    
    for i in range(start, 7):
        path.append(i)
        d(cnt+1,i)
        path.pop()

d(0,1)