def dfs(cnt, newli):
    global result
    num_sum = sum(newli)
    if num_sum > 100:
        return
    if cnt == 7 and num_sum == 100:
        newli.sort()
        result = newli[:]
        return 
    for i in range(cnt, 9):
        if visited[i]:
            continue
        if result: 
            return
        newli.append(li[i])
        visited[i] += 1
        dfs(cnt + 1, newli)
        visited[i] -= 1
        newli.pop()

li = [0] * 9
for i in range(9):
    li[i] = int(input())
visited = [0] * 9
result = 0
dfs(0, [])

for i in range(7):
    print(result[i])