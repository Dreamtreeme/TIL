def backtrack(sequence, visited, N, M,k):
    
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return

    for i in range(k, N+1):
        if not visited[i]: 
            visited[i] = True 
            sequence.append(i)  
            backtrack(sequence, visited, N, M,i+1)  
            sequence.pop() 
            visited[i] = False 

N, M = map(int, input().split())

visited = [False] * (N + 1)

backtrack([], visited, N, M,1)