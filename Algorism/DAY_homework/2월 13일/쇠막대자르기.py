T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    txt = input()
    result=0
    top = 0
    stack = [0] * 500000
    li=[0]

    for x in txt:
        if x == '(': # (경우
            top+=1
        else:           # )인 경우
            top-=1
        li.append(top)
    # 커트 지점을 기점으로 양 옆값 더함. 그리고 커트지점과 지점 사이의 요소들중 가장 낮은 요소를 뺌


    cut_idx=[]
    for i in range(len(txt)-1):
        if txt[i]+txt[i+1] == "()":
            cut_idx.append(i+1)
            result += (li[i]+li[i+2])
    for c in range(len(cut_idx)-1):

        result -= min(li[cut_idx[c]:cut_idx[c+1]])

    print(f'#{test_case} {result}')

