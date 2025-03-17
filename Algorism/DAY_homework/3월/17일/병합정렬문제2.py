# [lft, rgt)
# 왼쪽 포함, 오른쪽 포함하지않음
def mergesort(lft, rgt):
    
    # 먼저 길이가 1인것까지 쪼갠다.
    if lft +1 <rgt:

        mid = (lft + rgt) //2
        mergesort(lft,mid)
        mergesort(mid,rgt)

        # 2. 쪼개진 배열을 합친다.
        merge(lft, mid, rgt)

# 주어진 배열에서
# L : [lft, mid), R: [mid,rgt) 부분만 복사를 해서 L,R을 만든다.
# L,R을 합치면서 arr에다 덮어쓴다.
def merge(lft, mid, rgt):
    global arr, cnt

    # 내가 쓸 부분만 복사 떠오기
    L = arr[lft:mid]
    R = arr[mid:rgt]

    if L[-1]>R[-1]:
        cnt+=1
    i = j = 0
    k = lft
    while i < mid-lft and j < rgt -mid:
        if L[i] <= R[j]:
            arr[k] = L[i]
            k+=1
            i+=1
        else:
            arr[k] = R[j]
            k+=1
            j+=1

    while i < mid - lft:
        arr[k] = L[i]
        k +=1
        i+=1

    while j < rgt- mid :
        arr[k] = R[j]
        k +=1
        j+=1
T = int(input())
for tc in range(1, T+1):
    N= int(input())
    arr = list(map(int,input().split()))

    # 보통은 구간을 폐구간으로 놓는 것이 편함
    # [s, e] : s ~ e(e도 포함)

    # 이 문제는 오른쪽이 열린 구간으로 되어있음
    # [0, N)
    # 모든 구간은 한쪽이 열린 구간으로 통일
    cnt=0
    mergesort(0, N)
    print(f'#{tc} {arr[N//2]} {cnt}')