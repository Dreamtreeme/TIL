T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    count_num =1
    count_list=[]
    while len(count_list)!=10:
        num2 = N*count_num
        for i in str(num2):
            if not i in count_list:
                count_list.append(i)
                result = num2
        count_num+=1

    print(f'#{test_case} {result}')