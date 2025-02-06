# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
'''
풀이 추측:
버스 예시를 보면 정류장은 N개, 최대거리K,충전기설치M이 있다.
풀이 방식은 버스의 위치를 항상 감지해야한다. 그리고 그 버스를 중심으로 다음 정류장에
도달 할 수 있는지 없는지 판단한다.

'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    charge_location = list(map(int, input().split()))
    
    current_bus_location =0
    max_charge = 0
    
    charge_idx= 0
    while current_bus_location+K <N:
        max_k= 0
        for i in range(M):
            if current_bus_location<charge_location[i]<=current_bus_location+K:
                max_k =charge_location[i]
        if max_k==0:
            max_charge=0
            break
        current_bus_location = max_k
        max_charge+=1
    print(f'#{test_case} {max_charge}')
