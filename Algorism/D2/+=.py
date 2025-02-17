T = int(input())

for _ in range(T):
    result = 0
    A, B, N = list(map(int, input().split()))
    count=0
    count2=0
    while True:
        if A>B:
            B+=A
            count+=1
            if B>N:
                result = count+count2
                break
        else:
            A+=B
            count2+=1
            if A>N:
                result = count+count2
                break
        


    
    print(result)