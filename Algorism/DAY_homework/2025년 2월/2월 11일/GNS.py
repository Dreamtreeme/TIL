# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# 풀이방법
# 일단 0부터 9까지 기준 딕셔너리 만듦
def selection_sort(items):
    for i in range(len(items)):
        min_idx = i
        for j in range(i+1, len(items)):
            if items[min_idx][1] > items[j][1]:  # 값 기준으로 비교
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    return items


def sort_li(li,my_dict):
    pairs = [(s, my_dict.get(s, 0)) for s in li]

    # 값 기준으로 정렬
    pairs=selection_sort(pairs)
    # 정렬된 문자열만 추출
    sorted_list = [pair[0] for pair in pairs]

    return sorted_list

T= int(input())
for case in range(1,T+1):
    str_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    my_dict={}
    li_num= input()
    for i in range(10):
        my_dict.update({str_list[i]:i})
    li = list(input().split())
    my_list = sort_li(li, my_dict)
    result = ' '.join(my_list)
    print(f'#{case}')
    print(result)