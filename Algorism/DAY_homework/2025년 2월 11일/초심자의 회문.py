# 단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.

T= int(input())
for case in range(1, T+1):
    result=0
    str1 = input()
    sub_s =""
    
    for i in range(len(str1)):
        sub_s +=str1[i]
    for i in range(len(str1)//2):
        con =True
        if sub_s[i] != sub_s[len(str1)-1-i]: #맨앞 맨뒤 비교
            con = False
            break
    if con:
        result=1
    print(f"#{case} {result}") 

    
