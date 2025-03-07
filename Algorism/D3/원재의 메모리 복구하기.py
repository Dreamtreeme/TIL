T= int(input())
for tc in range(1, T+1):
    str1=input()
    str2=""
    cnt=0
    for i in str1:
        
        if i =="0" and cnt==0:
            continue
        if i =="1" and cnt==0:
            cnt+=1
        elif i == "0" and cnt!=0 and str2!="0":
            cnt+=1
        elif i =="1" and cnt !=0 and str2!="1":
            cnt +=1
        str2=i

    print(f'#{tc} {cnt}')