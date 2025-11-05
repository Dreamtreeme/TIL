def solution(s):
    
    numstr = ["zero",'one','two','three','four','five','six','seven','eight','nine','ten']
    numbers = {}
    for i in range(10):
        numbers[numstr[i]] = str(i)
    
    for n in numstr:
        while n in s:
            s = s.replace(n, numbers[n])
    answer = s
    return answer

print(solution("1oneone"))