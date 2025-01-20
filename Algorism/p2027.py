# 2027. 대각선 출력하기
answer = []

for i in range(5):
    row = ''
    for j in range(5):
        if i == j:
            row+='#'
        else:
            row+='+'
    answer.append(row)
for i in answer:
    print(i)