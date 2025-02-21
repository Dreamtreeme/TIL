T=int(input())
for case in range(1,T+1):
    N = int(input())
    li={}
    li_key=[]
    str1=""
    for _ in range(N):
        Ci, Ki = map(str,input().split())
        Ki = int(Ki)
        li_key.append(Ci)
        li.update({Ci:Ki})
    
    print(f'#{case}')
    for i in range(N):
        str1+=li_key[i]*li[li_key[i]]
    
    for i in range(0,len(str1),10):
        print(str1[i:i+10])