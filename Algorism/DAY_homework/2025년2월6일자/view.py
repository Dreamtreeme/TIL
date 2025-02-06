T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N=int(input())
    li = list(map(int,input().split()))
    buliding = N-4
    building_li = li[2:N-1]
    result=0
    for i in range(2, buliding+2):
        view=0
    	
        if li[i-2]<building_li[i-2]:
            view+=1
        if li[i-1]<building_li[i-2]:
            view+=1
        if li[i+1]<building_li[i-2]:
            view+=1
        if li[i+2]<building_li[i-2]:
            view+=1
        if view == 4:
            result+=building_li[i-2]-max([li[i-2],li[i-1],li[i+1],li[i+2]])
            
    print(f'# {test_case} {result}')
