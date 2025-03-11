# 트리의 루트는 1/1을 나타냄
# 트리의 각 노드는 왼쪽,오른쪽 자식을 가짐 왼쪽자식은 a/a+b, 오른쪽 자식은 a+b /b
import sys
sys.stdin= open("input.txt" , "r")
T= int(input())
for tc in range(1, T+1):
    str1=input()
    a, b = 1, 1
    for i in str1:
        if i == "L":
            a,b = a ,a+b
        elif i == "R":
            a,b = a+b ,b
    
    print(f'#{tc} {a} {b}')