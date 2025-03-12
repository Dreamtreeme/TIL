# idx를 이미썻다면 뽑지않는경우
for i in range(k, N+1):
        if not visited[i]: 
            visited[i] = True 
            sequence.append(i)  
            backtrack(sequence, visited, N, M,i+1)  
            sequence.pop() 
            visited[i] = False 