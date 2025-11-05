import sys
input = sys.stdin.readline

n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))

min_diff = float('inf')

def make_teams(idx, start_team):
    global min_diff
    
    # 스타트팀 완성 (첫 번째 사람 포함해서 n/2명)
    if len(start_team) == n // 2:
        # 링크팀은 나머지
        link_team = []
        for i in range(n):
            if i not in start_team:
                link_team.append(i)
        
        # 능력치 계산
        start_power = 0
        link_power = 0
        
        for i in range(len(start_team)):
            for j in range(i + 1, len(start_team)):
                start_power += s[start_team[i]][start_team[j]]
                start_power += s[start_team[j]][start_team[i]]
        
        for i in range(len(link_team)):
            for j in range(i + 1, len(link_team)):
                link_power += s[link_team[i]][link_team[j]]
                link_power += s[link_team[j]][link_team[i]]
        
        min_diff = min(min_diff, abs(start_power - link_power))
        return
    
    # idx부터 n-1까지 중에서 선택
    for i in range(idx, n):
        start_team.append(i)
        make_teams(i + 1, start_team)
        start_team.pop()

# 0번 사람을 스타트팀에 고정하고 시작 (대칭성 제거)
make_teams(1, [0])
print(min_diff)