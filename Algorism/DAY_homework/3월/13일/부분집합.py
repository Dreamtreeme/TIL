# 친구 ["A","B","C","D","E"]
# 최소 2명시아 친구

friend=["A","B","C","D","E"]
cnt=0
for i in range(1<<len(friend)):
    result=[]
    for j in range(len(friend)):
        if i &(1<<j):
            result.append(friend[j])
    if len(result)>=2:
        cnt+=1
print(cnt)