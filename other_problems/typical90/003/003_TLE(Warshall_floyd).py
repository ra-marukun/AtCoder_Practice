import io
import sys

##ここに入力テキストを入れる
_INPUT = """\
10
1 2
1 3
2 4
4 5
4 6
3 7
7 8
8 9
8 10

"""
sys.stdin = io.StringIO(_INPUT)

##ここ以降にコーディング
import sys

n = int(input())
xy = [map(int, sys.stdin.readline().split()) for _ in range(n-1)]
A, B = [list(i) for i in zip(*xy)]


def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]= min(d[i][j],d[i][k]+d[k][j])
    return d

INF = 10**10
cost = [[INF]*n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0

for a,b in zip(A,B):
    cost[a - 1] [b - 1] = 1
    cost[b - 1] [a - 1] = 1

m = warshall_floyd(cost)
ans = max(list(map(lambda x: max(x), m)))
print(ans+1)