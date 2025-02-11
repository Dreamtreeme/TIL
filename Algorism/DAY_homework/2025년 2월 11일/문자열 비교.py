# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

# 예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.

T= int(input())
for case in range(1, T+1):
    result=0
    str1 = input()
    str2 = input()
    for i in range(len(str2)-len(str1)+1):
        sub_s =""
        for j in range(len(str1)):
            sub_s +=str2[i+j]
        if str1 == sub_s:
            result=1


    print(f"#{case} {result}") 