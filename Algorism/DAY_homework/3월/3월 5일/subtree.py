
def treenode(n,tree):
     
    count = 1
    for nextnode in tree[n]:
        count += treenode(nextnode, tree)
    return count

T=int(input())

for tc in range(1, T+1):
    
    E,N= map(int,input().split())
    order=list(map(int,input().split()))
    tree = [[] for _ in range(max(order)+1)]
    for _ in range(E):
         node=order.pop(0)
         value=order.pop(0)
         tree[node].append(value)
    result =treenode(N,tree)
    

    print(f'#{tc} {result}')