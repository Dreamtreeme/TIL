arr = [1,2,3,4,5,6,7,8,9,10]

# 합이 10인 부분집합
# 가지치기론 합이 10 이상인건 쳐냄
cnt=0
for i in range(1<<len(arr)):
    result=0
    li=[]
    
    for j in range(len(arr)):
        if i &(1<<j):
            result += arr[j]
            li.append(arr[j])
        if result>10:
            
            break
    if result==10:
        cnt+=1
        print(li)
print(cnt)
