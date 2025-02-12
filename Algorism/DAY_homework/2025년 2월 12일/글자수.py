T=int(input())
for case in range(1, T+1):
    result=0
    #str1 : 중복된 글자가 있어도 하나만 카운트 set저장
    #str2: 중복된 글자 있으면 여러번 카운트 list저장
    char_set = set([c for c in input().strip()])
    arr = [c for c in input().strip()]

    cnt = {}
    for c in char_set:
        cnt[c] = 0

        for ch in arr:
            if c==ch:
                cnt[c] +=1

    print(f"#{case} {max(cnt.values())}") 