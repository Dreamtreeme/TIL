T = 10

def calc_val(o,l,r):
    if o == '+':
        return l+r
    elif o == '-':
        return l-r
    elif o == '*':
        return l*r
    elif o == '/':
        return l/r

def calc_tree(i): # 루트노드가 i일때 서브트리의 계산결과
    global tree, N
    if tree[i]['is_op']: # 현재 루트노드가 연산자 노드라면
        lft_val = calc_tree(tree[i]['lft'])
        rgt_val = calc_tree(tree[i]['rgt'])
        return calc_val(tree[i]['op'], lft_val, rgt_val)
    else:
        return tree[i]['val']

for tc in range(1, T + 1):
    N = int(input())
    tree = {} # 트리를 딕셔너리로 저장
    # 정점번호 : key , value:노드의 내용

    for _ in range(N): #N개의 노드 정보가 주어짐
        tokens = input().split()
        # 정수 노드: 정점번호, 숫자
        # 연산자 노드: 정점번호, 연산자, 왼쪽, 오른쪽자식
        num = int(tokens[0]) # 정점번호
        if len(tokens) ==2:
            val = int(tokens[1]) # 두번째 토큰에 정수값
            tree[num] = {"num": num, "is_op":False, "val":val}#정점번호,연산자여부,정수값저장
        elif len(tokens) == 4:
            op = tokens[1]
            lft, rgt = int(tokens[2]),int(tokens[3])
            tree[num] = {"num": num, "is_op":True,'op':op ,"lft":lft, "rgt":rgt}
    
    # 루트 노드로부터 탐색을 한다.
    ans = calc_tree(1) #1번 노드가 루트 노드일 때의 계산 결과

    
    print(f'#{tc} {int(ans)}')
