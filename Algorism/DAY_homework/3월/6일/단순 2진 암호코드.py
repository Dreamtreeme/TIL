import sys
sys.stdin= open("input.txt" , "r")

#조건1 배열중 암호코드 부분을 따로 떼어내야한다.
# 조건2 암호코드부분을 해독해서 올바른 암호코드인지 확인한다.
code={"0001101":0,"0011001":1,"0010011":2,"0111101":3,
      "0100011":4,"0110001":5,"0101111":6,"0111011":7,
      "0110111":8,"0001011":9,}
T = int(input())
for tc in range(1,T+1):
    result=0
    video=[]
    count=1
    N,M = map(int,input().split())
    for _ in range(N):
        video.append(input())

    for i in range(N):
        if not "1" in video[i]:
            continue
        for j in range(M-1,-1,-1):
            if video[i][j]=="1":
                code1= video[i][j-55:j+1]
                break
    codekey=""
    odd=[]
    even=[]
    for i in code1:
        codekey+=i
        if len(codekey)==7 and count%2==1:
            count+=1
            odd.append(code[codekey])
            codekey = ''
        elif count%2==0 and len(codekey)==7:
            count+=1
            even.append(code[codekey])
            codekey = ''
        
    result=(sum(odd)*3)+(sum(even))
    
    if not result%10==0:
        result=0
    else:
        result= sum(odd)+sum(even)

    print(f'#{tc} {result}')