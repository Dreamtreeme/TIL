T=int(input())
for case in range(1,T+1):
    str1 = input()
    # 많이 넣을 필요도 없이 겹치는 마디 2부분만 비교
    for word_len in range(1,word_len//2+1):
        if len(str1) % word_len ==0:
            s1=str1[0:word_len]
            s2=str1[word_len:2*word_len]
            if s1==s2:
                result=word_len
                break
    
    print(f'#{case} {result}')