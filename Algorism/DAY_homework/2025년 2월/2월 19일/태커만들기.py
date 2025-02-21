import random

N=4

arr = [ [str(random.randint(1, 500)) for c in range(N)] for r in range(N)]

for row in arr:
    print(' '.join(row))