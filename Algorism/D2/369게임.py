N = int(input())
arr=[]
for i in range(1, N+1):
    s =str(i)
    s2=""
    for j in range(len(s)):
        if int(s[j])>0 and int(s[j])%3==0:
            s2+="-"
    if s2=="":
        arr.append(s)
    else:
        arr.append(s2)
    result = " ".join(arr)
print(result) 
    