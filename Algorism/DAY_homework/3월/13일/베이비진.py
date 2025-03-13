def triplet(arr):
    cnt=1
    simbol = arr[0]
    for i in range(1,len(arr)):
        if cnt>=3:
            return True
        if arr[i]==simbol:
            cnt+=1
        else:
            simbol = arr[i]
            cnt=1
    
    
def run1(arr):
    simbol = arr[0]
    cnt=1
    for i in range(1,len(arr)):
        if cnt>=3:
            return True
        if arr[i] == simbol+1:
            simbol+=1
            cnt+=1
        else :
            simbol = arr[i]
            cnt=1
    


T= int(input())
for tc in range(1, T+1):
    N = list(map(int,input().split()))
    player1=[]
    player2=[]
    result=0
    for i in range(len(N)):
        if i>4:
            if i%2==0:
                player1.append(N[i])
                player1.sort()
                if triplet(player1) or run1(player1):
                    result =1
                    break
            else:
                player2.append(N[i])
                player2.sort()
                if triplet(player2) or run1(player2):
                    result =2
                    break
        else:
            if i%2==0:
                player1.append(N[i])
            else:
                player2.append(N[i])

    print(f'#{tc} {result}')