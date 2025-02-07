T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    count_num =1
    count_list=[]
    count_list_num=10
    num2=0
    while count_list_num>0:
        num2 = N*count_num
        count_list.append(num2%10)
        num2 = N*count_num//10
        if num2 ==0:
            count_num+=1
            count_list_num-=1
    

    result = count_num
    print(f'#{test_case} {result}')