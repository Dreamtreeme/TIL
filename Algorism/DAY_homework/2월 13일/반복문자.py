# 스택이용
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def stack_def(txt):
    stack = []
    for t in txt:
        if stack and stack[-1] == t:
            stack.pop()
        else:
            stack.append(t)
    return "".join(stack)
for test_case in range(1, T + 1):
    t= list(input())
    result= len(stack_def(t))

    print(f'#{test_case} {result}')

T = int(input())

# 재귀함수
# - 기저조건: 더이상 호출하지 않을 조건
# - 유도조건: 자기 자신을 호출하는 조건


def delete_repetition(text):
    # 기저조건: 만약에 text내에 반복이 없으면
    # => text를 그대로 그냥 return
    # 유도조건: 만약에 text내에 반복이 있다면
    # => 그 반복부분만 없앤 후 다시 재귀 호출

    # 1. 반복을 찾는다
    found = False # 반복이 있는지, 없는지 여부
    idx = -1 # 중복된 위치의 인덱스 기억
    for i in range(len(text) - 1):
        if text[i] == text[i+1]:
            found = True
            idx = i
            break

    if found: # 중복을 찾았다면(기저조건)
        return delete_repetition(text[:idx]+text[idx+2:])
    else: # 중복이 없다면( 기저조건)
        return text # 그대로 text 반환


for tc in range(1, T+1):
    text = input().strip()

    print(f"#{tc} {len(delete_repetition(text))}")

    
