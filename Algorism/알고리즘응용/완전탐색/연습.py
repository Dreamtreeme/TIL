# 카드 연속

card = ["A","J","Q","K"]
path = []
result = 0

def count_three(path):
    for i in range(len(path)-2):
        if path[i]==path[i+1] == path[i+2]: return True

def recur(cnt):
    global result
    if cnt == 5:
        if count_three(path):
            result+=1
            print(path)
        return
    
    for idx in range(4):
        path.append(card[idx])
        recur(cnt+1)
        path.pop()

recur(0)
print(result)